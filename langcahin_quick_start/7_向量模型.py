from langchain_community.embeddings import DashScopeEmbeddings

# 1.创建嵌入模型对象
embedding = DashScopeEmbeddings(model='text-embedding-v1')  # 默认使用text-embedding-v1

# 2.向量化
# user_input=input('用户：')
vector = embedding.embed_query('你好，yubo')

# 3.处理输出
print(vector)
print(len(vector))

# 4.批量处理
texts = ['你好，yubo', 'yubo你真好', 'yubo你太好了']
vectors = embedding.embed_documents(texts)
# [向量1，向量2，向量3]
print(len(vectors))
print(vectors)
print(vectors[0])
print(len(vectors[0]))