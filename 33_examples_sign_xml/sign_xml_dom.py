import base64
import re
import xml
from xml.dom.minidom import Document

import signxml
from lxml import etree
from signxml import XMLSigner, XMLVerifier
from cryptography.hazmat.primitives import serialization


class AlipaySignXml:

    __encoding = "utf-8"

    @classmethod
    def sign_xml(cls, private_key: str, xml_text: str) -> etree.Element:
        # 解析 XML 数据
        xml_doc = cls.to_xml(xml_text)

        # 使用 sha256WithRSA 对 XML 进行签名
        signed_xml_doc = XMLSigner(
            method=signxml.algorithms.SignatureConstructionMethod.enveloped,
            signature_algorithm=signxml.algorithms.SignatureMethod.RSA_SHA256,  # 指定使用 sha256WithRSA 算法
            digest_algorithm=signxml.algorithms.DigestAlgorithm.SHA1,
            c14n_algorithm=signxml.algorithms.CanonicalizationMethod.CANONICAL_XML_1_0,
        ).sign(xml_doc, key=private_key)

        return cls.__remove_keyinfo(signed_xml_doc)

    @classmethod
    def sign_xml_adaptation(cls, private_key: str, xml_text: str) -> Document:
        signed_xml_doc = cls.sign_xml(private_key, xml_text)
        return cls.__wrapper_request_doc(signed_xml_doc, xml_text)

    @classmethod
    def verify_xml(cls, public_cert: str, signed_xml: str) -> etree.Element:
        # signed_xml_doc = cls.to_xml(signed_xml)
        cleaned_string = re.sub(r'[^\x20-\x7E]', '', signed_xml)
        signed_xml_doc = etree.fromstring(cleaned_string)
        print("==================================")
        print(cleaned_string)

        # 验证签名
        verified_data = XMLVerifier().verify(signed_xml_doc, x509_cert=public_cert).signed_xml

        print("Verified XML with SHA256withRSA:")
        print(cls.to_string(verified_data))
        return verified_data

    @classmethod
    def to_bytes(cls, request_doc: Document) -> bytes:
        return request_doc.toxml(encoding=cls.__encoding)

    @classmethod
    def to_string(cls, signed_xml_doc: etree.Element, pretty=False) -> str:
        return etree.tostring(signed_xml_doc, encoding=cls.__encoding, xml_declaration=True, method="xml", pretty_print=pretty).decode(cls.__encoding)

    @classmethod
    def to_xml(cls, signed_xml: str) -> etree.Element:
        return etree.fromstring(signed_xml.encode(cls.__encoding), parser=etree.XMLParser(encoding=cls.__encoding, remove_blank_text=True, remove_pis=True, remove_comments=True))

    @classmethod
    def __wrapper_request_doc(cls, signed_xml_doc: etree.Element, xml_text: str) -> Document:
        import xml.dom.minidom

        # 提取 <ds:SignedInfo> 和 <ds:SignatureValue>
        signed_doc = xml.dom.minidom.parseString(AlipaySignXml.to_string(signed_xml_doc))
        signed_info_el = signed_doc.getElementsByTagName("ds:SignedInfo")[0]  # 提取加签后的节点
        signature_value_el = signed_doc.getElementsByTagName("ds:SignatureValue")[0]

        # 创建新的 <ds:Signature> 元素
        request_doc = xml.dom.minidom.parseString(xml_text)
        signature_el = request_doc.createElement('ds:Signature')
        signature_el.setAttribute('xmlns:ds', 'http://www.w3.org/2000/09/xmldsig#')
        signature_el.appendChild(signed_info_el)
        signature_el.appendChild(signature_value_el)

        # 将 <ds:Signature> 元素添加到请求 XML 的 <document> 元素中
        root = request_doc.getElementsByTagName("document")[0]
        root.appendChild(signature_el)
        return request_doc

    @classmethod
    def __remove_keyinfo(cls, signed_xml_doc: etree.Element) -> etree.Element:
        # 手动移除 <ds:KeyInfo> 元素
        for key_info in signed_xml_doc.findall(".//{http://www.w3.org/2000/09/xmldsig#}KeyInfo"):
            key_info.getparent().remove(key_info)

        return signed_xml_doc


def load_and_print_private_key(encode_private_key):
    try:
        # 移除可能存在的 PEM 标头和尾部
        encode_private_key = encode_private_key.replace("-----BEGIN PRIVATE KEY-----", "")
        encode_private_key = encode_private_key.replace("-----END PRIVATE KEY-----", "")
        encode_private_key = encode_private_key.replace(" ", "").replace("\n", "")

        # 解码 Base64 编码的私钥
        private_key_bytes = base64.b64decode(encode_private_key)

        # 尝试从 DER 或 PEM 编码的字节中加载私钥
        try:
            # 首先尝试作为 PKCS8 DER 编码的私钥加载
            private_key = serialization.load_der_private_key(
                private_key_bytes,
                password=None,  # 如果私钥是加密的，这里提供密码
            )
        except ValueError:
            # 如果失败，尝试作为 PKCS8 PEM 编码的私钥加载
            private_key = serialization.load_pem_private_key(
                private_key_bytes,
                password=None,  # 如果私钥是加密的，这里提供密码
            )

        return private_key
        """
        # 将私钥序列化为 PEM 格式的字节串，不加密
        pem_private_key = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )

        # 将字节串转换为字符串
        pem_private_key_str = pem_private_key.decode('utf-8')

        # 打印私钥字符串
        print("Private Key (PEM format):\n", pem_private_key_str)
        return pem_private_key_str
    """
    except base64.binascii.Error as e:
        print("Base64解码失败: 请确认输入的是有效的Base64编码字符串。\n", e)
    except ValueError as e:
        print("私钥加载失败: 可能私钥格式不正确或被加密了。\n", e)
    except Exception as e:
        print("发生未知错误:\n", e)


