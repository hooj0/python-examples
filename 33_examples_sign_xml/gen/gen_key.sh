# 生成私钥
openssl genpkey -algorithm RSA -out private_key.pem -pkeyopt rsa_keygen_bits:2048

# 生成自签名证书
openssl req -x509 -new -nodes -key private_key.pem -sha256 -days 365 -out public_cert.pem

# 检查私钥
#openssl rsa -in private_key.pem -check -noout
# 检查证书
#openssl x509 -in public_cert.pem -text -noout


# 生成公钥
# openssl rsa -in private_key.pem -pubout -out public_key.pem
# 检查公钥
# openssl rsa -pubin -in public_key.pem -text
# 公钥转换证书
# openssl req -new -key private_key.pem -out server.csr
# openssl x509 -req -days 365 -in server.csr -signkey private_key.pem -out server.crt
# openssl x509 -noout -text -in server.crt
# 和上面效果类似，生成自签名证书
# openssl req -x509 -new -nodes -key private_key.pem -sha256 -out public_cert.pem

# 检查私钥类型
# openssl pkey -in private_key.pem -text
# 检查公钥类型
# openssl pkey -pubin -in public_key.pem -text

# 查看密钥类型
#openssl asn1parse -in public_key.pem
#openssl asn1parse -in private_key.pem
# 查看私钥类型
#openssl rsa -in private_key.pem -check || openssl dsa -in private_key.pem -check || openssl ec -in private_key.pem -check
# 查看公钥类型
#openssl rsa -pubin -in private_key.pem -text || openssl dsa -pubin -in private_key.pem -text || openssl ec -pubin -in private_key.pem -text