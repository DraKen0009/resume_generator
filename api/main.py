from fastapi import FastAPI, File, UploadFile, Form, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os
from api.utils import extract_text_from_pdf, generate_html_resume

app = FastAPI()

# Mount the templates directory
templates = Jinja2Templates(directory="templates")

# Mount the static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.post("/upload")
async def upload_file(file: UploadFile = File(...), openai_key: str = Form(None), gemini_key: str = Form(None)):
    if openai_key == "" and gemini_key == "":
        raise HTTPException(status_code=400, detail="Either Gemini or OpenAI key must be provided")
    if openai_key != "" and gemini_key != "":
        raise HTTPException(status_code=400, detail="Please provide only one API key (either Gemini or OpenAI)")
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")
    if file.size > 524288:  # 512 KB in bytes
        raise HTTPException(status_code=413, detail="File size exceeds 512 KB")

    try:
        # Save the uploaded PDF file
        temp_file_path = os.path.join('/tmp', file.filename)

        # Save the uploaded PDF file
        with open(temp_file_path, "wb") as buffer:
            buffer.write(await file.read())

        # Extract text from PDF
        pdf_text = extract_text_from_pdf(temp_file_path)

        # Generate HTML resume using the provided API
        html_resume = generate_html_resume(pdf_text, openai_key, gemini_key)

        return HTMLResponse(content=html_resume, status_code=200)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        # Clean up: remove the temporary PDF file
        if os.path.exists(file.filename):
            os.remove(file.filename)


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
