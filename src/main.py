from fastapi import FastAPI

app = FastAPI()


@app.get("/test")
async def read_test():
    return {"message": "This is a test endpoint"}
