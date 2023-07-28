from os import getenv

from dotenv import load_dotenv

load_dotenv(override=True)

REDIS_URL = getenv("REDIS_URL", "localhost")
REDIS_PORT = int(getenv("REDIS_PORT", 6379))
REDIS_PASS = getenv("REDIS_PASS", None)
REDIS_TTL = int(getenv("REDIS_TTL", 1)) * 3600  # hours
