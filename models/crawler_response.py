from pydantic import BaseModel

from models.process import Process


class CrawlerResponse(BaseModel):
    grau_1_data: Process | None = None
    grau_2_data: Process | None = None
