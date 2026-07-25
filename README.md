# my_ai_knowledge
个人学习大模型与LangChain框架实战代码仓库，收录从原生API调用到LangChain组件封装的入门Demo，用于学习复盘与知识沉淀。

## 目录结构
```
my_ai_knowledge/
├── chat_with_model                # 原生接口实现大模型对话
│   ├── 2_测试大模型记忆.py
│   ├── 6_流式输出.py
│   ├── 7_多轮对话.py
│   ├── 8_流式输出多轮对话.py
│   └── __init__.py
├── langcahin_quick_start         # LangChain快速上手案例
│   ├── 1_和狭义大模型对话.py
│   ├── 2_狭义大模型流式对话.py
│   ├── 3_和聊天模型对接.py
│   ├── 4_和聊天模型对接流式输出.py
│   ├── 5-消息类型简写.py
│   ├── 6_实现讨论对话.py
│   ├── 7_向量模型.py
│   ├── 8_向量相似度判断.py
│   ├── __init__.py
│   └── test.py
└── langchain_prompt_outputparser # 提示词工程与输出解析器
    ├── 1_解释机器学习.py
    └── 2_提示词引入.py
```

## 模块功能介绍
### 1. chat_with_model
不依赖LangChain，原生调用大模型接口实现基础能力：
- 多轮对话上下文记忆留存
- 打字机效果流式输出
- 多轮会话+流式输出组合实现

### 2. langcahin_quick_start
LangChain核心基础入门代码：
- 基础LLM与ChatModel两种模型调用方式
- 聊天模型流式接口返回处理
- LangChain消息体Message简化写法
- 文本向量化、向量相似度计算（向量库知识库前置基础）

### 3. langchain_prompt_outputparser
提示词工程基础练习：
- Prompt提示词模板构建与变量注入
- 大模型结构化输出解析初步实践

## 环境依赖
```
langchain
langchain-openai
numpy
```

## 运行说明
1. 在对应Python文件中配置自己的大模型API Key、接口地址；
2. 单个py文件可直接独立运行测试效果；
3. 向量相关代码可自行替换不同Embedding嵌入模型。

## 声明
所有代码为学习过程演示版本，仅用于理解原理，未做异常处理、配置解耦、日志封装等工程化优化，仅供个人学习参考。

直接全选复制粘贴到编辑框即可提交。
