from fastapi import FastAPI
from pydantic import BaseModel
from uuid import UUID
from fastapi_sessions.frontends.implementations import SessionCookie, CookieParameters
from fastapi_sessions.session_verifier import SessionVerifier
from fastapi import HTTPException

app = FastAPI()
class SessionData(BaseModel):
    username: str
    password: str
    token: UUID

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