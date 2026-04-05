from pydantic import BaseModel

class NLQRequest(BaseModel):
    query: str