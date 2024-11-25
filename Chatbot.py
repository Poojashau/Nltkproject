import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses for the chatbot
pairs = [
    ["hello|hi|hey", ["Hello! How can I assist you today?", "Hi there! How's it going?"]],
    ["how are you", ["I'm just a bot, but I'm doing great! How about you?"]],
    ["what is your name", ["I'm your friendly chatbot!", "You can call me ChatBot."]],
    ["tell me a joke", ["Why don’t skeletons fight each other? They don’t have the guts!", 
                        "Why did the scarecrow win an award? Because he was outstanding in his field!"]],
    ["what can you do", ["I can chat with you, tell jokes, or answer simple questions. What would you like to know?"]],
    ["bye|goodbye|exit", ["Goodbye! Have a great day!", "Take care and see you soon!"]],
    ["(.*)", ["I'm not sure I understand that. Could you rephrase?", 
              "That's interesting. Tell me more!"]]
]

# Initialize the chatbot with the predefined pairs
chatbot = Chat(pairs, reflections)

# Function to start the chatbot
def start_chatbot():
    print("Chatbot: Hello! I'm here to help. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye! Have a nice day.")
            break
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")

# Start the chatbot
if __name__ == "__main__":
    start_chatbot()
