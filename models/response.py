from pydantic import BaseModel
from models.crawler_response import CrawlerResponse


class ApiResponse(BaseModel):
    status: str = "ok"
    message: str | None = None
    data: CrawlerResponse | None = None
