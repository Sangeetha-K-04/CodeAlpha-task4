# ChatBuddy - A Simple Rule-Based Chatbot
# This chatbot responds to a few basic messages in a friendly and fun way.

def chat_response(message):
    # Convert input to lowercase for easy matching
    message = message.lower().strip()

    # Predefined responses for common inputs
    replies = {
        "hello": "Hey there! Nice to meet you!",
        "hi": "Hi! Hope you're doing well today!",
        "how are you": "I'm doing great, thanks for asking! What about you?",
        "what is your name": "You can call me ChatBuddy. I’m still learning!",
        "who created you": "A curious mind with a love for Python!",
        "what can you do": "I can chat with you for now, but I’m getting smarter every day!",
        "bye": "It was nice chatting with you. Take care!",
        "thank you": "Anytime!"
    }

    # Return matched response or a default fallback
    return replies.get(message, "Hmm... I’m not sure how to respond to that yet ")

# --- Program Starts Here ---
print("ChatBuddy at your service!")
print("Type anything you'd like to say (type 'exit' to end the chat)\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("ChatBuddy: Goodbye! See you next time.")
        break

    bot_reply = chat_response(user_input)
    print("ChatBuddy:", bot_reply)
