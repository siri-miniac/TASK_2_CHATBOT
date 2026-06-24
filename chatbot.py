def chatbot(): 
    print("Chatbot:Hi! I am a chatbot.Type 'bye' to exit.")
    while True:
        user=input("You: ").lower()
        if user=="hello" or user=="hi":
            print("Chatbot:Hi!")
        elif user=="how are you":
            print("Chatbot:I am fine,thanks!")
        elif user=="what is your name":
            print("Chatbot:I am simple chatbot!")
        elif user=="bye":
            print("Chatbot:Goodbye!")
            break
        else:
            print("Chatbot:Sorry,I dont understand that!")
chatbot()
