
print("Chatbot: Hello! Welcome to my chatbot.")
print("Chatbot: Type 'bye' to exit.")

while True:
    user_message = input("You: ").lower().strip()

    if user_message == "bye":
        print("Chatbot: Goodbye!")
        break

    elif "hello" in user_message or "hi" in user_message:
        print("Chatbot: Hello! How can I help you?")

    elif "your name" in user_message:
        print("Chatbot: I am a simple Python chatbot.")

    elif "how are you" in user_message:
        print("Chatbot: I am doing well. Thanks for asking!")

    elif "thank" in user_message:
        print("Chatbot: You are welcome!")

    elif "help" in user_message:
        print("Chatbot: You can greet me, ask my name, or ask how I am.")

    else:
        print("Chatbot: Sorry, I don't understand that yet.")
