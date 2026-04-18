"""
用于发送内容给手机应用 Bark
"""

import json
import requests
import urllib.parse

from config import load_config
cfg = load_config()

BARK_API_KEY = cfg["bark_api_key"]

def load_bark_config():
    """bark_config.json"""
    try:
        with open("bark_config.json", "r", encoding="utf-8") as f:
            config = json.load(f)
            return config
    except FileNotFoundError:
        print("错误：找不到 config.json 文件")
        return ""
    except Exception as e:
        print(f"读取配置出错: {e}")
        return ""

def send_to_bark(chat_title, content):
    safe_title = urllib.parse.quote(chat_title)
    safe_content = urllib.parse.quote(content)
    
    api_url = f"https://api.day.app/{BARK_API_KEY}/{safe_title}/{safe_content}"
    
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            return "Bark 推送成功"
        else:
            return f"Bark 推送失败，状态码: {response.status_code}"
            # print(f"Bark 推送失败，状态码: {response.status_code}")
    except Exception as e:
        return f"发送请求时出现异常: {e}"
        # print(f"发送请求时出现异常: {e}")

def check_bark(msg):
    # print(msg)
    if not BARK_API_KEY:
        return "未配置 BARK_API_KEY, 无法发送"
    
    content = msg.get('content', '')
    chat_title = msg.get('chat', '微信消息')
    sender = msg.get('chat')
    print("SENDER: ", sender)

    bark_cfg = load_bark_config()
    
    for blacklist_sender in bark_cfg["blacklist"]:
        if blacklist_sender == sender:
            return "黑名单用户！"
    
    for keyword in bark_cfg["keywords"]:
        if keyword in content.lower():
            return send_to_bark(chat_title, content)
    
    for whitelist_sender in bark_cfg["whitelist"]:
        if whitelist_sender == sender:
            return send_to_bark(chat_title, content)