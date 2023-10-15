from fastapi import FastAPI, Response, Depends
from pydantic import BaseModel
from uuid import UUID, uuid4
from fastapi_sessions.frontends.implementations import SessionCookie, CookieParameters
from fastapi_sessions.backends.implementations import InMemoryBackend
from fastapi_sessions.session_verifier import SessionVerifier
from fastapi import HTTPException

import BasicVerifier
import SessionData

app = FastAPI()
backend = InMemoryBackend[UUID, SessionData]()
verifier = BasicVerifier(
    identifier="general_verifier",
    auto_error=True,
    backend=backend,
    auth_http_exception=HTTPException(status_code=403, detail="invalid session"),
)

cookie_params = CookieParameters()
cookie = SessionCookie(
    cookie_name="cookie",
    identifier="general_verifier",
    auto_error=True,
    secret_key="DONOTUSE",
    cookie_params=cookie_params,
)

@app.get("/api/python")
def hello_world():
    return {"message": "Hello World"}

@app.post("/api/login")
async def login(response: Response):
    if BasicVerifier.verify_session(verifier, SessionData):
        return {
            "status": True,
            "message": "Already logged in",
            "user": {
                "id": 1,
                "name": "John Doe",
            },
        }

    session = uuid4()
    data = SessionData(token=session, username="admin", password="admin")

    await backend.create(session, data)
    cookie.attach_to_response(response, session)

    return {
        "status": True,
        "message": "Login Success",
        "user": {
            "id": 1,
            "name": "John Doe",
        },
    }

@app.get("/api/whoami", dependencies=[Depends(cookie)])
async def whoami(session_data: SessionData = Depends(verifier)):
    return session_data