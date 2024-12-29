"""
This script demonstrates how to use the Google Generative AI API to generate text responses.

1. **Import necessary libraries:**
   - `dotenv`: To load environment variables from a `.env` file.
   - `google.generativeai`: To interact with the Google Generative AI API.
   - `os`: To access environment variables.

2. **Load environment variables:**
   - `load_dotenv()`: Loads environment variables from the `.env` file.

3. **`get_response(text)` function:**
   - Configures the API key using the `genai.configure()` function.
   - Creates a `GenerativeModel` instance using the specified model name.
   - Generates content using the `generate_content()` method.
   - Returns the generated text response.

4. **Main execution block (`if __name__ == "__main__":`)**
   - Calls the `get_response()` function with the input text "hello gemini".
   - Prints the generated response.
"""

from dotenv import load_dotenv
import google.generativeai as genai
import os

load_dotenv()


def get_response(text) -> str:
    """
    Generates a text response using the specified Google Generative AI model.

    Args:
      text: The input text for the model.

    Returns:
      The generated text response.
    """
    genai.configure(api_key=os.getenv("API_KEY"))
    model = genai.GenerativeModel(os.getenv("TEXT_MODEL_NAME"))
    response = model.generate_content(text)
    return response.text


if __name__ == "__main__":
    response_text = get_response("hello gemini")
    print(response_text)
