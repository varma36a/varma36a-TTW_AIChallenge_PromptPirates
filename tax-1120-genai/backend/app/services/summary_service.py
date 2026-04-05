from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_summary(data, result):

    prompt = f"""
    Generate a professional tax summary:

    Input Data: {data}
    Result: {result}

    Keep it clear and client-friendly.
    """

    response = client.chat.completions.create(
        model="gpt-5-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )

    return response.choices[0].message.content