from fastapi import FastAPI

from fastapi import UploadFile, File
from fastapi.responses import JSONResponse
from http import HTTPStatus
from docx import Document
from io import BytesIO

app = FastAPI(docs_url="/docs",)


@app.get("/test")
async def read_test():
    return {"message": "This is a test endpoint"}


@app.post('/upload_docx', responses={HTTPStatus.BAD_REQUEST: {"model": dict}})
async def upload_docx(doc_file: UploadFile = File(...)) -> dict:
    try:
        # Read the uploaded file as bytes
        contents = await doc_file.read()

        # Load the document using python-docx
        doc = Document(BytesIO(contents))

        # Print the first 20 lines
        for i in range(min(20, len(doc.paragraphs))):
            print(doc.paragraphs[i].text)

        return JSONResponse(
            status_code=HTTPStatus.CREATED,
            content={"success": True},
        )
    except Exception as e:
        return JSONResponse(
            status_code=HTTPStatus.BAD_REQUEST,
            content={"error": str(e)},
        )
