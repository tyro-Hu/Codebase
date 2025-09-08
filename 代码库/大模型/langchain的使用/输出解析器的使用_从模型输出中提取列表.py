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

"""
总结：
1. 创建一个输出解析器
2. 获取输出解析器的指令
3. 将指令文本和用户提示的变量值，一起传给提示模板的invoke方法，得到完整的提示文本
4. 将模型调用后的结果，传给输出解析器的invoke方法，得到解析后的结果

输出解析器的作用：
1. 给模型下指令，指令里要求模型按照指定的格式输出。
2. 解析模型的输出，提取所需的信息。（不是简单的提取模型输出中的字符串，而是解析为对应的数据格式，如列表，或者类）
"""


