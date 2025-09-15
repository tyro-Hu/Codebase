from langchain.memory import ConversationBufferMemory
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 创建一个对话缓冲区内存对象,用来储存历史对话记录
# return_messages=True表示返回列表形式的消息对象，反之，返回字符串拼接的对话
memory = ConversationBufferMemory(return_messages=True)

# 手动添加对话记录,save_context传入两个字典，一个是用户输入input，一个是模型输出output
memory.save_context(
    {"input" : "我的名字叫张三"},
    {"output" : "你好，张三，很高兴认识你"}
)

# 查看记忆中存储的对话内容,load_memory_variables传入空字典
print(memory.load_memory_variables({}))

# 创建好记忆后，提示模板里需要留出一块地方给历史消息
prompt = ChatPromptTemplate.from_messages(
    [
        ("system" , "你是一个乐于助人的助手"),
        # 消息列表模板，正好占位历史消息, history是memory字典中的key
        MessagesPlaceholder(variable_name="history"),
        ("human" , "{user_input}")
    ]
)

model = ChatDeepSeek(model="deepseek-chat")

chain = prompt | model

user_input = "你知道我的名字吗？"
history = memory.load_memory_variables({})["history"]

response = chain.invoke(
    {
    "history" : history, 
    "user_input" : user_input
    }
)
print(response.content)

# 将新一轮的对话储存在记忆中
memory.save_context(
    {"input" : user_input},
    {"output": response.content}
)

# 查看记忆中存储的对话内容
print(memory.load_memory_variables({}))