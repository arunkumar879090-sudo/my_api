from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "My first deployed API"}

@app.get("/square")
def square_number(n: int):
    return {"result": n * n}