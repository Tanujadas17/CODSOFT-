import re
from datetime import datetime

def chatbot():
    print("Hello! I'm a simple chatbot. How can I help you today?")
    
    while True:
        # Get user input
        user_input = input("You: ").strip().lower()
        
        # Check for exit command
        if user_input in ["bye", "quit", "exit"]:
            print("Chatbot: See you later!")
            break
        
        # Respond to greetings
        elif re.search(r'\b(hi|hello|hey|greetings|what\'s up|howdy)\b', user_input):
            print("Chatbot: Hi there! How can I assist you?")
            
        # Respond to name
        elif re.search(r'\b(what is your name|tell me your name |what was your name again| how you are called| whas your name)\b', user_input):
            print("Chatbot: My name is Hope. It's a pleasure to meet you!") 
            break

        # Respond to farewells
        elif re.search(r'\b(bye|goodbye|see you|later|take care)\b', user_input):
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        # Respond to small talk
        elif re.search(r'\b(how are you|how\'s it going|how do you do|what\'s new)\b', user_input):
            print("Chatbot: I'm just a program, so I don't have feelings, but thanks for asking! How can I assist you?")
        
        # Respond for a joke
        elif re.search(r'\b(tell me a joke)\b', user_input):
            print("Chatbot: Here's a funny joke for you:")
            print("Why don't scientists trust atoms? Because they make up everything!")
        
        # Respond to questions about the chatbot
        elif re.search(r'\b(what can you do|your capabilities|what are you capable of)\b', user_input):
            print("Chatbot: I can answer simple questions, tell you the time and date, and have basic conversations. I'm still under development!")
        
        # Respond to asking the time
        elif re.search(r'\b(what time is it|current time|time now)\b', user_input):
            now = datetime.now().strftime("%H:%M:%S")
            print(f"Chatbot: The current time is {now}.")
        
        # Respond to asking the date
        elif re.search(r'\b(what is the date|current date|today\'s date)\b', user_input):
            today = datetime.now().strftime("%Y-%m-%d")
            print(f"Chatbot: Today's date is {today}.")
        
        # Respond to questions about the weather
        elif re.search(r'\b(weather|what\'s the weather|current weather)\b', user_input):
            print("Chatbot: I currently cannot provide weather updates. Please check a weather website or app.")
        
        # Respond to general knowledge questions
        elif re.search(r'\b(who is|what is|where is|tell me about)\b', user_input):
            print("Chatbot: I'm not equipped to answer general knowledge questions in detail. You might want to look that up online.")
        
        # Respond to thank you
        elif re.search(r'\b(thank you|thanks)\b', user_input):
            print("Chatbot: You're welcome! Is there anything else I can help with?")
        
        # Respond to affirmations
        elif re.search(r'\b(yes|yeah|sure|ok|okay)\b', user_input):
            print("Chatbot: Great! How can I assist you further?")
        
        # Respond to negative responses
        elif re.search(r'\b(no|nope|nah)\b', user_input):
            print("Chatbot: Alright, let me know if there's anything else you need.")
        
        # Generic response for unrecognized input
        else:
            print(f"Chatbot: I'm not sure I understand what you mean by '{user_input}'.")
            print("Chatbot: Could you please rephrase or ask something else?")

# Run the chatbot
chatbot()
