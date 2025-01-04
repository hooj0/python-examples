from unittest import TestCase

import signxml
from lxml import etree
from signxml import XMLSigner, XMLVerifier


class SignXmlTest(TestCase):

    def test_bank_sing_xml(self):
        # 原始 XML 数据
        data_to_sign = """
        <root>
            <element1>data</element1>
            <element2>more data</element2>
        </root>
        """

        with open("bank/private_key.pem", "r") as file:
            key = file.read()

        AlipaySignXml.sign_xml(key, data_to_sign)

    def test_bank_verify_xml(self):
        # 签名后的 XML 数据
        signed_xml = """
        <root>
          <element1>data</element1>
          <element2>more data</element2>
          <ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#">
            <ds:SignedInfo>
              <ds:CanonicalizationMethod Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315"/>
              <ds:SignatureMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256"/>
              <ds:Reference URI="">
                <ds:Transforms>
                  <ds:Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature"/>
                  <ds:Transform Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315"/>
                </ds:Transforms>
                <ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"/>
                <ds:DigestValue>cDsr3Xe7NNMftkBdeB4hRxU6uG+Yy+qmNHL9/r+RemI=</ds:DigestValue>
              </ds:Reference>
            </ds:SignedInfo>
            <ds:SignatureValue>FrVy5Lq+WAAUvS8BCT/TdLi9T1BJxprtPvK25s9Tw9x4Y6wF7NUx7irN+DKSwn86gP441qDV5TM5FWbZ64IkfORWgChJdu272wM8y+afTRq6AqQP6AYroCWtuWCHadNmen7oqN9eOBQDxLeTgiLhPDbTqGu5EpTTLQfJScweoNg2GsRHD6NRr4DCXYFliFuX+4M0W3u/k3ng0vrrnObDb4bkW7ndYd/yml3Cj4nmycvotsWTLjm8xkrpPXft69/s+HWxgkP4jSPUrj9Dw5+SjXsaH5/4uTD34or4ON0rpPfjFOwufD5EK5OVyuWzbL/g8mlqCE4sZ7rc8n0yoeJhxw==</ds:SignatureValue>
          </ds:Signature>
        </root>
        """

        with open("bank/public_cert.pem", "r") as file:
            key = file.read()

        AlipaySignXml.verify_xml(key, signed_xml)

    def test_bank_sing_xml_sk(self):
        # 原始 XML 数据
        data_to_sign = """
        <root>
            <element1>data</element1>
            <element2>more data</element2>
        </root>
        """

        request_sign_private_key = """
-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC+DjjKuBYNScrhp7/+yf/vqsZbyWAMuvLZ76rv9wLA3XTCY1Cb3xxm7xvux/OzhzDlQdURRrEhjjsVdP9Bx0Ig5yfGyDec/4Z50dcRgqsu17QU/m2WXHEwFd4yBAGomWXzy/q7+8JJ9YoTraSDfKhfV3qWx7/vBzqk0QNzZ3AgFwSMiP5Azz8K2GhkHWxbVLlji9+/oRL5yj13a8P9bbtIrdUB/PZ+Fk3klxhBL9Vxii0YmX96nwVuJgkmgyiRCwmLhIQBFdL7H63cNgUi9UoCsFC6lV4ErEcHCUFsLqggukKPmTlr4KSnFvf9bZoIYC9I7XBWcM+KDGTSdxeGpXbvAgMBAAECggEABIJr4It7oncUxEPpr071rqcbq8PcbpDlADzKjoUK4K6gfZhDql8h2mNkA0dlReY4R8hHGPDXdRdd2YV8JQBoVkWF0RahEy2Q8EUFWFoEW8ksca8TxJSO7vgl3IPx0iFJpP47BcjUdFLKIutk0uXbTN/Tfc5hhHdkcdKvxUY4B9rZYSNI5+YdIGjJj/nBWNGBndIqKnLfs2AhpCqPkADC3xo73fxiM/77TPB7RiaFeK9jk80kLAwaZeOKArCIY7YSpnyhqvPi4kO9vxTeGGHONhN+mfAsMG94AY83vZ6qhUiZZuofslbUt7beOw2PTmzGi8jXDI8k6WVHKqNnwYt/+QKBgQD/fT8sG3oJyRpvfhc/gPM+ovYGL3MH+6B3Gtq32K+ZyAmtoHnfLFkaa1bOLUEklvr2xViFTU4NlUyEWNE1jGW1JFC9AhU3JUnVKmiG/BSURH8neYsNUQ/yKOmjRyTvQmELp2Qb7h46ZWM6kWOzrJtiXMvkoAjWwgO/4YOxEazJdQKBgQC+b3zZW/yh/cOTCAzfN8AR/luSq9TJ7D8CZxHVOpXRL3YP950SUWEfuyOby4ddhFDwU3b6+BhtOtClMrBKO2Q9wbPVjVD5plGlhhMaLiNJmbFL63hEazrMOE3UVbOY8EYBJyyeUguqiYyRJkUbiVubRsdbFLUbGai8qWg5BvTOUwKBgEFOUoeDvn4h2ZAGOwsQexzXquuJ1W2E9E99ncrAqKI2b8Lh8kUJoP0P0vCAwNYJgbzyVN4+FGWEdDqgOVnmuVjEH58wmRuvfF/wpydZ6Ci+GYKNnu2Yeur7aj1CQj6mSQghkYVSKIfkwqiF4WZcCJvr/HJENf4vOaYijvcD/ZbBAoGBAKoZFyFnIq7m5cvtAuJW/76SveSyiuyZkmZo/erB25PvmrsEZ043VlNrapD8KLsFNu6S/tGIzPiz8i28qu6DQjRPUnxLL6ruPjtlGKbn0ykomM7BUrl6Nhi3qf0hV7wh0cWx4g7AJh97oQz9a/j+pc56WBMo2eOM9cUeZDOb3Qp1AoGAQwB8ndcxkt4UCfC+87Rpy5yrxVuaVKDZfTIy4qpuLrHRqCIHvAl41EnJTE8MPIemXhdTmPeLmGWe7KjGDo0F0GPRqBMVKrLrCnM52FUx/Wp5P2h8ZVXvm7TR5/b3jhCb7qC0gjey+HunyEn78H9Vxty4XzcSlF0zu8uVUSgwIJ8=
-----END PRIVATE KEY-----
"""

        AlipaySignXml.sign_xml(request_sign_private_key, data_to_sign)

    def test_bank_verify_xml_str(self):
        # 签名后的 XML 数据
        signed_xml = """
        <root>
          <element1>data</element1>
          <element2>more data</element2>
          <ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#">
            <ds:SignedInfo>
              <ds:CanonicalizationMethod Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315"/>
              <ds:SignatureMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256"/>
              <ds:Reference URI="">
                <ds:Transforms>
                  <ds:Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature"/>
                  <ds:Transform Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315"/>
                </ds:Transforms>
                <ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"/>
                <ds:DigestValue>cDsr3Xe7NNMftkBdeB4hRxU6uG+Yy+qmNHL9/r+RemI=</ds:DigestValue>
              </ds:Reference>
            </ds:SignedInfo>
            <ds:SignatureValue>FrVy5Lq+WAAUvS8BCT/TdLi9T1BJxprtPvK25s9Tw9x4Y6wF7NUx7irN+DKSwn86gP441qDV5TM5FWbZ64IkfORWgChJdu272wM8y+afTRq6AqQP6AYroCWtuWCHadNmen7oqN9eOBQDxLeTgiLhPDbTqGu5EpTTLQfJScweoNg2GsRHD6NRr4DCXYFliFuX+4M0W3u/k3ng0vrrnObDb4bkW7ndYd/yml3Cj4nmycvotsWTLjm8xkrpPXft69/s+HWxgkP4jSPUrj9Dw5+SjXsaH5/4uTD34or4ON0rpPfjFOwufD5EK5OVyuWzbL/g8mlqCE4sZ7rc8n0yoeJhxw==</ds:SignatureValue>
            <ds:KeyInfo>
              <ds:KeyValue>
                <ds:RSAKeyValue>
                  <ds:Modulus>vg44yrgWDUnK4ae//sn/76rGW8lgDLry2e+q7/cCwN10wmNQm98cZu8b7sfzs4cw5UHVEUaxIY47FXT/QcdCIOcnxsg3nP+GedHXEYKrLte0FP5tllxxMBXeMgQBqJll88v6u/vCSfWKE62kg3yoX1d6lse/7wc6pNEDc2dwIBcEjIj+QM8/CthoZB1sW1S5Y4vfv6ES+co9d2vD/W27SK3VAfz2fhZN5JcYQS/VcYotGJl/ep8FbiYJJoMokQsJi4SEARXS+x+t3DYFIvVKArBQupVeBKxHBwlBbC6oILpCj5k5a+Ckpxb3/W2aCGAvSO1wVnDPigxk0ncXhqV27w==</ds:Modulus>
                  <ds:Exponent>AQAB</ds:Exponent>
                </ds:RSAKeyValue>
              </ds:KeyValue>
            </ds:KeyInfo>
          </ds:Signature>
        </root>
        """

        response_verify_public_key = """-----BEGIN CERTIFICATE-----
MIIDazCCAlOgAwIBAgIUVwvieYRFavckKfGkgH7wSOew+ZAwDQYJKoZIhvcNAQEL
BQAwRTELMAkGA1UEBhMCQVUxEzARBgNVBAgMClNvbWUtU3RhdGUxITAfBgNVBAoM
GEludGVybmV0IFdpZGdpdHMgUHR5IEx0ZDAeFw0yNTAxMDQwMzE4NTRaFw0yNTAy
MDMwMzE4NTRaMEUxCzAJBgNVBAYTAkFVMRMwEQYDVQQIDApTb21lLVN0YXRlMSEw
HwYDVQQKDBhJbnRlcm5ldCBXaWRnaXRzIFB0eSBMdGQwggEiMA0GCSqGSIb3DQEB
AQUAA4IBDwAwggEKAoIBAQC+DjjKuBYNScrhp7/+yf/vqsZbyWAMuvLZ76rv9wLA
3XTCY1Cb3xxm7xvux/OzhzDlQdURRrEhjjsVdP9Bx0Ig5yfGyDec/4Z50dcRgqsu
17QU/m2WXHEwFd4yBAGomWXzy/q7+8JJ9YoTraSDfKhfV3qWx7/vBzqk0QNzZ3Ag
FwSMiP5Azz8K2GhkHWxbVLlji9+/oRL5yj13a8P9bbtIrdUB/PZ+Fk3klxhBL9Vx
ii0YmX96nwVuJgkmgyiRCwmLhIQBFdL7H63cNgUi9UoCsFC6lV4ErEcHCUFsLqgg
ukKPmTlr4KSnFvf9bZoIYC9I7XBWcM+KDGTSdxeGpXbvAgMBAAGjUzBRMB0GA1Ud
DgQWBBTA5MQsEWn2L8g/gHSjrJp2jZgJfTAfBgNVHSMEGDAWgBTA5MQsEWn2L8g/
gHSjrJp2jZgJfTAPBgNVHRMBAf8EBTADAQH/MA0GCSqGSIb3DQEBCwUAA4IBAQCZ
fvhApR6pqyDH0ey4FE6hQlaFBaGEDhZsnQ44WP2ygG96hOeBo2QlEjhrpMNs1moN
eT8FFfhirZ/hcBSjrRwGThuRUSTxEtOrF5A//CVpCE1PTeZGKCtJtfoBPHa68RDl
Vm0AcbngpLqyf3EfkCC7s8UGc8si7z2sj1bEbM/NCErATdbXZBv0maHNC5MDVozZ
8ZcH9qHzSzBFWupRnduFekncBnC8+w1Kq1cdUxAKvUtJA7sdfNdYEFFtVRSfRWmg
oDVr24u2/JcZI8ckgFcrFyxgL/deVCBjjvsYuFSCsAkO9BMqpVoLv2/tq+ljcKdc
F6MjwndXyBc/vcu9IueM
-----END CERTIFICATE-----"""

        AlipaySignXml.verify_xml(response_verify_public_key, signed_xml)

