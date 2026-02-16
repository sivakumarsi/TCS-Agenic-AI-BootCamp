from langchain_ollama import ChatOllama
llm = ChatOllama(model='gemma2:2B')

message_history = []

system_prompt = 'You are a helpful assisistant who helps students with math problems'

message_history.append({'role':'system', 'content':system_prompt})

user_prompt = 'How do I find the LCM of 12 and 15?'

message_history.append({'role':'user', 'content':user_prompt})

response = llm.invoke(message_history)

print(response.content)
