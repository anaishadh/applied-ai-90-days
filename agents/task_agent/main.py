import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
API_URL = "https://api.openai.com/v1/responses"  # UPDATED endpoint

def get_task_breakdown(goal: str):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = f"""
You are a planning assistant.
Break the following goal into clear, actionable steps.
Return output as JSON with a list called "steps".

Goal: {goal}
"""

    payload = {
        "model": "gpt-4.1-mini",  # modern model
        "input": prompt,
        "temperature": 0.2
    }

    response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
    response.raise_for_status()
    data = response.json()

    # Extract text output from the response
    # The Responses API returns content in: data['output'][0]['content'][0]['text']
    result_text = data["output"][0]["content"][0]["text"]

    # Attempt to parse JSON if user returned valid JSON
    try:
        result_json = json.loads(result_text)
    except json.JSONDecodeError:
        # fallback if the response is not strict JSON
        result_json = {"steps": [step.strip() for step in result_text.split("\n") if step.strip()]}

    return result_json

if __name__ == "__main__":
    goal = input("Enter your goal: ")
    result = get_task_breakdown(goal)

    print("\n--- Task Breakdown ---")
    print(json.dumps(result, indent=2))

    with open("tasks.json", "w") as f:
        json.dump(result, f, indent=2)

