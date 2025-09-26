from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain_deepseek import ChatDeepSeek
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from huggingface_hub import InferenceClient
from langchain_text_splitters import RecursiveCharacterTextSplitter
from huggingface_hub import InferenceClient
from langchain_community.embeddings import HuggingFaceInferenceAPIEmbeddings
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os

# 文档加载器
loader = TextLoader(r"大模型\langchain的使用\RAG\data.txt")

# 加载文档
docs = loader.load()

# 文本分割器
text_splitter = RecursiveCharacterTextSplitter()

# 分割文档
texts = text_splitter.split_documents(docs)

# embedding模型
embedding_model = OpenAIEmbeddings(
    model="bge-m3",
    api_key="sk-sKcPySd7NTG6mKyyFbP3t9uSAQouM0V2fOdkn019utwfgZcr",
    base_url="http://10.159.252.49:33000/v1"
)

# 构建向量数据库
db = FAISS.from_documents(texts, embedding_model)

# 构建检索器
retriever = db.as_retriever()

# 构建大模型实例
load_dotenv()
model = ChatDeepSeek(
    model="deepseek-chat"
)

# 构建记忆
memory = ConversationBufferMemory(return_messages=True,
                                  memory_key="chat_history", # 因为conversationalRetrievalChain默认的历史消息是"chat_history"
                                  output_key="answer") # 因为conversationalRetrievalChain默认的AI输出的key是"answer"


# 创建对话链
chain = ConversationalRetrievalChain.from_llm(
    llm = model,
    retriever=retriever,
    memory=memory,
    return_source_documents=True
)

result = chain.invoke({"chat_history":memory,
                       "question":"卢浮宫这个名字怎么来的？"})

print(result)