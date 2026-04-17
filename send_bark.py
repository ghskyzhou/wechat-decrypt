"""
用于发送内容给手机应用 Bark
"""

import json
import requests
import urllib.parse

from config import load_config
cfg = load_config()

BARK_API_KEY = cfg["bark_api_key"]

def send_to_bark(msg):
    # print(msg)
    if not BARK_API_KEY:
        return "未配置 BARK_API_KEY, 无法发送"
    
    content = msg.get('content', '')
    chat_title = msg.get('chat', '微信消息')

    if "sky" in content.lower():  # .lower() 可以同时匹配 sky 和 Sky
        # 对内容进行 URL 编码，防止中文或空格导致请求失败
        safe_title = urllib.parse.quote(chat_title)
        safe_content = urllib.parse.quote(content)
        
        api_url = f"https://api.day.app/{BARK_API_KEY}/{safe_title}/{safe_content}"
        
        try:
            # 发送 HTTP GET 请求
            response = requests.get(api_url)
            # 检查是否请求成功
            if response.status_code == 200:
                return "Bark 推送成功"
            else:
                return f"Bark 推送失败，状态码: {response.status_code}"
                # print(f"Bark 推送失败，状态码: {response.status_code}")
        except Exception as e:
            return f"发送请求时出现异常: {e}"
            # print(f"发送请求时出现异常: {e}")
        