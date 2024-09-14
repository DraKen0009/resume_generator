import re

import PyPDF2
import openai
import google.generativeai as genai
from openai import AuthenticationError, APIError
from google.api_core import exceptions as google_exceptions


def extract_text_from_pdf(file_path):
    try:
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
        return text
    except Exception as e:
        raise ValueError(f"Error extracting text from PDF: {str(e)}")


def generate_html_resume(pdf_text, openai_key=None, gemini_key=None):
    if openai_key:
        return generate_with_openai(pdf_text, openai_key)
    elif gemini_key:
        return generate_with_gemini(pdf_text, gemini_key)
    else:
        raise ValueError("No valid API key provided")


def validate_openai_key(api_key):
    try:
        openai.api_key = api_key
        # Make a simple API call to check if the key is valid
        openai.Engine.list()
        return True
    except AuthenticationError:
        raise ValueError("Invalid OpenAI API key")
    except Exception as e:
        raise ValueError(f"Error validating OpenAI API key: {str(e)}")


def generate_with_openai(pdf_text, openai_key):
    try:
        validate_openai_key(openai_key)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                 "content": "You are a helpful assistant that generates HTML resumes from text input."},
                {"role": "user", "content": f"Generate an HTML resume from the following text:\n\n{pdf_text}"}
            ]
        )
        return response.choices[0].message['content']
    except AuthenticationError:
        raise ValueError("Invalid OpenAI API key")
    except APIError as e:
        raise ValueError(f"OpenAI API error: {str(e)}")
    except Exception as e:
        raise ValueError(f"Error generating resume with OpenAI: {str(e)}")


def validate_gemini_key(api_key):
    try:
        genai.configure(api_key=api_key)
        # Make a simple API call to check if the key is valid
        model = genai.GenerativeModel('gemini-1.5-flash')
        model.generate_content("Test")
        return True
    except google_exceptions.PermissionDenied:
        raise ValueError("Invalid Gemini API key")
    except Exception as e:
        raise ValueError(f"Error validating Gemini API key: {str(e)}")


def generate_with_gemini(pdf_text, gemini_key):
    try:
        validate_gemini_key(gemini_key)
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(
            f"Generate an HTML resume from the following text. Do not include ```html tags or any other markdown formatting, just the raw HTML:\n\n{pdf_text}"
        )

        # Extract the HTML content
        html_content = response.text

        # Remove ```html and ``` if they're still present
        html_content = re.sub(r'```html\s*', '', html_content)
        html_content = re.sub(r'```\s*$', '', html_content)

        # Ensure the content starts with <!DOCTYPE html>
        if not html_content.strip().startswith('<!DOCTYPE html>'):
            html_content = f"<!DOCTYPE html>\n{html_content}"

        # Ensure there's a <html> tag
        if '<html>' not in html_content:
            html_content = re.sub(r'(<!DOCTYPE html>\s*)', r'\1<html>\n', html_content)
            html_content += '\n</html>'

        # Ensure there's a <head> and <body> tag
        if '<head>' not in html_content:
            html_content = re.sub(r'(<html>\s*)', r'\1<head><title>Resume</title></head>\n', html_content)
        if '<body>' not in html_content:
            html_content = re.sub(r'(</head>\s*)', r'\1<body>\n', html_content)
            html_content = re.sub(r'(</html>)', r'</body>\n\1', html_content)

        return html_content.strip()
    except google_exceptions.PermissionDenied:
        raise ValueError("Invalid Gemini API key")
    except Exception as e:
        raise ValueError(f"Error generating resume with Gemini: {str(e)}")
