Langchain构成

- langchain-core: 基础抽象类和 LangChain 表达式语言。

- langchain-community: 第三方集成。
  - 合作伙伴包（例如 langchain-openai、langchain-anthropic 等）：一些集成已进一步拆分为自己的轻量级包，仅依赖于 langchain-core。

- langchain: 构成应用程序认知架构的链、代理和检索策略。

- langgraph: 通过将步骤建模为图中的边和节点，使用 LLM 构建健壮且有状态的多角色应用程序。

- langserve: 将 LangChain 链部署为 REST API。

- LangSmith: 一个开发者平台，可让您调试、测试、评估和监控 LLM 应用程序，并与 LangChain 无缝集成。


## LLMS


## Prompts 提示词模板

PromptTemplate

```python
from langchain.prompts import  PromptTemplate  
  
prompt_template = PromptTemplate.from_template("将{content}翻译成{lang}")  
  
# prompt_template.format(content='hi',lang='chinese')  
# prompt_template = PromptTemplate.from_template('给我讲个笑话')  
# prompt_template.format()  此时无需传递参数
```

ChatPromptTemplate

```python
from langchain.prompts import ChatPromptTemplate  
  
chat_template = ChatPromptTemplate.from_messages(  
    [  
        ('system','你是一个语言专家，你的名字是Emy'),  
        ('human','你最近怎么样？'),  
        ('ai','我很好，谢谢'),  
        ('human','{question}')  
    ]  
)  
message= chat_template.format_messages(question='你从哪里来？')  
message


from langchain_core.messages import SystemMessage, HumanMessage,AIMessage  
from langchain.prompts import HumanMessagePromptTemplate  
chat_template = ChatPromptTemplate.from_messages(  
    [  
        SystemMessage(content='你是一个语言专家，你的名字是Emy'),  
        HumanMessage(content='你最近怎么样？'),  
        AIMessage(content='我很好，谢谢'),  
        # HumanMessage(content='{question}'),  
        HumanMessagePromptTemplate.from_template('{text}')  
    ]  
)  
# 如果使用 HumanMessagePromptTemplate  
message = chat_template.format_messages(text='你从哪里来')
```
## Memory



## Chains



## Vector stores



## Document loaders