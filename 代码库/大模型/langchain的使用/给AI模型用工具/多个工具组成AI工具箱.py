from langchain_experimental.agents.agent_toolkits import create_python_agent
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
from langchain.tools import Tool, BaseTool
from langchain_experimental.tools import PythonREPLTool
from langchain.agents import create_structured_chat_agent, AgentExecutor
from langchain import hub
from langchain.memory import ConversationBufferMemory


load_dotenv()

model = ChatDeepSeek(model="deepseek-chat", temperature=0)

python_agent_executor = create_python_agent(
    llm=model,
    tool=PythonREPLTool(),
)

csv_agent_executor = create_csv_agent(
    llm=model,
    path=r"大模型\langchain的使用\给AI模型用工具\housing.csv",
    allow_dangerous_code=True
)

class TextLengthTool(BaseTool):
    # 定义类变量，类变量是所有实例共享的变量。定义类变量，必须加上类型注解
    #BaseTool 继承自 pydantic.BaseModel，它内部把字段当作 模型字段 来管理。
    #在 Pydantic v2 里，如果你覆盖了父类的字段，就必须明确声明类型，否则 Pydantic 无法区分 “普通类变量” 和 “模型字段”。
    name : str = "文本字数计算工具"
    description : str = "当你被要求计算文本的字数时，使用此工具"

    # 如果需要调用工具，_run方法会被调用
    def _run(self, text: str): 
        return len(text) 
    
tools = [
    Tool(
        name="python代码工具",
        description="""当你需要借助python解释器时，使用这个工具。
        用自然语言把要求给这个工具，它会生成python代码并返回代码执行的结果。""",
        func=python_agent_executor.invoke,
    ),
    Tool(
        name="csv分析工具",
        description="""当你需要回答有关housing.csv文件的问题时，使用这个工具。
        它接受完整的问题作为输入，在使用pandas库计算后，返回答案。""",
        func=csv_agent_executor.invoke,
    ),
    TextLengthTool(),
]


prompt = hub.pull('hwchase17/structured-chat-agent')

memory = ConversationBufferMemory(
    return_messages=True,
    memory_key="chat_history"
)

agent = create_structured_chat_agent(
    llm=model,
    tools=tools,
    prompt=prompt,
)

agent_executor = AgentExecutor.from_agent_and_tools(
    agent=agent,
    tools=tools,
    memory=memory,
    verbose=True,
    handle_parsing_errors=True,
)

response = agent_executor.invoke({"input":"第8个斐波拉契数列的值是多少？"})
print(response['answer'])

