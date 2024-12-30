import hashlib
import hmac
import subprocess

# GitLab 项目设置的 Secret Token
SECRET_TOKEN = 'c755461021cd52dddf6f8384600b1d78f1eaebc393ddad82194ae0a088687756'

class WebhookHandler:

    def __init__(self, secret_token):
        self.secret_token = secret_token

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
        print(f"Repository: {data['repository']['name']}")
        print(f"Ref: {data['ref']}")
        print(f"Author: {data['user_name']}")
        print(f"Commits: {len(data['commits'])}")

        # 执行 Shell 代码
        if data['ref'] == 'refs/heads/main':
            flag, message = self.__execute_shell_command("./script/update.sh")

            if not flag:
                self.__send_message(message)


    def __process_merge_request_event(self, data):
        # 在这里实现你对合并请求事件的处理逻辑
        print("Received merge request event from GitLab")
        print(f"Action: {data['object_attributes']['action']}")
        print(f"Title: {data['object_attributes']['title']}")

        # 执行 Shell 代码
        self.__execute_shell_command("./script/update.sh")


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


    def __send_message(self, message):
        # 在这里实现对消息的推送逻辑
        print(f"Sending message: {message}")

if __name__ == '__main__':
    handler = WebhookHandler(SECRET_TOKEN)
    print(handler.verify_signature('0d33b8ec495bcbd7165f281809ee525b243bc66229f4eebcdc13e127e59c1cea'))
    # print(handler.__execute_shell_command("./script/update.sh"))
