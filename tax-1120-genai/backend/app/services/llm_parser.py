import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def parse_nlq(query: str):

    prompt = f"""
    Extract IRS Form 1120 tax fields from the input.

    Input: "{query}"

    Return JSON ONLY:
    {{
      "gross_receipts": number,
      "cogs": number,
      "total_deductions": number,
      "depreciation": number,
      "interest_expense": number,
      "nol_carryforward": number
    }}
    """

    response = client.chat.completions.create(
        model="gpt-5-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    content = response.choices[0].message.content

    import json
    return json.loads(content)