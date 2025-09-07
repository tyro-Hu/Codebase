from langchain.prompts import FewShotChatMessagePromptTemplate, ChatPromptTemplate
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

example_prompt = ChatPromptTemplate.from_messages(
    [
        ("human", "格式化以下客户信息：\n姓名 -> {customer_name}\n年龄 -> {customer_age}\n 城市 -> {customer_city}"),
        ("ai", "##客户信息\n- 客户姓名：{formattend_name}\n- 客户年龄：{formattend_age}\n- 客户城市：{formattend_city}")
    ]
)

examples = [
    {
        "customer_name": "张三",
        "customer_age": "27",
        "customer_city": "长沙",
        "formattend_name": "张三",
        "formattend_age": "27岁",
        "formattend_city": "湖南省长沙市"
    },
    {
        "customer_name": "李四",
        "customer_age": "42",
        "customer_city": "广州",
        "formattend_name": "李四",
        "formattend_age": "42岁",
        "formattend_city": "广东省广州市"
    }
]

# 使用小样本提示词模板，传入示例和示例提示词，生成小样本提示词模板
few_shot_prompt = FewShotChatMessagePromptTemplate(
    example_prompt=example_prompt,
    examples=examples
)

# 将小样本的模板和用户输入的模板组合起来，生成最终提示词模板。 
# 注意：from_messages()方法的列表中，不仅可以接受元组还可以接受其他模板
final_prompt_template = ChatPromptTemplate.from_messages(
    [
        few_shot_prompt,
        ("human", "{input}"),
    ]
)

# 但是模板不能直接传给模型，因为里面可能有动态变量，调用invoke方法,传入参数字典，生成最终提示词
final_prompt = final_prompt_template.invoke({"input":"格式化以下客户信息：\n姓名 -> 王五\n年龄 -> 31\n 城市 -> 郑州"})

# 创建模型
model = ChatDeepSeek(model="deepseek-chat")

# 调用模型，传入最终提示词
response = model.invoke(final_prompt)

print(response.content)
