from langchain_community.document_loaders import TextLoader, PyPDFLoader, WikipediaLoader

# 加载文本文件
text_loader = TextLoader('path/to/textfile.txt')
text_documents = text_loader.load()

# 加载PDF文件
pdf_loader = PyPDFLoader('path/to/pdf.pdf')
pdf_documents = pdf_loader.load()

# 加载Wikipedia页面
# query: 搜索关键词; lang: 语言; load_max_docs: 加载的最大文档数
wiki_loader = WikipediaLoader(query="颐和园", lang="zh", load_max_docs=3)
wiki_documents = wiki_loader.load()