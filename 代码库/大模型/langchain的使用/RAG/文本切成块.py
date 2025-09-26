from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader


# 文本分割器RecursiveCharacterTextSplitter根据指定的字符进行分割
# chunk_size：每个块的最大长度，字符长度
# chunk_overlap：每个块之间的重叠长度，字符长度
# separators：用于分割的字符列表。首先尝试按段落 \n\n 切分，如果还太长，就按单行换行 \n 切分。默认["\n\n", "\n", " ", ""]
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=40,
    separators=["\n\n", "\n", "。", "！", "?", "；", "，", "、", ""]
)

# 加载文档
loader = TextLoader("data.txt")
documents = loader.load()

# 分割文档
split_docs = text_splitter.split_documents(documents)

# 打印分割后的文档
for doc in split_docs:
    print(doc.page_content)