from dotenv import load_dotenv
import google.generativeai as genai
import os
import base64
load_dotenv()


def get_response(prompt: str, image_paths: [str]) -> str:
    """
    Generates a text response using the specified Google Generative AI model.

    Args:
      prompt: The input text for the model.
      image_paths: The input image path for the model.

    Returns:
      The generated text response.
    """
    genai.configure(api_key=os.getenv("API_KEY"))
    model = genai.GenerativeModel(os.getenv("TEXT_IMAGE_MODEL_NAME"))

    image_data = []
    for image_path in image_paths:
        try:
            with open(image_path, "rb") as image_file:
                image_data.append({
                    'mime_type': 'image/jpeg',
                    'data': base64.b64encode(image_file.read()).decode('utf-8')
                })
        except FileNotFoundError:
            print(f"Error: Image file not found at {image_path}")

    try:
        response = model.generate_content(image_data + [prompt])
        return response.text
    except Exception as e:
        print(f"Error generating response: {e}")
        return None




if __name__ == "__main__":
    response_text = get_response("What do you see?", ["../test_data/bird_image_snickers_2024.jpg",
                                                      "../test_data/bread_image.jpg"])
    print(response_text)
