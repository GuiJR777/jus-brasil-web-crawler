from pydantic import BaseModel


class Parts(BaseModel):
    advogados_apelada: list[str] = []
    advogados_apelado: list[str] = []
    advogados_apelante: list[str] = []
    advogados_autor: list[str] = []
    advogados_reu: list[str] = []
    apelada: str = None
    apelado: str = None
    apelante: list[str] = []
    autor: str = None
    custos_legis: str = None
    reu: str = None
    terceiros: list[str] = []
    testemunhas: list[str] = []
    vitima: str = None
