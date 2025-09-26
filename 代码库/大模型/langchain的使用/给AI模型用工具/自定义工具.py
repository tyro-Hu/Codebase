from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
from langchain.tools import BaseTool
from langchain import hub
from langchain.agents import create_structured_chat_agent, AgentExecutor
from langchain.memory import ConversationBufferMemory

load_dotenv()

class TextLengthTool(BaseTool):
    # 定义类变量，类变量是所有实例共享的变量。定义类变量，必须加上类型注解
    #BaseTool 继承自 pydantic.BaseModel，它内部把字段当作 模型字段 来管理。
    #在 Pydantic v2 里，如果你覆盖了父类的字段，就必须明确声明类型，否则 Pydantic 无法区分 “普通类变量” 和 “模型字段”。
    name : str = "文本字数计算工具"
    description : str = "当你被要求计算文本的字数时，使用此工具"

    # 如果需要调用工具，_run方法会被调用
    def _run(self, text: str): 
        return len(text) 
    
# tolls是一个列表，里面可以放多个工具
tools = [TextLengthTool()] 

# prompt 从hub中拉取
prompt = hub.pull('hwchase17/structured-chat-agent')

model = ChatDeepSeek(model="deepseek-chat", temperature=0)

# 创建agent
agent = create_structured_chat_agent(
    llm=model,
    tools=tools, # 告诉 agent 我们有哪些工具可以使用
    prompt=prompt,
)

# 连续对话，定义memory
memory = ConversationBufferMemory(
    return_messages=True,
    memory_key="chat_history"
)

# 创建agent执行器
agent_executor = AgentExecutor.from_agent_and_tools(agent=agent,
                                                     tools=tools, # 实际可调用的工具
                                                     memory=memory,
                                                     handle_param_errors=True, # 不按照ReAct框架输出时，不终止程序，而是将错误返回给大模型
                                                     verbose=True  # 打印执行中的日志
                                                     )

response = agent_executor.invoke({"input": "请计算以下文本的字数：'Hello, world!'"})
print(response)

