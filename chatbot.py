# AI Chatbot using Prompt Engineering (Basic Version)

def chatbot():
    print("AI Chatbot: Hello! Type 'bye' to exit.\n")

    while True:
        user = input("You: ").lower()

        if user == "bye":
            print("AI Chatbot: Goodbye!")
            break

        elif "hello" in user or "hi" in user:
            print("AI Chatbot: Hey! How can I help you?")

        elif "what is python" in user:
            print("AI Chatbot: Python is a programming language used for web development, AI, and more.")

        elif "ai" in user:
            print("AI Chatbot: AI stands for Artificial Intelligence — machines that mimic human thinking.")

        elif "help" in user:
            print("AI Chatbot: I can answer basic questions about programming and AI.")

        else:
            print("AI Chatbot: I’m not sure, but I’m learning!")

# Run chatbot
chatbot()