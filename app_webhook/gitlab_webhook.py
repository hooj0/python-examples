import datetime
import hashlib
import hmac
import subprocess

from app_webhook.dingtalk_push import DingTalkPush, ACCESS_TOKEN, SECRET
from app_webhook.model import MessageContent

# GitLab 项目设置的 Secret Token
SECRET_TOKEN = 'c755461021cd52dddf6f8384600b1d78f1eaebc393ddad82194ae0a088687756'


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

        print(f"Repository: {repo}")
        print(f"Ref: {branch}")
        print(f"Author: {user}")
        print(f"Commits: {commit}")

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
            'main': "生产环境更新",
            'test': "测试环境更新",
            'dev': "开发环境更新",
            'prod': "预生产环境更新"
        }

        for key, title in branch_to_title.items():
            if key in branch:
                return title, key

        return "未知环境更新"


if __name__ == '__main__':
    handler = WebhookHandler(SECRET_TOKEN)
    print(handler.verify_signature('0d33b8ec495bcbd7165f281809ee525b243bc66229f4eebcdc13e127e59c1cea'))
    # print(handler.__execute_shell_command("./script/update.sh"))
    handler.handle_event({
        'repository':{
            'name':'test-repo'
        },
        'ref':'refs/heads/test',
        'user_name':'John Doe',
        'commits':[
            {'id':'1234567890abcdef1234567890abcdef12345678'},
            {'id':'0987654321fedcba0987654321fedcba09876543'}
        ]
    }, 'push')
