from huggingface_hub import InferenceClient

# 1. 在 https://huggingface.co/settings/tokens 申请一个 Token
HF_TOKEN = "XXX"  

# 2. 创建客户端
client = InferenceClient(token=HF_TOKEN)

# 3. 调用 bge-m3 模型生成向量
resp = client.feature_extraction(
    model="BAAI/bge-m3",
    text="今天天气很好，我们去公园散步吧。"
)

# 4. 输出结果
print(f"向量维度: {resp.size}")  # 应该是 1024
print(f"前10个数: {resp[:10]}")  # 打印前 10 个数
