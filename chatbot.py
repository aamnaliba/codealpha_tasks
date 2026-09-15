def chatbot():

    print("================================")
    print("       Simple Python Chatbot")
    print("================================")
    print("Type 'bye' to exit the chatbot.")

    while True:

        user_input = input("\nYou: ").lower()

        if user_input == "hello" or user_input == "hi":
            print("Bot: Hi! Nice to meet you!")

        elif user_input == "how are you":
            print("Bot: I'm fine! How are you?")

        elif user_input == "what is your name":
            print("Bot: I'm a simple Python chatbot.")

        elif user_input == "thank you" or user_input == "thanks":
            print("Bot: You're welcome!")

        elif user_input == "bye":
            print("Bot: Goodbye! Have a great day!")
            break

        else:
            print("Bot: Sorry, I don't understand that.")


chatbot()