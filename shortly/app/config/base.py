from typing import Any

from pydantic import BaseSettings, PostgresDsn, SecretStr, validator


class Settings(BaseSettings):
    # Postgres connection settings

    POSTGRES_USER: str
    POSTGRES_PASSWORD: SecretStr
    POSTGRES_DB_NAME: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str = "5432"

    ASYNC_POSTGRES_URI: str = ""  # use this URI to async connection

    @validator("ASYNC_PSQL_URI", always=True)
    def get_async_psql_uri(cls, async_psql_uri: str, values: dict[str, Any]) -> str:
        return PostgresDsn.build(
            scheme="postgresql+asyncpg",
            user=values["POSTGRES_USER"],
            password=values["POSTGRES_PASSWORD"].get_secret_value(),
            path=f"/{values['POSTGRES_DB_NAME']}",
            port=values["POSTGRES_PORT"],
            host=values["POSTGRES_HOST"],
        )

    SYNC_POSTGRES_URI: str = ""  # use this URI to alembic migration

    @validator("SYNC_PSQL_URI", always=True)
    def get_sync_psql_uri(cls, sync_psql_uri: str, values: dict[str, str]) -> str:
        async_uri = values["ASYNC_POSTGRES_URI"]
        return async_uri.replace("postgresql+asyncpg", "postgresql+psycopg2")

    # Postgres logs settings

    DB_ECHO_LOGS: bool = True

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
