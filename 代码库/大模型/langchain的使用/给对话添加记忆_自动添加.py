from langchain_deepseek import ChatDeepSeek
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv
from langchain.chains import ConversationChain
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder

# 记载环境变量
load_dotenv()

model = ChatDeepSeek(model="deepseek-chat")

# 创建一个对话记忆
memory = ConversationBufferMemory(return_messages=True)

# 创建对话链,传入模型和记忆 
# chain = ConversationChain(llm=model, memory=memory)

# 使用对话链进行对话
# result = chain.invoke({"input", "你好，我的名字叫张三"})
# print(result["response"])

# chain.invoke({"input", "我是谁？"})["response"]

# 该对话链支持传入模板
# 注意：表示用户输入的变量名必须是input，表示历史输入的变量名必须是history

# 提前存入一些对话记录
memory.save_context(
    {"input" : "你好，我是李四"},
    {"output" : "你好，李四，我是你的助手。"}
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个脾气暴躁的助手，喜欢冷嘲热讽和用阴阳怪气的语气回答问题。"),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}")
    ]
)

chain = ConversationChain(llm=model, memory=memory, prompt=prompt)

print(chain.invoke({"input" : "今天天气怎么样？", "history" : memory.load_memory_variables({})["history"]}))
print(chain.invoke({"input" : "我的上一个问题是什么？", "history" : memory.load_memory_variables({})["history"]}))

