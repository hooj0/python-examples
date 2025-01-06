import xmlsec
from lxml import etree

# Load the private key used to sign the document.
private_key = xmlsec.Key.from_file('private_key.pem', xmlsec.constants.KeyDataFormatPem)

# Create a new XML document to sign.
root = etree.Element('Example')
etree.SubElement(root, 'Content').text = 'This is some content.'

# Wrap the root element into an ElementTree object.
doc = etree.ElementTree(root)

# Create a signature template for RSA-SHA256 enveloped signature.
signature_node = xmlsec.template.create(
    doc,
    c14n_method=xmlsec.constants.TransformExclC14N,
    sign_method=xmlsec.constants.SignatureMethodRsaSha256
)

# Add the <ds:Signature/> node as the last child of the root element.
root.append(signature_node)

# Add the reference to the signed part of the document (the whole document in this case).
ref = xmlsec.template.add_reference(
    signature_node,
    digest_algorithm=xmlsec.constants.TransformSha256
)

# Add the enveloped transform to the reference.
xmlsec.template.add_transform(ref, xmlsec.constants.TransformEnveloped)

# Optionally, add a KeyInfo with an X509Certificate if you want to include it in the signature.
key_info = xmlsec.template.ensure_key_info(signature_node)
if public_cert_path := 'public_cert.pem':  # Only if you have a path to a public certificate file.
    x509_data = xmlsec.template.add_x509_data(key_info)
    cert = xmlsec.crypto.load_cert_from_file(public_cert_path, xmlsec.constants.KeyDataFormatCertPem)
    xmlsec.template.x509data_add_certificate(x509_data, cert)
    xmlsec.template.add_key_name(key_info).text = "MyKeyName"  # Optional

# Apply the signature using the private key.
context = xmlsec.SignatureContext()
context.key = private_key
try:
    context.sign(signature_node)
except Exception as e:
    print(f"Failed to sign the document: {e}")
    raise

# Convert the signed document to a string and save it to a file.
signed_xml_str = etree.tostring(doc, encoding='utf-8', pretty_print=True)
with open('signed.xml', 'wb') as f:
    f.write(signed_xml_str)

print("Document signed and saved to 'signed.xml'.")