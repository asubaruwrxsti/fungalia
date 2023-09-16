from fastapi import FastAPI

app = FastAPI()

@app.get("/api/python")
def hello_world():
    return {"message": "Hello World"}

@app.post("/api/login")
def login():
    return {"stauts": True, "message": "Login Success"}