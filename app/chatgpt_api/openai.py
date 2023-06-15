from dotenv import load_dotenv
import openai
import os

load_dotenv()

openai.api_key = os.getenv('CHATGPT_API_KEY')

def chatgpt_response(prompt):

    global prompt_response
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt=prompt,
        temperature=1,
        max_tokens=200
    )

    response_dict = response.get("choices")
    if response_dict and len(response_dict) > 0:
        prompt_response = response_dict[0]["text"]
        return prompt_response
