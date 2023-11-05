from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    return "Hola Mundo"


@app.get("/url")
async def url():
    return {"url": "https://mouredev.com/python"}
