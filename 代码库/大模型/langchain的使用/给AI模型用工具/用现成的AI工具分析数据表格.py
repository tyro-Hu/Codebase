from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv

load_dotenv()

model = ChatDeepSeek(model="deepseek-chat", temperature=0)

agent_executor = create_csv_agent(
    llm=model,
    path=r"大模型\langchain的使用\给AI模型用工具\housing.csv",
    verbose=True,
    agent_executor_kwargs={"handle_parsing_errors": True},
    allow_dangerous_code=True
)

response = agent_executor.invoke({"input":"数据集里，所有房子的价格的平均值是多少？用中文回复。"})
print(response['output'])