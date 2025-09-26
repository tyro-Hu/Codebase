from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
from langchain_experimental.tools import PythonREPLTool
from langchain_experimental.agents.agent_toolkits import create_python_agent

load_dotenv()  # 加载环境变量

model = ChatDeepSeek(model="deepseek-chat", temperature=0)

agent_executor = create_python_agent(
    llm=model,
    tool=PythonREPLTool(),
    verbose=True,
    agent_executor_kwargs={"handle_parsing_errors" : True}
)

response = agent_executor.invoke({"input": "7的2.3次方是多少？"})
print(response["output"])

