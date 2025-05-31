import google.generativeai as genai
from dotenv import load_dotenv

import os


def get_gemini_api_key():
    """
    Retrieves the Google Gemini API key from environment variables.
    """ 
    load_dotenv()
    genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
    model = genai.GenerativeModel('gemini-2.0-flash')
    return model


# response = model.generate_content('who are you model name')
# print(response.text)

