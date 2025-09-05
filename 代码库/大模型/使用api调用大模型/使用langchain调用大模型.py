import getpass
import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

"""
下面演示几种填写api密钥的方法：
"""
#1. 手动设置 DeepSeek API 密。

# 1.1将密钥直接写入代码，存入python的环境变量中
# os.environ["DEEPSEEK_API_KEY"] = "sk-e24ba93f8f204f34a2ade604b8ebecf0"

#1.2 使用getpass库，在运行时输入密钥
# if not os.environ.get("DEEPSEEK_API_KEY"):
#     os.environ["DEEPSEEK_API_KEY"] = getpass.getpass("Enter your API key: ")

#3. 使用.env配置文件
# 3.1 加载.env文件中的环境变量，存入python的环境变量中
load_dotenv()   # 默认读取当前目录下的.env文件，也可指定路径

# 3.2 检查是否成功加载API密钥
if not os.environ.get("DEEPSEEK_API_KEY"):
    raise ValueError("API密钥未设置")


model = init_chat_model("deepseek-chat", model_provider="deepseek")

response = model.invoke("Hello, world!")

print(response.content)