import uvicorn
from controllers.crawler import CrawlersController
from services.cache import RedisCache
from views.api import ConsultApi
from configs import REDIS_PASS, REDIS_PORT, REDIS_URL


cache_service = RedisCache(REDIS_URL, REDIS_PASS, REDIS_PORT)
crawlers_controller = CrawlersController()

api_app = ConsultApi(cache_service, crawlers_controller).app

if __name__ == "__main__":
    uvicorn.run(api_app, host="localhost", port=8000)
