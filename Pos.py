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

# Proof of Concept function
def chatbot_poc():
    print("\n--- Proof of Concept ---")
    test_inputs = ["hello", "how are you", "tell me a joke", "what can you do", "goodbye"]
    for user_input in test_inputs:
        print(f"\nYou: {user_input}")
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")

# Run the POC
if __name__ == "__main__":
    chatbot_poc()
