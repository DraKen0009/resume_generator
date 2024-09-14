# LinkedIn PDF to HTML Resume Generator

This application takes a LinkedIn PDF download and generates an HTML resume using OpenAI's/GEMINI's API.

## Project Structure

```
resume_generator/
│
├── api/
│   ├── __init__.py
│   ├── main.py
│   └── utils.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── styles.css
│
├── requirements.txt
├── vercel.json
└── README.md
```

## How it works

1. The user uploads a LinkedIn PDF file and provides their OpenAI API key.
2. The application extracts text from the PDF.
3. It then uses OpenAI's/GEMINI's API to generate an HTML resume based on the extracted text.
4. The generated HTML resume is returned to the user.

## Technologies used

- FastAPI: For creating the web application
- Jinja2: For HTML templating
- PyPDF2: For extracting text from PDF files
- OpenAI API: For generating the HTML resume
- GEMINI API: For generating the HTML resume
- Vercel: For deployment

## Setup and Deployment

1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run locally: `uvicorn app.main:app --reload`


## Approach

1. Created a FastAPI application with endpoints for file upload and HTML generation.
2. Implemented PDF text extraction using PyPDF2.
3. Integrated OpenAI's/GEMINI's  API for HTML resume generation.
4. Set up deployment configuration for Vercel.
5. Ensured secure handling of the OpenAI/GEMINI API key by taking it as user input.
6. Structured the project for better organization and maintainability.

## NOTE
> - Tested only with Gemini Api key. ( Bcz I don't have OpenAI's API key)
> - Timeout is 60 second
> - Document size limit is 512Kb
> - Document should only be a PDF file