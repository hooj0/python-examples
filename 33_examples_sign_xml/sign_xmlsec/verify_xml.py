import xmlsec
from lxml import etree

# Load the public key used to verify the signature.
public_key = xmlsec.Key.from_file('public_cert.pem', xmlsec.constants.KeyDataFormatCertPem)

# Load the signed XML document from a file.
with open('signed.xml', 'rb') as f:
    signed_doc = etree.parse(f)

# Find the <ds:Signature/> node.
signature_node = xmlsec.tree.find_node(signed_doc.getroot(), xmlsec.constants.NodeSignature)

# Create a context for verifying the signature.
context = xmlsec.SignatureContext()
context.key = public_key

# Verify the signature.
try:
    if context.verify(signature_node):
        print("The signature is valid.")
    else:
        print("The signature is invalid.")
except Exception as e:
    print(f"Verification failed: {e}")