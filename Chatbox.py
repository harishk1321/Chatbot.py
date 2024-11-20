def chatbot():
    print("Chatbot: Hello! I'm here to help you. Type 'exit' to end the chat.\n")
    while True:
        # Taking user input
        user_input = input("You: ").strip().lower()

        # Check if user wants to exit
        if user_input == 'exit':
            print("Chatbot: Goodbye! Have a nice day!")
            break

        # Rule-based responses
        elif "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hi there! How can I assist you today?")
        elif "how are you" in user_input:
            print("Chatbot: I'm just a program, but I'm functioning perfectly! How about you?")
        elif "your name" in user_input:
            print("Chatbot: I'm a simple chatbot created to assist you.")
        elif "help" in user_input:
            print("Chatbot: Sure! I can answer questions or have a friendly chat.")
        elif "bye" in user_input:
            print("Chatbot: Bye! Feel free to return anytime.")
            break
        else:
            print("Chatbot: I'm sorry, I didn't understand that. Can you rephrase?")

# Run the chatbot
chatbot()
