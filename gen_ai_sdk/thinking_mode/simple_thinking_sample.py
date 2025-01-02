import os

from google import genai
from dotenv import load_dotenv
load_dotenv()


def get_response(text) -> str:
    """
    Generates a thinking response using the specified Google Generative AI model.

    Args:
      text: The input text for the model.

    Returns:
      The generated text response.
    """
    client = genai.Client(api_key=os.getenv("API_KEY"), http_options={'api_version':'v1alpha'})
    response = client.models.generate_content(
        model='gemini-2.0-flash-thinking-exp', contents=text
    )
    return response.candidates[0].content.parts


if __name__ == "__main__":
    response_parts = get_response("Explain how Oauth2 works in simple terms.")
    for part in response_parts:
        if part.thought:
            print(f"Model Thought:\n{part.text}\n")
        else:
            print(f"\nModel Response:\n{part.text}\n")



