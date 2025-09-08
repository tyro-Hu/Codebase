from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field 
from typing import List
from langchain.prompts import ChatPromptTemplate
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

class BookInfo(BaseModel):
    book_name: str = Field(description="书籍的名字", examples="百年孤独")
    author_name: str = Field(description="书籍的作者", examples="加西亚·马尔克斯")
    genres: List[str] = Field(description="书籍的体裁", examples=["小说", "文学"])

# 创建一个输出解析器的实例.这个解析器可以做两件事情：
# 1. 指令要求模型根据各个字段的要求输出JSON
# 2. 把模型输出的JSON，解析成对应的BookInfo实例
output_parser = PydanticOutputParser(pydantic_object=BookInfo)

# 创建提示模板，把给AI的消息列表写出来
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "{parser_instructions}。你输出的结果请使用中文。"),
        ("human", "请你帮我从书籍概述中，提取书名、作者，以及书籍的体裁。书籍概述会被三个###顾好包围。\n###{book_insroduction}###")
    ]
)

book_insroduction = """《明朝那些事儿》,作者是当年明月。2006年3月在天涯
轻女首次发表,2009年3月21日连载完毕,边写作边集结成书出版发行,一共7本。
《明朝那些事儿》主要讲述的是从1344年到1644年这三百年间关于明朝的一些故事。以 史料为基础,以年代和具体人物为主线,并加入了小说的笔法,语言幽默风趣。对明朝十 六帝和其他王公权贵和小人物的命运进行全景展示,尤其对官场政治、战争、帝王心术着 墨最多,并加入对当时政治经济制度、人伦道德的演义。
它以一种网络语言向读者娓娓道出三百多年关于明朝的历史故事、人物。其中原本在历史 中陌生、模糊的历史人物在书中一个个变得鲜活起来。《明朝那些事儿》为读者解读历史 中的另一面,让历史变成一部活生生的生活故事。"""

# 填充提示模板，生成完整的提示
final_prompt = prompt.invoke(
    {
        "parser_instructions" : output_parser.get_format_instructions(),
        "book_insroduction" : book_insroduction
    }
)

# 创建一个ChatDeepSeek实例，并使用它来生成回答
model = ChatDeepSeek(model="deepseek-chat")

# 调用模型生成回答
response = model.invoke(final_prompt)

# 使用输出解析器，把模型输出的JSON，解析成对应的BookInfo实例
book_info = output_parser.invoke(response)

print(response.content)



"""
总结：
1. 定义Pydantic数据结构（如`BookInfo`），指定字段及其描述和示例。
2. 实例化`PydanticOutputParser`，生成JSON格式化指令并解析输出。
3. 创建`ChatPromptTemplate`，嵌入解析器指令和用户输入要求。
4. 使用`prompt.invoke`填充模板，生成完整提示。
5. 调用语言模型（如`ChatDeepSeek`）生成JSON格式响应。
6. 使用解析器将模型输出解析为Pydantic实例。
7. 访问解析后的字段或打印原始输出以验证。

知识点：
1. pydantic就像一个“数据检查员”，可以确保数据格式正确，自动转换类型，还能将数据打包成JSON或者从JSON中解包。
2. pydantic中的BaseModel是定义规则的主框架，所有数据类型都得继承它。告诉pydantic
你的数据有哪些字段，每个字段是什么类型。继承之后，一旦输入的数据类型不对，会进行提示和报错。
3. pydantic中的Field就像给表格中的每一栏加上备注说明。给每个字段加上具体要求，比如：字段描述、最大值、最小值、是否必填、默认值、格式要求等。
4. typing中的List是类型注解工具，用来描述变量的类型，而list是实际的列表类型，用来存储和操作数据。
"""