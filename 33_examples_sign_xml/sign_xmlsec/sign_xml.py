import xmlsec
from lxml import etree

__encoding = "utf-8"

# Load the private key used to sign the document.
private_key = xmlsec.Key.from_file('private_key.pem', xmlsec.constants.KeyDataFormatPem)

with open("unsigned.xml", 'rb') as file:
    xml_text = file.read()

print(xml_text)
# Wrap the root element into an ElementTree object.
root = etree.fromstring(xml_text, parser=etree.XMLParser(encoding=__encoding, remove_blank_text=True, remove_pis=True, remove_comments=True))
doc = etree.ElementTree(root)

# Sign the document
def sign_document(doc, key):
    # Create a signature template for RSA-SHA1 enveloped signature
    signature_node = xmlsec.template.create(
        doc,
        c14n_method=xmlsec.Transform.EXCL_C14N,
        sign_method=xmlsec.Transform.RSA_SHA1,
    )

    # Add the <ds:Signature/> node to the document:
    doc.getroot().append(signature_node)

    # Create a reference to the enveloped document:
    ref = xmlsec.template.add_reference(signature_node, xmlsec.Transform.SHA1)

    # Add an enveloped transform descriptor:
    xmlsec.template.add_transform(ref, xmlsec.Transform.ENVELOPED)

    # Add the <ds:KeyInfo/> and <ds:KeyName/> nodes:
    ki = xmlsec.template.ensure_key_info(signature_node)
    xmlsec.template.add_key_name(ki, "MyKey")

    # Create a digital signature context (no key manager is needed):
    ctx = xmlsec.SignatureContext()

    # Sign the template:
    ctx.key = key
    ctx.sign(signature_node)

    return doc


if __name__ == '__main__':
    signed_doc = sign_document(doc, private_key)
    signed_doc_xml = etree.tostring(signed_doc, encoding=__encoding, xml_declaration=False, pretty_print=True).decode(__encoding)
    print(signed_doc_xml)