from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain_deepseek import ChatDeepSeek
import os

# 加载环境变量
load_dotenv()

# 创建一个聊天提示模板
template = ChatPromptTemplate.from_messages(
    [
        ("system", "{parser_instructions}"),
        ("human", "列出5个{subject}色系的十六进制颜色码。")
    ]
)


# 创建一个输出解析器（要获取输出解析器的指令，要先有输出解析器）
output_parser = CommaSeparatedListOutputParser()

# 获取输出解析器的指令
parser_instructions = output_parser.get_format_instructions()

# 将指令文本和用户提示的变量值，一起传给提示模板的invoke方法，得到完整的提示文本
final_prompt = template.invoke(
    {
        "parser_instructions": parser_instructions,
        "subject": "莫兰迪"
    }
)

# 创建模型
model = ChatDeepSeek(model="deepseek-chat")

# 调用模型
response = model.invoke(final_prompt)

# 使用输出解析器的invoke方法解析输出文本
result = output_parser.invoke(response)
print(result)
