import base64

from cryptography.hazmat.primitives import serialization


def load_and_print_private_key(encode_private_key):
    try:
        # 移除可能存在的 PEM 标头和尾部
        encode_private_key = encode_private_key.replace("-----BEGIN PRIVATE KEY-----", "")
        encode_private_key = encode_private_key.replace("-----END PRIVATE KEY-----", "")
        encode_private_key = encode_private_key.replace(" ", "").replace("\n", "")

        # 解码 Base64 编码的私钥
        private_key_bytes = base64.b64decode(encode_private_key)

        # 尝试从 DER 或 PEM 编码的字节中加载私钥
        try:
            # 首先尝试作为 PKCS8 DER 编码的私钥加载
            private_key = serialization.load_der_private_key(
                private_key_bytes,
                password=None,  # 如果私钥是加密的，这里提供密码
            )
        except ValueError:
            # 如果失败，尝试作为 PKCS8 PEM 编码的私钥加载
            private_key = serialization.load_pem_private_key(
                private_key_bytes,
                password=None,  # 如果私钥是加密的，这里提供密码
            )

        # 将私钥序列化为 PEM 格式的字节串，不加密
        pem_private_key = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )

        # 将字节串转换为字符串
        pem_private_key_str = pem_private_key.decode('utf-8')

        # 打印私钥字符串
        print("Private Key (PEM format):\n", pem_private_key_str)
        return pem_private_key_str

    except base64.binascii.Error as e:
        print("Base64解码失败: 请确认输入的是有效的Base64编码字符串。\n", e)
    except ValueError as e:
        print("私钥加载失败: 可能私钥格式不正确或被加密了。\n", e)
    except Exception as e:
        print("发生未知错误:\n", e)


def load_and_print_public_key(encode_public_key):
    try:
        # 移除可能存在的 PEM 标头和尾部
        encode_public_key = encode_public_key.replace("-----BEGIN PUBLIC KEY-----", "")
        encode_public_key = encode_public_key.replace("-----END PUBLIC KEY-----", "")
        encode_public_key = encode_public_key.replace(" ", "").replace("\n", "")

        # 解码 Base64 编码的公钥
        public_key_bytes = base64.b64decode(encode_public_key)

        # 尝试从 DER 或 PEM 编码的字节中加载公钥
        try:
            # 首先尝试作为 X.509 SubjectPublicKeyInfo DER 编码的公钥加载
            public_key = serialization.load_der_public_key(
                public_key_bytes
            )
        except ValueError:
            # 如果失败，尝试作为 X.509 SubjectPublicKeyInfo PEM 编码的公钥加载
            public_key = serialization.load_pem_public_key(
                public_key_bytes
            )

        # 将公钥序列化为 PEM 格式的字节串
        pem_public_key = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

        # 将字节串转换为字符串
        pem_public_key_str = pem_public_key.decode('utf-8')

        # 打印公钥字符串
        print("Public Key (PEM format):\n", pem_public_key_str)
        return pem_public_key_str
    except base64.binascii.Error as e:
        print("Base64解码失败: 请确认输入的是有效的Base64编码字符串。\n", e)
    except ValueError as e:
        print("公钥加载失败: 可能公钥格式不正确。\n", e)
    except Exception as e:
        print("发生未知错误:\n", e)


