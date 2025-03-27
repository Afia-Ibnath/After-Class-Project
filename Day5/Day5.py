def chatbot():
    responses = {
        "hello": "Hi! How can I help?",
        "bye": "bye!",
        "how are you": "I'm good, thanks!",
    }
    
    while True:
        user_input = input("You: ").lower()
        if user_input == "bye":
            print("Chatbot: Goodbye!")
            break
        print("Chatbot:", responses.get(user_input, "I don't understand."))

chatbot()