# 生成私钥
openssl genpkey -algorithm RSA -out private_key.pem -pkeyopt rsa_keygen_bits:2048

# 生成自签名证书
openssl req -x509 -new -nodes -key private_key.pem -sha256 -days 365 -out public_cert.pem