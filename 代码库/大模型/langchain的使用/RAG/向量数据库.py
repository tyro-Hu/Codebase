from langchain_community.vectorstores import FAISS

# 分割文档和实例化嵌入模型
texts  = ['hello world', 'hello again']
embeddings_model = "这里是embedding模型"

# 将文档和嵌入向量存储到FAISS数据库中
db = FAISS.from_documents(texts, embeddings_model)

# 相似性搜索，返回最相似的文档
# 1. 得到一个检索器
retriever = db.as_retriever()

# 2. 检索器进行检索
retrieved_docs = retriever.invoke("世界上最高的山是什么山？")  