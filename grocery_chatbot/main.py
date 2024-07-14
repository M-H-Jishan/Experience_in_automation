from chatbot.bot import GroceryStoreChatbot

def main():
    chatbot = GroceryStoreChatbot()
    print(chatbot.greet())

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Thank you for shopping with us. Goodbye!")
            break
        response = chatbot.respond(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()