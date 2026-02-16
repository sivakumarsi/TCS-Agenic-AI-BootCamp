from langchain_ollama import ChatOllama
llm = ChatOllama(model='gemma2:2B')

response = llm.invoke("Say a prayer to God Murugan")
print(response.content)
