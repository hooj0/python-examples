import requests
import hashlib
import hmac
import base64
import time
import json

# 钉钉群机器人的 Webhook URL
WEBHOOK_URL = "https://oapi.dingtalk.com/robot/send"
# 访问 token
ACCESS_TOKEN = "2bbdd023507b1ce91b377275cb2d75f96e2f49b53d6155215e"
# 加签密钥
SECRET = "SEC03c4d1cb7abead6cbd325ecb0af2e7861e90e332fda1203b"


class DingTalkPush:
    def __init__(self, access_token, secret=None):
        self.access_token = access_token
        self.secret = secret

    def __build_message(self, title, content):
        return {
            "msgtype": "actionCard",
            "actionCard": {
                "title": title,
                "text": content,
                "hideAvatar": "0",
                "btnOrientation": "0"
            }
        }

    def __sign_url(self):
        if not self.secret:
            return WEBHOOK_URL

        timestamp = str(round(time.time() * 1000))
        secret_enc = self.secret.encode('utf-8')
        string_to_sign = f'{timestamp}\n{self.secret}'
        string_to_sign_enc = string_to_sign.encode('utf-8')
        hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
        sign = base64.b64encode(hmac_code).decode('utf-8')

        # 钉钉群机器人的 Webhook URL
        return f"{WEBHOOK_URL}?access_token={self.access_token}&timestamp={timestamp}&sign={sign}"

    def send(self, title, content):
        message = self.__build_message(title, content)
        signed_url = self.__sign_url()
        response = requests.post(signed_url, headers={"Content-Type": "application/json"}, data=json.dumps(message))
        return response.json()


if __name__ == '__main__':

    dingtalk_push = DingTalkPush(ACCESS_TOKEN, SECRET)
    title2 = "ERP服务更新"
    content2 = """### 测试测试   
    **环境：** 测试环境   
    **系统：** ERP后端   
    **执行人：** xxx   
    **时间：** 2024-12-30 14:09   
    **状态：** 成功   
    **日志：**
    \n> Script completed successfully.
    > Script completed successfully.
    """

    result = dingtalk_push.send(title2, content2)
    print("Response:", result)
    print("Response:", result["errcode"])
