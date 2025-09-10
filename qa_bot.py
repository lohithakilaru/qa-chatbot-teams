import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def get_answer(question: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": question}],
        max_tokens=256
    )
    return response.choices[0].message["content"].strip()
