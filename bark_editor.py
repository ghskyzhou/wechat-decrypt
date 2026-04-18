from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)
CONFIG_FILE = 'bark_config.json'
PORT = 1145

# 如果配置文件不存在，初始化一个默认的
def init_config():
    if not os.path.exists(CONFIG_FILE):
        default_data = {"keywords": [], "whitelist": [], "blacklist": []}
        with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
            json.dump(default_data, f, indent=4, ensure_ascii=False)

init_config()

# 路由：访问首页，返回前端页面
@app.route('/')
def index():
    return render_template('index.html')

# 接口：获取当前配置
@app.route('/api/config', methods=['GET'])
def get_config():
    with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return jsonify(data)

# 接口：保存/覆盖配置
@app.route('/api/config', methods=['POST'])
def save_config():
    new_data = request.json
    with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
        # ensure_ascii=False 保证存进去的中文不是 unicode 乱码
        json.dump(new_data, f, indent=4, ensure_ascii=False)
    return jsonify({"status": "success", "message": "保存成功！"})

if __name__ == '__main__':
    # 启动服务
    print(f"后台已启动，请在浏览器访问: http://127.0.0.1:{PORT}")
    app.run(host='0.0.0.0', port=PORT)