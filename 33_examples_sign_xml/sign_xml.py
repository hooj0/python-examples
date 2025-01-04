from unittest import TestCase

import signxml
from lxml import etree
from signxml import XMLSigner, XMLVerifier


class SignXmlTest(TestCase):

    def test_sign_xml(self):
        sign_xml("gen/public_cert.pem", "gen/private_key.pem")

    def test_bank_sing_xml(self):
        sign_xml("bank/public_cert.pem", "bank/private_key.pem")

def sign_xml(public_cert, private_key):

    with open(public_cert, "r") as file:
        cert = file.read()

    with open(private_key, "r") as file:
        key = file.read()

    # 原始 XML 数据
    data_to_sign = """
    <root>
        <element1>data</element1>
        <element2>more data</element2>
    </root>
    """

    try:
        # 解析 XML 数据
        root = etree.fromstring(data_to_sign.encode('utf-8'), parser=etree.XMLParser(encoding='utf-8'))
        print(root)

        # 使用 sha256WithRSA 对 XML 进行签名
        signed_root = XMLSigner(
            method=signxml.algorithms.SignatureConstructionMethod.enveloped,
            signature_algorithm=signxml.algorithms.SignatureMethod.RSA_SHA256,  # 指定使用 sha256WithRSA 算法
            digest_algorithm=signxml.algorithms.DigestAlgorithm.SHA256,
            c14n_algorithm=signxml.algorithms.CanonicalizationMethod.CANONICAL_XML_1_0,
        ).sign(root, key=key)

        # 将签名后的 XML 转换为字符串
        signed_xml = etree.tostring(signed_root, encoding='utf-8', xml_declaration=False, pretty_print=True)

        print("Signed XML with SHA256withRSA:")
        print(signed_xml.decode('utf-8'))

        # 验证签名
        verified_data = XMLVerifier().verify(signed_root, x509_cert=cert).signed_xml

        print("Verified XML with SHA256withRSA:")
        print(etree.tostring(verified_data, encoding='utf-8', pretty_print=True).decode('utf-8'))

    except Exception as e:
        raise e