if __name__ == '__main__':
    private_key = "MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC+DjjKuBYNScrhp7/+yf/vqsZbyWAMuvLZ76rv9wLA3XTCY1Cb3xxm7xvux/OzhzDlQdURRrEhjjsVdP9Bx0Ig5yfGyDec/4Z50dcRgqsu17QU/m2WXHEwFd4yBAGomWXzy/q7+8JJ9YoTraSDfKhfV3qWx7/vBzqk0QNzZ3AgFwSMiP5Azz8K2GhkHWxbVLlji9+/oRL5yj13a8P9bbtIrdUB/PZ+Fk3klxhBL9Vxii0YmX96nwVuJgkmgyiRCwmLhIQBFdL7H63cNgUi9UoCsFC6lV4ErEcHCUFsLqggukKPmTlr4KSnFvf9bZoIYC9I7XBWcM+KDGTSdxeGpXbvAgMBAAECggEABIJr4It7oncUxEPpr071rqcbq8PcbpDlADzKjoUK4K6gfZhDql8h2mNkA0dlReY4R8hHGPDXdRdd2YV8JQBoVkWF0RahEy2Q8EUFWFoEW8ksca8TxJSO7vgl3IPx0iFJpP47BcjUdFLKIutk0uXbTN/Tfc5hhHdkcdKvxUY4B9rZYSNI5+YdIGjJj/nBWNGBndIqKnLfs2AhpCqPkADC3xo73fxiM/77TPB7RiaFeK9jk80kLAwaZeOKArCIY7YSpnyhqvPi4kO9vxTeGGHONhN+mfAsMG94AY83vZ6qhUiZZuofslbUt7beOw2PTmzGi8jXDI8k6WVHKqNnwYt/+QKBgQD/fT8sG3oJyRpvfhc/gPM+ovYGL3MH+6B3Gtq32K+ZyAmtoHnfLFkaa1bOLUEklvr2xViFTU4NlUyEWNE1jGW1JFC9AhU3JUnVKmiG/BSURH8neYsNUQ/yKOmjRyTvQmELp2Qb7h46ZWM6kWOzrJtiXMvkoAjWwgO/4YOxEazJdQKBgQC+b3zZW/yh/cOTCAzfN8AR/luSq9TJ7D8CZxHVOpXRL3YP950SUWEfuyOby4ddhFDwU3b6+BhtOtClMrBKO2Q9wbPVjVD5plGlhhMaLiNJmbFL63hEazrMOE3UVbOY8EYBJyyeUguqiYyRJkUbiVubRsdbFLUbGai8qWg5BvTOUwKBgEFOUoeDvn4h2ZAGOwsQexzXquuJ1W2E9E99ncrAqKI2b8Lh8kUJoP0P0vCAwNYJgbzyVN4+FGWEdDqgOVnmuVjEH58wmRuvfF/wpydZ6Ci+GYKNnu2Yeur7aj1CQj6mSQghkYVSKIfkwqiF4WZcCJvr/HJENf4vOaYijvcD/ZbBAoGBAKoZFyFnIq7m5cvtAuJW/76SveSyiuyZkmZo/erB25PvmrsEZ043VlNrapD8KLsFNu6S/tGIzPiz8i28qu6DQjRPUnxLL6ruPjtlGKbn0ykomM7BUrl6Nhi3qf0hV7wh0cWx4g7AJh97oQz9a/j+pc56WBMo2eOM9cUeZDOb3Qp1AoGAQwB8ndcxkt4UCfC+87Rpy5yrxVuaVKDZfTIy4qpuLrHRqCIHvAl41EnJTE8MPIemXhdTmPeLmGWe7KjGDo0F0GPRqBMVKrLrCnM52FUx/Wp5P2h8ZVXvm7TR5/b3jhCb7qC0gjey+HunyEn78H9Vxty4XzcSlF0zu8uVUSgwIJ8="
    load_and_print_private_key(private_key)

    public_key = """
    MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvg44yrgWDUnK4ae//sn/
76rGW8lgDLry2e+q7/cCwN10wmNQm98cZu8b7sfzs4cw5UHVEUaxIY47FXT/QcdC
IOcnxsg3nP+GedHXEYKrLte0FP5tllxxMBXeMgQBqJll88v6u/vCSfWKE62kg3yo
X1d6lse/7wc6pNEDc2dwIBcEjIj+QM8/CthoZB1sW1S5Y4vfv6ES+co9d2vD/W27
SK3VAfz2fhZN5JcYQS/VcYotGJl/ep8FbiYJJoMokQsJi4SEARXS+x+t3DYFIvVK
ArBQupVeBKxHBwlBbC6oILpCj5k5a+Ckpxb3/W2aCGAvSO1wVnDPigxk0ncXhqV2
7wIDAQAB
    """
    load_and_print_public_key(public_key)

    public_key = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDOb4B1dnwONcW0RoJMa0IOq3O6jiqnTGLUpxEw2xJg+c7wsb6DBy5CAoR0w2ZjZ/BjKxGIQ+DoDg3NsHJeyuEjNF0/Ro/R5xVpFC5z4cBVSC2/gddz4a1EoGDJewML/Iv0yIw7ylB86++h23nRd079c5S9RZXurBfnLW2Srhqk2QIDAQAB"
    load_and_print_public_key(public_key)
