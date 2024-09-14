# LinkedIn PDF to HTML Resume Generator

This application takes a LinkedIn PDF download and generates an HTML resume using OpenAI's API.

## Project Structure

```
resume_generator/
│
├── app/
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
3. It then uses OpenAI's API to generate an HTML resume based on the extracted text.
4. The generated HTML resume is returned to the user.

## Technologies used

- FastAPI: For creating the web application
- Jinja2: For HTML templating
- PyPDF2: For extracting text from PDF files
- OpenAI API: For generating the HTML resume
- Vercel: For deployment

## Setup and Deployment

1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run locally: `uvicorn app.main:app --reload`
4. Deploy to Vercel:
    - Install Vercel CLI: `npm i -g vercel`
    - Run `vercel` in the project directory

## Approach

1. Created a FastAPI application with endpoints for file upload and HTML generation.
2. Implemented PDF text extraction using PyPDF2.
3. Integrated OpenAI's API for HTML resume generation.
4. Set up deployment configuration for Vercel.
5. Ensured secure handling of the OpenAI API key by taking it as user input.
6. Structured the project for better organization and maintainability.

## Challenges and Solutions

- Challenge: Handling PDF uploads securely.
  Solution: Used FastAPI's built-in file upload handling and securely saved files temporarily.

- Challenge: Integrating OpenAI API securely.
  Solution: Took the API key as user input instead of hardcoding it.

- Challenge: Deploying a FastAPI application on Vercel.
  Solution: Created a custom `vercel.json` configuration file to specify build and route settings.

- Challenge: Improving code organization.
  Solution: Structured the project into separate directories for application code, templates, and static files.

## Future Improvements

- Add more styling options for the generated HTML resume.
- Implement caching to reduce API calls for repeated conversions.
- Add error handling and validation for better user experience.
- Implement user authentication for enhanced security.

## Deployed Application

[Insert the link to your deployed application here]#   r e s u m e _ g e n e r a t o r  
 