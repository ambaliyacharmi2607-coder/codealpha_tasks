# Simple Rule-Based Chatbot

def chatbot():
    print("Chatbot: Hello! I am a simple chatbot.")
    print("Chatbot: You can say 'hello', 'how are you', or 'bye'.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("Chatbot: Hi!")

        elif user_input == "how are you":
            print("Chatbot: I am fine, thanks!")

        elif user_input == "bye":
            print("Chatbot: Goodbye!")
            break

        else:
            print("Chatbot: Sorry, I don't understand that.")

# Start the chatbot
chatbot()