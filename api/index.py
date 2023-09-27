from fastapi import FastAPI, Response, Depends
from pydantic import BaseModel
from uuid import UUID, uuid4
from fastapi_sessions.frontends.implementations import SessionCookie, CookieParameters
from fastapi_sessions.backends.implementations import InMemoryBackend
from fastapi_sessions.session_verifier import SessionVerifier
from fastapi import HTTPException

app = FastAPI()
class SessionData(BaseModel):
    token: UUID
    username: str
    password: str

class BasicVerifier(SessionVerifier[UUID, SessionData]):
    def __init__(
        self,
        *,
        identifier: str,
        auto_error: bool,
        backend: InMemoryBackend[UUID, SessionData],
        auth_http_exception: HTTPException,
    ):
        self._identifier = identifier
        self._auto_error = auto_error
        self._backend = backend
        self._auth_http_exception = auth_http_exception

    @property
    def identifier(self):
        return self._identifier

    @property
    def backend(self):
        return self._backend

    @property
    def auto_error(self):
        return self._auto_error

    @property
    def auth_http_exception(self):
        return self._auth_http_exception

    def verify_session(self, model: SessionData) -> bool:
        """If the session exists, it is valid"""
        if not model:
            print("model not found!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            return False
        else:
            print("model found!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            return True

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
    # verify if the user is already logged in
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