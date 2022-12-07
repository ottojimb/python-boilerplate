import logging
import os
from functools import lru_cache

from pydantic import BaseSettings

logger = logging.getLogger(__name__)


class GlobalConfig(BaseSettings):
    TITLE: str = "Project Title"

    API_KEY: str = os.getenv("TMDB_API_KEY", "")


@lru_cache()
def get_configuration() -> GlobalConfig:
    return GlobalConfig()


settings = get_configuration()
