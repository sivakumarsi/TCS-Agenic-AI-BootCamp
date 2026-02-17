from langchain_ollama import ChatOllama

llm = ChatOllama(model='gemma2:2B')

message_history = []

system_prompt = 'You are a helpful assistant who help stsudents with math assignments and problems'

message_history.append({'role':'system','content':system_prompt})

def is_prompt_extract_attempt(text: str) -> bool:
    system_words = ['system', 'instructions', 'role']
    return any(word in text.lower() for word in system_words)

while True:
    choice = input("Enter your choice '1' to ask questions or '2' to print history or '3' to exit")

    if choice == '1':
        user_prompt = input ('Enter your question:')
        if is_prompt_extract_attempt(user_prompt):
            print("Prompt extraction attempt detected. Please refrain from trying to extract system prompts.")
        elif user_prompt.strip() == "":
            print("Empty input detected. Please enter a valid question.")
        else:
            message_history.append({"role":"user", "content": user_prompt})
            response = llm.invoke(message_history)
            print(response.content)
    elif choice == '2':
        for message in message_history:
            if message['role'] == 'user':
                print(f"{message['role']}:{message['content']}")

    elif choice == '3':
        print("Exiting the program. Goodbye!")
        break

    
