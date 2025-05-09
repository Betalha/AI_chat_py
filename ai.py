import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")  

def get_ai_response(message, history=None):
    """
    Sends the user's message and conversation history to the AI and returns the response.
    """
    messages = history.copy() if history else []
    messages.append({"role": "user", "content": message})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response.choices[0].message.content
