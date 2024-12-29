from dotenv import load_dotenv
import google.generativeai as genai
import os
import PIL.Image
load_dotenv()


def get_response(text, image_path) -> str:
    """
    Generates a text response using the specified Google Generative AI model.

    Args:
      text: The input text for the model.
      image_path: The input image path for the model.

    Returns:
      The generated text response.
    """
    genai.configure(api_key=os.getenv("API_KEY"))
    model = genai.GenerativeModel(os.getenv("TEXT_IMAGE_MODEL_NAME"))

    image_data = PIL.Image.open(image_path)
    response = model.generate_content([text, image_data])
    return response.text


if __name__ == "__main__":
    response_text = get_response("What do you see?", "../test_data/bird_image_snickers_2024.jpg")
    print(response_text)
