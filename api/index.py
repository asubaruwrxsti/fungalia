from fastapi import FastAPI

app = FastAPI()

@app.get("/api/python")
def hello_world():
    return {"message": "Hello World"}

@app.post("/api/login")
def login():
    return {
        "status": True,
        "message": "Login Success",
        "user": {
            "id": 1,
            "name": "John Doe",
        },
    }