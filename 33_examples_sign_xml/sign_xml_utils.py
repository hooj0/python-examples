import signxml
from lxml import etree
from signxml import XMLSigner, XMLVerifier


class SignXmlUtils:

    __encoding = "utf-8"

    @classmethod
    def sign_xml(cls, private_key, xml_text):
        # 解析 XML 数据
        xml_doc = cls.to_xml(xml_text)
        print(xml_doc)

        # 使用 sha256WithRSA 对 XML 进行签名
        signed_xml_doc = XMLSigner(
            method=signxml.algorithms.SignatureConstructionMethod.enveloped,
            signature_algorithm=signxml.algorithms.SignatureMethod.RSA_SHA256,  # 指定使用 sha256WithRSA 算法
            digest_algorithm=signxml.algorithms.DigestAlgorithm.SHA256,
            c14n_algorithm=signxml.algorithms.CanonicalizationMethod.CANONICAL_XML_1_0,
        ).sign(xml_doc, key=private_key)
        print(xml_doc)

        # 将签名后的 XML 转换为字符串
        signed_xml = cls.to_string(signed_xml_doc)
        print("Signed XML with SHA256withRSA:")
        print(signed_xml)

        return cls.__remove_keyinfo(signed_xml_doc)

    @classmethod
    def verify_xml(cls, public_cert, signed_xml):
        signed_xml_doc = cls.to_xml(signed_xml)
        print(signed_xml_doc)

        # 验证签名
        verified_data = XMLVerifier().verify(signed_xml_doc, x509_cert=public_cert).signed_xml
        print(verified_data)

        print("Verified XML with SHA256withRSA:")
        print(cls.to_string(verified_data))

        return verified_data

    @classmethod
    def to_string(cls, signed_xml_doc: etree.Element):
        return etree.tostring(signed_xml_doc, encoding=cls.__encoding, xml_declaration=False, pretty_print=True).decode(cls.__encoding)

    @classmethod
    def to_xml(cls, signed_xml: str):
        return etree.fromstring(signed_xml.encode(cls.__encoding), parser=etree.XMLParser(encoding=cls.__encoding, remove_blank_text=True, remove_pis=True, remove_comments=True))

    @classmethod
    def __remove_keyinfo(cls, signed_xml_doc):
        # 手动移除 <ds:KeyInfo> 元素
        for key_info in signed_xml_doc.findall(".//{http://www.w3.org/2000/09/xmldsig#}KeyInfo"):
            key_info.getparent().remove(key_info)

        # 将签名后的 XML 转换为字符串
        signed_xml = SignXmlUtils.to_string(signed_xml_doc)

        print("Signed XML with SHA256withRSA (without KeyInfo):")
        print(signed_xml)
        return signed_xml_doc