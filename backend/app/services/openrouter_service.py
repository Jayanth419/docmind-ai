import os

import requests
from dotenv import load_dotenv


load_dotenv()



class OpenRouterService:

    def __init__(self):
        api_key = os.getenv("OPENROUTER_API_KEY")

        if not api_key:
            raise ValueError(
                "OPENROUTER_API_KEY environment variable is not set"
            )

        self.api_key = api_key

    def generate_answer(
        self,
        prompt: str,
        response_format: str | None = None,
    ) -> str:

        payload = {
            "model": "google/gemma-4-26b-a4b-it",
            "messages": [
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        }

        if response_format == "json":
            payload["response_format"] = {
                "type": "json_object"
            }

        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
            json=payload,
            timeout=60,
        )

        response.raise_for_status()

        data = response.json()

        return data["choices"][0]["message"]["content"]