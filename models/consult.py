from pydantic import BaseModel


class Consult(BaseModel):
    numero_processo: str