class AlipaySignXml:

    __encoding = "utf-8"

    @classmethod
    def sign_xml(cls, private_key, xml_text):
        # 解析 XML 数据
        xml_doc = cls.__to_xml(xml_text)
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
        signed_xml = cls.__to_string(signed_xml_doc)
        print("Signed XML with SHA256withRSA:")
        print(signed_xml)

        return cls.__remove_keyinfo(signed_xml_doc)

    @classmethod
    def verify_xml(cls, public_cert, signed_xml):
        signed_xml_doc = cls.__to_xml(signed_xml)
        print(signed_xml_doc)

        # 验证签名
        verified_data = XMLVerifier().verify(signed_xml_doc, x509_cert=public_cert).signed_xml
        print(verified_data)

        print("Verified XML with SHA256withRSA:")
        print(cls.__to_string(verified_data))

        return verified_data

    @classmethod
    def __to_string(cls, signed_xml_doc: etree.Element):
        return etree.tostring(signed_xml_doc, encoding=cls.__encoding, xml_declaration=False, pretty_print=True).decode(cls.__encoding)

    @classmethod
    def __to_xml(cls, signed_xml: str):
        return etree.fromstring(signed_xml.encode(cls.__encoding), parser=etree.XMLParser(encoding=cls.__encoding, remove_blank_text=True, remove_pis=True, remove_comments=True))

    @classmethod
    def __remove_keyinfo(cls, signed_xml_doc):
        # 手动移除 <ds:KeyInfo> 元素
        for key_info in signed_xml_doc.findall(".//{http://www.w3.org/2000/09/xmldsig#}KeyInfo"):
            key_info.getparent().remove(key_info)

        # 将签名后的 XML 转换为字符串
        signed_xml = AlipaySignXml.__to_string(signed_xml_doc)

        print("Signed XML with SHA256withRSA (without KeyInfo):")
        print(signed_xml)
        return signed_xml_doc