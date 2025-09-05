from langchain.schema.messages import SystemMessage, HumanMessage
from dotenv import load_dotenv
import os
from langchain_deepseek import ChatDeepSeek

# 加载环境变量
load_dotenv()

# # 获取环境变量中的API密钥
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")

# 创建ChatDeepSeek对象
model = ChatDeepSeek(model="deepseek-chat")

#  创建系统消息
system_message = SystemMessage(content="你是一个智能助手，请根据用户的问题提供答案。")

# 创建用户消息
user_message = HumanMessage(content="你好")

messages = [system_message, user_message]

# 调用模型生成回复
response = model.invoke(messages)

print(response.content)