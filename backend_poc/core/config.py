import os
from typing import List, ClassVar

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

ENV: str = ""


class Configs(BaseSettings):
    # base
    ENV: str = os.getenv("ENV", "dev")
    API: str = "/api"
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "backend-poc-api"
    ENV_DATABASE_MAPPER: dict = {
        "prod": "backend-poc",
        "stage": "stage-backend-poc",
        "dev": "postgres",
        "test": "test-backend-poc",
    }
    DB_ENGINE_MAPPER: dict = {
        "postgresql": "postgresql",
        "mysql": "mysql+pymysql",
    }

    PROJECT_ROOT: str = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    # date
    DATETIME_FORMAT: str = "%Y-%m-%dT%H:%M:%S"
    DATE_FORMAT: str = "%Y-%m-%d"

    # auth
    SECRET_KEY: str = os.getenv("SECRET_KEY", "")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 30  # 60 minutes * 24 hours * 30 days = 30 days

    # CORS
    BACKEND_CORS_ORIGINS: List[str] = ["*"]

    # database
    DB: str = os.getenv("DB", "postgresql")
    DB_USER: str = os.getenv("DB_USER", "postgres")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "Postgres2024!")
    DB_HOST: str = os.getenv("DB_HOST", "localhost")
    DB_PORT: str = os.getenv("DB_PORT", "5432")
    DB_ENGINE: str = DB_ENGINE_MAPPER.get(DB, "postgresql")

    DATABASE_URI_FORMAT: str = "{db_engine}://{user}:{password}@{host}:{port}/{database}"

    DATABASE_URI: ClassVar[str]
    PAGE: ClassVar[str]
    PAGE_SIZE: ClassVar[str]
    ORDERING: ClassVar[str]

    DATABASE_URI = "{db_engine}://{user}:{password}@{host}:{port}/{database}".format(
        db_engine=DB_ENGINE,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
        database=ENV_DATABASE_MAPPER[ENV],
    )

    # find query
    PAGE = 1
    PAGE_SIZE = 20
    ORDERING = "-id"

    class Config:
        case_sensitive = True


class TestConfigs(Configs):
    ENV: str = "test"


configs = Configs()

if ENV == "prod":
    pass
elif ENV == "stage":
    pass
elif ENV == "test":
    setting = TestConfigs()