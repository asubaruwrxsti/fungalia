class SessionData(BaseModel):
    token: UUID
    username: str
    password: str