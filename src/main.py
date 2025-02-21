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

        print("type(doc):", type(doc))

        return JSONResponse(
            status_code=HTTPStatus.CREATED,
            content={"success": True},
        )
    except Exception as e:
        return JSONResponse(
            status_code=HTTPStatus.BAD_REQUEST,
            content={"error": str(e)},
        )


# db test
import psycopg2

# Database configuration
DATABASE_CONFIG = {
    "user": "py_docx_fastapi",
    "password": "py_docx_fastapi",
    "host": "pg_db",  # or your host
    "port": 5432,
    "database": "py_docx_fastapi",
}


def get_connection():
    return psycopg2.connect(**DATABASE_CONFIG)


@app.on_event("startup")
async def startup_event():
    app.db_connection = get_connection()

    app.db_connection.autocommit = True
    cursor = app.db_connection.cursor()

    # Optionally create a table for testing purposes
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS test_table (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100)
        );
    """)

    cursor.close()
    app.db_connection.close()


@app.on_event("shutdown")
async def shutdown_event():
    app.db_connection.close()
