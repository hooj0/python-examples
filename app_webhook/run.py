from flask import Flask, request, jsonify

from app_webhook.gitlab_webhook import WebhookHandler, SECRET_TOKEN

app = Flask(__name__)
handler = WebhookHandler(SECRET_TOKEN)


@app.route('/webhook', methods=['POST'])
def webhook():
    print("Received webhook request from GitLab")

    # 获取请求头中的签名
    token_signature = request.headers.get('X-Gitlab-Token')
    if not token_signature:
        return jsonify({'error': 'Missing X-Gitlab-Token header'}), 400

    # 验证签名
    if not handler.verify_signature(token_signature):
        print(flush=True)
        return jsonify({'error': 'Invalid or no X-Gitlab-Token'}), 403

    # 解析 JSON 数据
    try:
        data = request.json
        print(f"Request json: {request.json}")
    except Exception as e:
        return jsonify({'error': 'Invalid JSON'}), 400

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
    return jsonify({'status': 'success'}), 200


if __name__ == '__main__':
    app.run(debug=True, port=12521, host='0.0.0.0')
