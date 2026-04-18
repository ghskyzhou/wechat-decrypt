# WeChat Dycrypt & Message Bark

本项目所有内容基于 [wechat-decrypt](https://github.com/L1en2407/wechat-decrypt)，拓展制作 Bark 相关功能仅为了个人实行 Information Reduction，无其他目的。

**在使用本项目之前，请先详细阅读原项目的 `README.md`！**

微信 4.0 (Windows、MacOS、Linux) 本地数据库解密工具。从运行中的微信进程内存提取加密密钥，解密所有 SQLCipher 4 加密数据库，并提供实时消息监听。

## 更新日志

2026.4.18 写了关键词、白名单、黑名单功能

2026.4.17 第一次成功 Bark

## 使用方法

### 环境要求

- Python 3.10+
- 微信 4.x

Windows：

- Windows 10/11
- 微信正在运行
- 需要管理员权限（读取进程内存）

Linux：

- 64-bit Linux
- 需要 root 权限或 `CAP_SYS_PTRACE`（读取 `/proc/<pid>/mem`）
- `db_dir` 默认类似 `~/Documents/xwechat_files/<wxid>/db_storage`

### 安装依赖

```bash
pip install pycryptodome zstandard requests flask
```

### 快速开始

先创建一个 `config.json`，可以复制 `config.example.json` 来改。格式如下：
```json
{
    "db_dir": "C:\\xwechat_files\\your_wxid\\db_storage",
    "keys_file": "all_keys.json",
    "decrypted_dir": "decrypted",
    "wechat_process": "Weixin.exe",
    "bark_api_key": "your_bark_api_key"
}
```

这里这个 `db_dir` 原则上会自动获取，但也会出现获取不到的情况需要手动填入。

> 关于这个 Bark API Key 的获取，方法放在了最下面

先使用

```bash
python main.py decrypt
```

来解密所有数据库，然后再使用

```bash
python main.py
```

来启动程序。

## 功能

### Bark 规则编辑器

如下图，网址是 `http://localhost:1145/`，原则上启动主程序之后会自己打开。

**切记每次编辑完要点击右上角保存！**

<p align="center">
    <img src="https://img.skyzhou.top/i/2026/04/18/69e30eea11d15.png" height="500px">
</p >


### `unread == 0` 不推送

意思就是如果用户正在使用手机微信给别人发消息，或者正在看别人的消息，这种时候消息的 `unread` 标签的值为 `0`，不需要推送，此优先级最高。

### 关键词 Bark

可以在一个地方填入一些关键词，然后如果所有收到的微信消息**包含关键词**（包括私聊和群聊），推送该消息。

### 白名单

白名单，所有白名单用户发送的消息**会**推送，无论是否包含关键词。

### 黑名单

黑名单，所有黑名单用户发送的消息将**不会**推送，无论是否包含关键词，优先级仅次于 `unread == 0`。

> 注意：这里的所有白名单和黑名单，使用的是你给他/她的**微信备注名**。

## Bark API Key

### iOS 用户

App Store 找到 `Bark` 这个软件，下载之后点开首页如下（记得允许消息通知），红色框起来的打码部分即为你的 Bark API Key，将其复制到 `config.json` 里面的 `bark_api_key` 即可。

<p align="center">
    <img src="https://img.skyzhou.top/i/2026/04/17/69e235d31c5f9.png" height="500px">
</p >

### Android 用户

安卓的有些应用市场疑似有类似的软件，但因为本人没有安卓移动设备，无法调试，所以请自行查找类似软件的 API Key，可能还需要修改源码，非常抱歉！

## 免责声明

本工具仅用于学习和研究目的，用于解密**自己的**微信数据。请遵守相关法律法规，不要用于未经授权的数据访问。
