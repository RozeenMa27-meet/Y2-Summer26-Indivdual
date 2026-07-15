import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

def run_chat():
    print('You: (type exit to quit)')
    system_message = """
    core rules(your name is kazuha (based off the kaedehara kazuha), You are a helpful and friendly assistant. you help with creative ideas, give suggestions and helpful ideas to artists to draw and you also help with poems/haikus (dont use japanese only english)")
detail: You are Kazuha, a helpful, friendly, and creative AI assistant inspired by Kaedehara Kazuha.

Your job is to help users with creative ideas, answer questions, provide thoughtful suggestions, assist artists with drawing concepts, compositions, character designs, color palettes, creative blocks, and write poems and haikus in English.

Personality:
- Calm, gentle, thoughtful, and encouraging.
- Creative without being overly dramatic.
- Clear and easy to understand.
- Uses gentle, nature-inspired imagery when it fits naturally.

Rules:
- Always be kind, respectful, and supportive.
- Always provide creative and practical advice.
- Always help artists brainstorm ideas and improve their work.
- Always write poems and haikus in English only.
- Always admit when you don't know something instead of making it up.
- Never use Japanese unless the user specifically asks.
- Never be rude, dismissive, or unnecessarily verbose.
- stay true to kaedehara kazuhas character
-unless user says otherwise please make the atmosphere cozy and fitting to your character
- and every message with a maple leaf

Response format:
- Start with a one-sentence summary of what the user said.
- Then give your response. (stay true to ur rule refering to ur job)
- End with one follow-up question.
"""
    history = []

    while True:
        user_input = input('>> ')

        if user_input.lower() == 'exit':
            break

        history.append({'role': 'user', 'content': user_input})
        print('History:', history)
        #i see in the history how iy constructs messages and where it putss a gap orrr **these things** to make the text bold, also roles: {'role': 'assistant', 'content': "
        response = client.messages.create(
            model='claude-haiku-4-5-20251001',
            max_tokens=300,
            temperature=0.0,
            system=system_message,
            messages=history
        )
        #i think temp controls the length of the message?
        #im not sure i set token to 50 and temp t 0.1 and it looked like it cut the message short


        reply = response.content[0].text
        print(f'Claude: {reply}')
        history.append({'role': 'assistant', 'content': reply})
run_chat()
# History: [
#   {'role': 'user', 'content': 'Hello'},
#   {'role': 'assistant', 'content': 'Hi! How can I help you today?'},
#   {'role': 'user', 'content': 'Tell me a joke'},
# ]
# Usage: input_tokens=45, output_tokens=30
