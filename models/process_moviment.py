from pydantic import BaseModel


class ProcessMoviment(BaseModel):
    data: str
    details: str
