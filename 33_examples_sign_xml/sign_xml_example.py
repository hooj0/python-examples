from lxml import etree
from signxml import XMLSigner, XMLVerifier
import signxml
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

# 生成一个新的 RSA 密钥对
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)
public_key = private_key.public_key()

# 将私钥序列化为 PEM 格式
pem_private_key = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
)

# 将公钥序列化为 PEM 格式
pem_public_key = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

cert = open("public_cert.pem").read()
key = open("private_key.pem").read()

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
        digest_algorithm=signxml.algorithms.DigestAlgorithm.SHA256
    ).sign(root, key=key)

    # 将签名后的 XML 转换为字符串
    signed_xml = etree.tostring(signed_root, encoding='utf-8', xml_declaration=True)

    print("Signed XML with SHA256withRSA:")
    print(signed_xml.decode('utf-8'))

    # 验证签名
    verified_data = XMLVerifier().verify(signed_root, x509_cert=cert).signed_xml

    print("Verified XML with SHA256withRSA:")
    print(etree.tostring(verified_data, encoding='utf-8', pretty_print=True).decode('utf-8'))

except Exception as e:
    raise e