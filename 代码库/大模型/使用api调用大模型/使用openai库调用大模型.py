from openai import OpenAI

# 创建OpenAI对象
client = OpenAI(api_key="your_api_key", base_url="https://api.deepseek.com") 

#调用大模型
response = client.chat.completions.create(
    model = 'deepseek-chat',
    messages = [
        {"role" : "system", "content" : "You are a helpful assistant."},
        {"role" : "user", "content" : "Hello"},
    ],
    stream=False
)

print(response.choices[0].message.content)

