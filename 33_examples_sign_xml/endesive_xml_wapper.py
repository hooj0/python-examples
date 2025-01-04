from unittest import TestCase
import endesive.xml
from lxml import etree

class SignXmlTest(TestCase):

    def test_bank_sign_xml(self):
        # 原始 XML 数据
        data_to_sign = """
        <root>
            <element1>data</element1>
            <element2>more data</element2>
        </root>
        """

        with open("bank/private_key.pem", "r") as file:
            key = file.read()

        sign_xml(key, data_to_sign)

    def test_bank_verify_xml(self):
        # 签名后的 XML 数据
        signed_xml = """
        <root>
            <element1>data</element1>
            <element2>more data</element2>
        <ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#"><ds:SignedInfo><ds:CanonicalizationMethod Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315"/><ds:SignatureMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256"/><ds:Reference URI=""><ds:Transforms><ds:Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature"/><ds:Transform Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315"/></ds:Transforms><ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"/><ds:DigestValue>jmXnyWOraUghEOaDv0DVWsxBAIoCxarukS+agLBVBcc=</ds:DigestValue></ds:Reference></ds:SignedInfo><ds:SignatureValue>JZya3cs4vd8dhv8D1iLts+2PHFg6Swd1zeNOVEni9kUYQqVyC3uF/d6mfmTK8ibsj7SkkzaS6A1H7m4Dq8Ge8snQX8JcEqwI0YUsGqUzjsKH1W8mcrQ44xK50OlxOFXYKsmBXWC4jZDKLvh0qP1k7Auf9OMNz3b3/aZbU4EqJ8ZnWOyXzo3INQgPuJuilVdFwDjET2mA9Bj+4lI+YhxWeDc8O28JGDAzP4v8xdwp+8Pe+NTXtaDVsghffkfSykAGm+WXjwWP12lOUhp0L8GSSE9D3AUupOtW4vDrpdJpim4fNBy2BLZgf1pSbsrjRYPiukZv2Z4QljiIP2TMC68xYA==</ds:SignatureValue></ds:Signature></root>
        """

        with open("bank/public_cert.pem", "r") as file:
            key = file.read()

        verify_xml(key, signed_xml)

def sign_xml(private_key, xml_text):
    # 解析 XML 数据
    xml_doc = etree.fromstring(xml_text.encode('utf-8'), parser=etree.XMLParser(encoding='utf-8'))
    print(xml_doc)

    # 使用 endesive 库进行签名
    def get_signer():
        return endesive.xml.signedsig.Signature(
            x509cert=private_key,
            key=private_key,
            hashalg='sha256',
            method='enveloped'
        )

    signed_xml_doc = endesive.xml.sign(xml_doc, get_signer(), False)
    print(signed_xml_doc)

    # 将签名后的 XML 转换为字符串
    signed_xml = etree.tostring(signed_xml_doc, encoding='utf-8', xml_declaration=False, pretty_print=True)
    print("Signed XML with SHA256withRSA:")
    print(signed_xml.decode('utf-8'))

    return remove_keyinfo(signed_xml_doc)

def verify_xml(public_cert, signed_xml):
    signed_xml_doc = etree.fromstring(signed_xml.encode('utf-8'), parser=etree.XMLParser(encoding='utf-8'))
    print(signed_xml_doc)

    # 验证签名
    def get_verifier():
        return endesive.xml.signedsig.Signature(
            x509cert=public_cert,
            hashalg='sha256',
            method='enveloped'
        )

    verified_data = endesive.xml.verify(signed_xml_doc, get_verifier())
    print(verified_data)

    print("Verified XML with SHA256withRSA:")
    print(etree.tostring(verified_data, encoding='utf-8', pretty_print=True).decode('utf-8'))

    return verified_data

def remove_keyinfo(signed_xml_doc):
    # 手动移除 <ds:KeyInfo> 元素
    for key_info in signed_xml_doc.findall(".//{http://www.w3.org/2000/09/xmldsig#}KeyInfo"):
        key_info.getparent().remove(key_info)

    # 将签名后的 XML 转换为字符串
    signed_xml = etree.tostring(signed_xml_doc, encoding='utf-8', xml_declaration=False)

    print("Signed XML with SHA256withRSA (without KeyInfo):")
    print(signed_xml.decode('utf-8'))
    return signed_xml_doc
