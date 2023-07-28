from pydantic import BaseModel

from models.parts import Parts
from models.process_moviment import ProcessMoviment


class Process(BaseModel):
    classe: str
    area: str
    assunto: str
    data_de_distribuicao: str
    juiz: str
    valor_da_acao: float
    partes_do_processo: Parts
    lista_das_movimentacoes: list[ProcessMoviment] | list[str]
