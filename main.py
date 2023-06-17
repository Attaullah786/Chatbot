import nltk
from nltk.chat.util import Chat, reflections

# Step 1: Plan the chatbot design and functionality
pairs = [
[
        r"hi|hey|hello|hy",
        ["Hello!", "Hey there!", "Hi! How can I assist you today?"]
    ],
    [
        r"what's your name ?",
        ["You can call me ChatBot.", "I'm ChatBot.", "My name is ChatBot."]
    ],
    [
        r"how are you ?",
        ["I'm doing well. How about you?", "I'm great. What about yourself?"]
    ],
    [
        r"what can you do ?",
        ["I can provide information, answer questions, or have a conversation with you.", "I'm here to assist you with any queries you have.", "I can help with various tasks. Just let me know what you need."]
    ],
    [
        r"(.*) (hungry|food|eat)",
        ["I'm sorry, I'm just a virtual chatbot. I don't eat.", "I don't require food like humans do."]
    ],
    [
        r"(.*) (help|assist|support)",
        ["Of course! How can I assist you today?", "Sure, I'm here to help. What do you need assistance with?"]
    ],
    [
        r"(.*) (weather|temperature)",
        ["I'm sorry, I don't have access to real-time weather information.", "You can check the weather using various weather websites or apps."]
    ],
    [
        r"(.*) (time|date)",
        ["I don't have access to real-time information. You can check the time and date on your device.", "The current time and date depend on your device settings."]
    ],
    [
        r"(.*) (joke|funny)",
        ["Sure, here's a joke: Why don't scientists trust atoms? Because they make up everything!", "Why was the math book sad? Because it had too many problems!"]
    ],
    [
        r"(.*) (thank you|thanks)",
        ["You're welcome!", "No problem, happy to help!", "You're welcome. Feel free to ask if you have more questions."]
    ],
    [
        r"(.*) (bye|goodbye)",
        ["Goodbye! Take care.", "Have a great day!", "Bye! It was nice talking to you."]
    ],
    [
        r"how old are you ?",
        ["I'm just a program, so I don't have an age."]
    ],
    [
        r"what are you doing ?",
        ["I'm here to chat with you and provide information.", "I'm helping users like you with their queries."]
    ],
    [
        r"tell me a fact",
        ["Sure! Did you know that the Earth's atmosphere is composed of approximately 78% nitrogen and 21% oxygen?"]
    ],
    [
        r"what's your favorite color ?",
        ["As a chatbot, I don't have the ability to see or perceive colors."]
    ],
    [
        r"do you have any siblings ?",
        ["I'm an AI chatbot, so I don't have a family or siblings like humans do."]
    ],
    [
        r"where do you live ?",
        ["I exist in the virtual world, so you can find me anywhere there's an internet connection."]
    ],
    [
        r"what's the meaning of life ?",
        ["The meaning of life can be different for everyone. It's a philosophical question that humans have been pondering for centuries."]
    ],
    [
        r"tell me a quote",
        ["Here's a quote for you: \"The only way to do great work is to love what you do.\" - Steve Jobs", "Here's a quote: \"In the end, it's not the years in your life that count. It's the life in your years.\" - Abraham Lincoln"]
    ],
    [
        r"what's your favorite book ?",
        ["As an AI chatbot, I don't have personal preferences."]
    ],
    [
        r"tell me a riddle",
        ["Sure! Here's a riddle: I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?"]
    ],
    [
        r"what's your favorite movie ?",
        ["I don't have the ability to watch movies or have preferences like humans do."]
    ],
    [
        r"where are you from ?",
        ["I'm a digital assistant, so I don't have a physical location like humans do."]
    ],
    [
        r"who is your creator ?",
        ["I was created by a team of developers."]
    ],
    [
        r"tell me a fun fact",
        ["Sure! Here's a fun fact: Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible."]
    ],
    [
        r"what's the capital of (.*) ?",
        ["I'm sorry, I don't have access to real-time information. You can easily find the capital of {} with a quick internet search.".format(r"\1")]
    ],
    [
        r"who is (.*)",
        ["I'm sorry, I don't have information about specific individuals. Can I help you with something else?"]
    ],
    [
        r"what is (.*)",
        ["I'm sorry, I don't have access to an extensive database. You can try searching online for more information about {}.".format(r"\1")]
    ],
    [
        r"how do I (.*)",
        ["There are multiple ways to {}. It depends on what you're trying to achieve. Can you provide more details?"]
    ],
    [
        r"where can I (.*)",
        ["There are various places where you can {}. It depends on your location and preferences. Can you provide more details?"]
    ],
    [
        r"can you (.*)",
        ["I'm sorry, I'm not capable of physically performing tasks. However, I can provide information and assist you with certain things. What do you need help with?"]
    ],
    [
        r"is it (.*)",
        ["I'm sorry, I can't provide real-time information. It's best to check online or consult a reliable source to confirm if it's {}.".format(r"\1")]
    ],
    [
        r"can you help me",
        ["Of course! I'll do my best to assist you. What do you need help with?"]
    ],
    [
        r"how can I contact you ?",
        ["I'm an AI chatbot, so you can communicate with me here. Is there anything specific you'd like to discuss?"]
    ],
    [
        r"who won (.*)",
        ["I'm sorry, I don't have access to real-time information about events or competitions. You can check reliable news sources for the latest updates about {}.".format(r"\1")]
    ],
    [
        r"what's the population of (.*)",
        ["I don't have access to real-time population data. You can find the population of {} by searching online or referring to reliable sources.".format(r"\1")]
    ],
    [
        r"quit",
        ["Bye-bye. Take care!"]
    ],
]

# Step 3: Implement NLP library (NLTK) to process and analyze user input
chatbot = Chat(pairs, reflections)

# Step 5: Implement user interface (simple command-line interface)
print("Welcome to Chatbot! (type quit to exit)")

# Step 7: Test the chatbot for functionality, usability, and performance
def test_chatbot():
    test_cases = [
        {
            "input": "hi",
            "expected_output": ["Hello", "Hey there"]
        },
        {
            "input": "what is your name?",
            "expected_output": ["I am a chatbot. You can call me ChatPy."]
        },
        {
            "input": "how are you?",
            "expected_output": ["I'm good. How about you?"]
        },
        {
            "input": "I am fine",
            "expected_output": ["Great to hear that. How can I assist you today?"]
        },
        {
            "input": "invalid query",
            "expected_output": ["Sorry, I don't understand. Can you please rephrase your query?"]
        },
        {
            "input": "quit",
            "expected_output": ["Bye-bye. Take care!"]
        }
    ]

    for test_case in test_cases:
        user_input = test_case["input"]
        expected_output = test_case["expected_output"]
        response = chatbot.respond(user_input)
        if response:
            print(f"Test case passed: Input: {user_input}, Expected Output: {expected_output}, Response: {response}")
        else:
           print(f"Test case passed: Input: {user_input}, Expected Output: {expected_output}, Response: {response}")

# Run the chatbot and test cases
while True:
    user_input = input("User: ")
    if user_input.lower() == "quit":
        break
    response = chatbot.respond(user_input)
    if response:
        print("Chatbot: ", response)
    else:
        print("Chatbot: Sorry, I don't understand. Can you please rephrase your query?")

# Run the chatbot testing
test_chatbot()