def test_simple():
    data_to_sign = """<root><element1>data</element1><element2>more data</element2></root>"""
    api_config = config.AlipayTestEnvConfig.get_api_config()

    xml_doc = AlipaySignXml.sign_xml(api_config.sign_private_key, data_to_sign)
    sign_xml = AlipaySignXml.to_string(xml_doc)
    print(sign_xml)

    AlipaySignXml.verify_xml(config.AlipayTestEnvConfig.local_verify_public_key, sign_xml)

def test_simple2():
    data_to_sign = """<document><request>abc</request></document>"""
    api_config = config.AlipayTestEnvConfig.get_api_config()

    xml_doc = AlipaySignXml.sign_xml_adaptation(api_config.sign_private_key, data_to_sign)
    sign_xml = AlipaySignXml.to_bytes(xml_doc)
    print(sign_xml)

    AlipaySignXml.verify_xml(config.AlipayTestEnvConfig.local_verify_public_key, sign_xml.decode("utf-8"))

def test_example():
    data_to_sign = """
<document>
    <request id="request">
        <head>
            <Version>1.0.0</Version>
            <Function>ant.mybank.merchantprod.merch.applet.register.query</Function>
            <AppId>2021063000000572</AppId>
            <Appid>2021063000000572</Appid>
            <ReqTime>20250104191040</ReqTime>
            <ReqMsgId>1d3c8791c86f45e588dce7682179ad9f</ReqMsgId>
            <InputCharset>UTF-8</InputCharset>
            <SignType>RSA</SignType>
            <ReqTimeZone>UTC+8</ReqTimeZone>
            <Reserve></Reserve>
        </head>
        <body>
        <OutMerchantId>556061744625414223</OutMerchantId>
        <IsvOrgId>202211000000000000572</IsvOrgId>
        </body>
    </request>
</document>
"""

    api_config = config.AlipayTestEnvConfig.get_api_config()

    xml_doc = AlipaySignXml.sign_xml_adaptation(api_config.sign_private_key, data_to_sign)
    sign_xml = AlipaySignXml.to_bytes(xml_doc)
    print(sign_xml)

    AlipaySignXml.verify_xml(config.AlipayTestEnvConfig.local_verify_public_key, sign_xml.decode("utf-8"))

def verify_example():
    sign_xml = """
    <document>  <response id="response">    <head>      <Version>1.0.0</Version>      <AppId>2021063000000572</AppId>      <Function>ant.mybank.merchantprod.merch.applet.register.query</Function>      <RespTimeZone>UTC+8</RespTimeZone>      <RespTime>20250106023808</RespTime>      <ReqMsgId>763d02c157cd4e2cb291182f6d7a28c5</ReqMsgId>      <InputCharset>UTF-8</InputCharset>      <SignType>RSA</SignType>    </head>    <body>      <RespInfo>        <ResultStatus>S</ResultStatus>        <ResultCode>0000</ResultCode>        <ResultMsg>处理成功</ResultMsg>      </RespInfo>      <OutMerchantId>556061744625414223</OutMerchantId>    </body>  </response><Signature xmlns="http://www.w3.org/2000/09/xmldsig#">
<SignedInfo>
<CanonicalizationMethod Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315"></CanonicalizationMethod>
<SignatureMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256"></SignatureMethod>
<Reference URI="">
<Transforms>
<Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature"></Transform>
</Transforms>
<DigestMethod Algorithm="http://www.w3.org/2000/09/xmldsig#sha1"></DigestMethod>
<DigestValue>JOAEIzpjRufg8Ez+BqUvBXv3sf0=</DigestValue>
</Reference>
</SignedInfo>
<SignatureValue>
RiF7R8M7+QL8R1pI/wdIUtRS4nO137/vURDbVTgo2wMpeRtP1TQ/FOxhLDolKvrOHOE3009jgDPU
PTKHXvKZoezVtVYC/KIT3rGFCVj5MjS2ad+CCz3bfTv8oPOvpuT1vwc6QotiTXaZtF2kiKPeryJa
R0TL7ndG1OW+F17A7FE=
</SignatureValue>
</Signature></document>
    """

    api_config = config.AlipayTestEnvConfig.get_api_config()
    AlipaySignXml.verify_xml(api_config.verify_public_key, sign_xml)

if __name__ == '__main__':
    # test_simple()
    # test_simple2()
    # test_example()
    verify_example()