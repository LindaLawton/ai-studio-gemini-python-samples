# ai-studio-gemini-python-samples

My Name is Linda Lawton I am a AI/ML GDE.  I have been working with AI studio Gemini since 2023 when it was called bard or Palm api.

I am slowing adding all of my samples here. 

# Library

This sample code uses the Python SDK to connect to AI studio gemini or gemini api.  

- [Documentation](https://ai.google.dev/gemini-api/docs/downloads)
- [pip](https://pypi.org/project/google-generativeai/)
- [generative-ai-python GitHub](https://github.com/google-gemini/generative-ai-python)

These samples are not intended to work with Vertex AI version of gemini.


# Support

I am here to help with these samples but if you need general help with Gemini there are sevral places you can go.

- [Build with Google AI forum](https://discuss.ai.google.dev/)
- [Discord google-dev-community](https://discord.com/invite/google-dev-community)  the Gemini-api channel.
- [StackOverflow Google-Gemini Tag](https://stackoverflow.com/questions/tagged/google-gemini)

# .env 

This file needs to contain your settings

## Your api key from [AI studio](https://aistudio.google.com/app/apikey)

    API_KEY=[Redacted]

## Any model that supports Audio, images, videos, and text

[Model List](https://ai.google.dev/gemini-api/docs/models/gemini) input must contain Audio, images, videos, and text.

    MODEL_NAME=gemini-1.5-flash-latest

## any model that supports embeddings

    EMBEDDING_MODEL_NAME=models/embedding-001

