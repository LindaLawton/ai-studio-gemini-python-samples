from dotenv import load_dotenv  # Import the load_dotenv function to load environment variables from a .env file

import google.generativeai as genai  # Import the Google Generative AI library

import os  # Import the os module for environment variable access

load_dotenv()  # Load environment variables from the .env file


def get_embedding_for(text, dimensionality: int = None):
    """
    Gets the embedding for the given text using the Google Generative AI API.

    Args:
        text: The text to generate an embedding for.
        dimensionality: The desired dimensionality of the embedding.
                        If None, the default dimensionality of the model is used.

    Returns:
        A dictionary containing the embedding and other information.
    """

    genai.configure(api_key=os.getenv("API_KEY"))  # Configure the API key from the environment variable

    return genai.embed_content(
        model=os.getenv("EMBEDDING_MODEL_NAME"),  # Use the embedding model name from the environment variable
        content=text,  # The text to embed
        task_type="retrieval_document",  # Specify the task type as document retrieval
        title="Embedding of single string",  # Set a title for the text (optional)
        output_dimensionality=dimensionality  # Set the desired output dimensionality (optional)
    )


if __name__ == "__main__":
    """
    Example usage of the get_embedding_for function.
    """
    result = get_embedding_for("What is the meaning of life?", 100)  # Get an embedding with dimensionality 100
    print(str(result['embedding'])[:50], '... TRIMMED')  # Print a truncated representation of the embedding
