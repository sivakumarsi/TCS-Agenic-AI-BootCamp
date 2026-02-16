from langchain_ollama import ChatOllama

llm = ChatOllama(model = 'gemma2:2B')

response = llm.invoke( 'what is a crossbow?') 

print(response.content)
