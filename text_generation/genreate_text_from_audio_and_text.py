import pathlib

from dotenv import load_dotenv
import google.generativeai as genai
import os
import PIL.Image
load_dotenv()

def get_response(prompt, audio_path) -> str:
    """
    Generates a text response using the specified Google Generative AI model.

    Args:
      prompt: The input text for the model.
      audio_path: The input image path for the model.

    Returns:
      The generated text response.
    """
    genai.configure(api_key=os.getenv("API_KEY"))
    model = genai.GenerativeModel(os.getenv("TEXT_IMAGE_MODEL_NAME"))

    audio_data = {
        "mime_type": "audio/mp3",
        "data": pathlib.Path(audio_path).read_bytes()
    }
    response = model.generate_content([prompt, audio_data])
    return response.text


if __name__ == "__main__":
    response_text = get_response("Please describe this audio. Tell me what it could be", "../test_data/Ship Bell.mp3")
    print(response_text)
