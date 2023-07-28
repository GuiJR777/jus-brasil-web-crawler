from pydantic import BaseModel


class Parts(BaseModel):
    autor: str = None
    advogados_autor: list[str] = []
    reu: str = None
    advogados_reu: list[str] = []
