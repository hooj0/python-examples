import base64
from unittest import TestCase

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend


class FormatCertTest(TestCase):

    def test_format_cert_pem(self):
        # 生成一个新的 RSA 密钥对
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        print("[private_key]", private_key)

        public_key = private_key.public_key()
        print("[public_key]", public_key)

        # 将私钥序列化为 PEM 格式
        pem_private_key = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )
        print("[pem_private_key]", pem_private_key)
        print(pem_private_key.decode())

        # 将公钥序列化为 PEM 格式
        pem_public_key = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        print("[pem_public_key]", pem_public_key)
        print(pem_public_key.decode())

    def test_format_cert_text(self):
        key = self.format_private_key("MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC+DjjKuBYNScrhp7/+yf/vqsZbyWAMuvLZ76rv9wLA3XTCY1Cb3xxm7xvux/OzhzDlQdURRrEhjjsVdP9Bx0Ig5yfGyDec/4Z50dcRgqsu17QU/m2WXHEwFd4yBAGomWXzy/q7+8JJ9YoTraSDfKhfV3qWx7/vBzqk0QNzZ3AgFwSMiP5Azz8K2GhkHWxbVLlji9+/oRL5yj13a8P9bbtIrdUB/PZ+Fk3klxhBL9Vxii0YmX96nwVuJgkmgyiRCwmLhIQBFdL7H63cNgUi9UoCsFC6lV4ErEcHCUFsLqggukKPmTlr4KSnFvf9bZoIYC9I7XBWcM+KDGTSdxeGpXbvAgMBAAECggEABIJr4It7oncUxEPpr071rqcbq8PcbpDlADzKjoUK4K6gfZhDql8h2mNkA0dlReY4R8hHGPDXdRdd2YV8JQBoVkWF0RahEy2Q8EUFWFoEW8ksca8TxJSO7vgl3IPx0iFJpP47BcjUdFLKIutk0uXbTN/Tfc5hhHdkcdKvxUY4B9rZYSNI5+YdIGjJj/nBWNGBndIqKnLfs2AhpCqPkADC3xo73fxiM/77TPB7RiaFeK9jk80kLAwaZeOKArCIY7YSpnyhqvPi4kO9vxTeGGHONhN+mfAsMG94AY83vZ6qhUiZZuofslbUt7beOw2PTmzGi8jXDI8k6WVHKqNnwYt/+QKBgQD/fT8sG3oJyRpvfhc/gPM+ovYGL3MH+6B3Gtq32K+ZyAmtoHnfLFkaa1bOLUEklvr2xViFTU4NlUyEWNE1jGW1JFC9AhU3JUnVKmiG/BSURH8neYsNUQ/yKOmjRyTvQmELp2Qb7h46ZWM6kWOzrJtiXMvkoAjWwgO/4YOxEazJdQKBgQC+b3zZW/yh/cOTCAzfN8AR/luSq9TJ7D8CZxHVOpXRL3YP950SUWEfuyOby4ddhFDwU3b6+BhtOtClMrBKO2Q9wbPVjVD5plGlhhMaLiNJmbFL63hEazrMOE3UVbOY8EYBJyyeUguqiYyRJkUbiVubRsdbFLUbGai8qWg5BvTOUwKBgEFOUoeDvn4h2ZAGOwsQexzXquuJ1W2E9E99ncrAqKI2b8Lh8kUJoP0P0vCAwNYJgbzyVN4+FGWEdDqgOVnmuVjEH58wmRuvfF/wpydZ6Ci+GYKNnu2Yeur7aj1CQj6mSQghkYVSKIfkwqiF4WZcCJvr/HJENf4vOaYijvcD/ZbBAoGBAKoZFyFnIq7m5cvtAuJW/76SveSyiuyZkmZo/erB25PvmrsEZ043VlNrapD8KLsFNu6S/tGIzPiz8i28qu6DQjRPUnxLL6ruPjtlGKbn0ykomM7BUrl6Nhi3qf0hV7wh0cWx4g7AJh97oQz9a/j+pc56WBMo2eOM9cUeZDOb3Qp1AoGAQwB8ndcxkt4UCfC+87Rpy5yrxVuaVKDZfTIy4qpuLrHRqCIHvAl41EnJTE8MPIemXhdTmPeLmGWe7KjGDo0F0GPRqBMVKrLrCnM52FUx/Wp5P2h8ZVXvm7TR5/b3jhCb7qC0gjey+HunyEn78H9Vxty4XzcSlF0zu8uVUSgwIJ8=")
        print(key)

    @staticmethod
    def format_private_key(private_key_str):
        # 去除所有空格和换行符
        private_key_clean = ''.join(private_key_str.split())

        try:
            # 尝试直接加载未格式化的私钥
            private_key = serialization.load_pem_private_key(
                private_key_clean.encode(),
                password=None,
                # 如果私钥被加密，可以在这里提供密码
            )
        except ValueError:
            # 如果上述方法失败，尝试去掉头尾并解码base64
            if private_key_clean.startswith('LS0t'):
                private_key_clean = private_key_clean[26:]  # Remove '-----BEGIN PRIVATE KEY-----'
                private_key_clean = private_key_clean[:-26]  # Remove '-----END PRIVATE KEY-----'

            private_key_bytes = base64.b64decode(private_key_clean + '=' * (-len(private_key_clean) % 4))

            private_key = serialization.load_der_private_key(
                private_key_bytes,
                password=None,
            )

        # 重新序列化私钥为PEM格式
        pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )

        return pem.decode()

