import base64
import datetime
import hashlib
import hmac
import json
import subprocess
import time
from dataclasses import dataclass

import requests
from flask import Flask, request, jsonify

# GitLab 项目设置的 Secret Token
SECRET_TOKEN = 'c755461021cd52dddf6f8384600b182194ae0a088687756'

# 钉钉群机器人的 Webhook URL
WEBHOOK_URL = "https://oapi.dingtalk.com/robot/send"
# 访问 token
ACCESS_TOKEN = "2bbdd023507b1ce91b37c275cb2d75f96e2f49b53d6155215e"
# 加签密钥
SECRET = "SEC03c4d1cb7abead6cbd325ec93a392af2e7861e90e332fda1203b"


@dataclass
class MessageContent:
    summary: str
    title: str
    repo: str
    branch: str
    user: str
    state: bool
    log: str
    commit: int

    def state_text(self):
        return "成功" if self.state else "失败"

    def published_at(self):
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def __str__(self):
        return f"""### {self.title}   
**仓库：** {self.repo}   
**分支：** {self.branch}   
**作者：** {self.user}   
**时间：** {self.published_at()}   
**状态：** {self.state_text()}   
**文件更改数量：** {self.commit}   
**更新命令日志：**
\n> {self.log}
"""


class DingTalkPush:
    def __init__(self, access_token, secret=None):
        self.access_token = access_token
        self.secret = secret

    def __build_message(self, title, content):
        return {
            "msgtype":"actionCard",
            "actionCard":{
                "title":title,
                "text":content,
                "hideAvatar":"0",
                "btnOrientation":"0"
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
        response = requests.post(signed_url, headers={"Content-Type":"application/json"}, data=json.dumps(message))
        return response.json()

    def send_for(self, message_content):
        return self.send(message_content.summary, str(message_content))


class WebhookHandler:

    def __init__(self, secret_token):
        self.secret_token = secret_token
        self.dingtalk_push = DingTalkPush(ACCESS_TOKEN, SECRET)

    def verify_signature(self, signature):
        mac = hmac.new(self.secret_token.encode(), digestmod=hashlib.sha256)
        calculated_signature = mac.hexdigest()

        if hmac.compare_digest(calculated_signature, signature):
            return True
        else:
            print(f"Calculated Signature: {calculated_signature}")
            print(f"Received Signature: {signature}")

    def handle_event(self, data, event_type):
        if event_type == 'push':
            self.__process_push_event(data)
        elif event_type == 'merge_request':
            self.__process_merge_request_event(data)
        else:
            print(f"Unknown event type: {event_type}")

    def __process_push_event(self, data):
        # 在这里实现你对推送事件的处理逻辑
        print("Received push event from GitLab")
        repo = data['repository']['name']
        branch = data['ref']
        user = data['user_name']
        commit = len(data['commits'])

        # print(f"Repository: {repo}")
        # print(f"Ref: {branch}")
        # print(f"Author: {user}")
        # print(f"Commits: {commit}")

        title, branch_name = self.__get_update_title(branch)
        # 执行 Shell 代码
        state, message = self.__execute_shell_command("./script/update.sh")

        message_content = MessageContent("宝乡通ERP服务更新", title, repo, branch_name, user, state, message, commit)
        self.dingtalk_push.send_for(message_content)

    def __process_merge_request_event(self, data):
        # 在这里实现你对合并请求事件的处理逻辑
        print("Received merge request event from GitLab")
        print(f"Action: {data['object_attributes']['action']}")
        print(f"Title: {data['object_attributes']['title']}")

        # 执行 Shell 代码
        # state, message = self.__execute_shell_command("./script/update.sh")

    def __execute_shell_command(self, script_path):
        try:
            # 使用 subprocess.run 来执行 Shell 脚本，并捕获输出和错误
            result = subprocess.run(['bash', script_path], capture_output=True, text=True, check=True)

            # 打印标准输出
            print("Command Output:")
            print(result.stdout)

            # 如果没有抛出异常，说明脚本成功执行
            print("Script completed successfully.")
            return True, result.stdout
        except subprocess.CalledProcessError as e:
            # 打印标准输出和标准错误
            print("Command Failed:")
            print("Standard Output:")
            print(e.stdout)

            print("Standard Error:")
            print(e.stderr)
            print(f"Exit Code: {e.returncode}")
            return False, e.stderr
        except FileNotFoundError as e:
            # 打印其他异常信息
            print("An error occurred:")
            print(e)
            return False, str(e)

    def __get_update_title(self, branch):
        branch_to_title = {
            'main':"生产环境更新",
            'test':"测试环境更新",
            'dev':"开发环境更新",
            'prod':"预生产环境更新"
        }

        for key, title in branch_to_title.items():
            if key in branch:
                return title, key

        return "未知环境更新"


app = Flask(__name__)
handler = WebhookHandler(SECRET_TOKEN)


@app.route('/webhook', methods=['POST'])
def webhook():
    print("Received webhook request from GitLab")

    # 获取请求头中的签名
    token_signature = request.headers.get('X-Gitlab-Token')
    if not token_signature:
        return jsonify({'error':'Missing X-Gitlab-Token header'}), 400

    # 验证签名
    if not handler.verify_signature(token_signature):
        print(flush=True)
        return jsonify({'error':'Invalid or no X-Gitlab-Token'}), 403

    # 解析 JSON 数据
    try:
        data = request.json
        # print(f"Request json: {request.json}")
    except Exception as e:
        return jsonify({'error':'Invalid JSON'}), 400

    # 检查事件类型
    event = request.headers.get('X-Gitlab-Event')
    if data['ref'] == 'refs/heads/main':
        return jsonify({'status': f'{data["ref"]}, ignore execution'}), 200

    if event == 'Push Hook':
        # 处理推送事件
        handler.handle_event(data, "push")
    elif event == 'Merge Request Hook':
        # 处理合并请求事件
        handler.handle_event(data, "merge_request")
    else:
        # 其他类型的事件可以在这里处理
        pass

    print(flush=True)
    return jsonify({'status':'success'}), 200


if __name__ == '__main__':
    app.run(debug=True, port=12521, host='0.0.0.0')
