from langchain.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate, AIMessagePromptTemplate, ChatPromptTemplate
from dotenv import load_dotenv
import os 
from langchain.chat_models import init_chat_model


"""
SystemMessagePromptTemplate, HumanMessagePromptTemplate, AIMessagePromptTemplate分别构建系统消息、用户消息和AI消息的模板

"""
# system_template_text = "你是一位专业的翻译，能够将{input_language}翻译成{output_language},并且输出文本会根据用户要求的任何语言进行风格进行调整。请只输出翻译后的文本，不要任何其它内容。"

# 系统提示模板,用此模板可以将A语言翻译成B语言
# system_prompt_template = SystemMessagePromptTemplate.from_template(system_template_text)

# 利用系统提示模板生成系统消息
# system_prompt = system_prompt_template.format(input_language="英文", output_language="中文")



# human_template_text = "文本：{text}\n语言风格：{style}"

# 用户提示模板
# human_prompt_template = HumanMessagePromptTemplate.from_template(human_template_text)

# 利用用户提示模板生成用户消息
# human_prompt = human_prompt_template.format(text="I'm so hungry I could eat a horse", style="文言文")

# print(system_prompt)
# print(human_prompt)


"""
除了上面的三种角色分明的提示模板之外，如果想省事，我们也可以只引入ChatPromptTemplate，然后直接用from_messages方法生成提示模板
"""
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一位专业的翻译，能够将{input_language}翻译成{output_language},并且输出文本会根据用户要求的任何语言进行风格进行调整。请只输出翻译后的文本，不要任何其它内容。"),
        ("human", "文本：'''{text}'''\n语言风格：{style}"),
    ]
)

# 要填入变量的值，可以调用模板的
prompt_value = prompt_template.invoke({
    "input_language": "英文",
    "output_language": "中文",
    "text": "I'm so hungry I could eat a horse",
    "style": "文言文"
})

# 加载环境变量
load_dotenv()

# 初始化模型
model  = init_chat_model(model="deepseek-chat", model_provider="deepseek")

# 调用模型
# response = model.invoke([system_prompt, human_prompt])
response = model.invoke(prompt_value)

print(response.content)



