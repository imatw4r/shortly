from typing import Any

from pydantic import BaseSettings, PostgresDsn, SecretStr, validator


class Settings(BaseSettings):
    # Postgres connection settings

    POSTGRES_USER: str
    POSTGRES_PASSWORD: SecretStr
    POSTGRES_DB_NAME: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str = "5432"

    ASYNC_POSTGRES_URI: SecretStr = ""  # use this URI to async connection

    @validator("ASYNC_POSTGRES_URI", pre=True)
    def get_async_psql_uri(cls, async_psql_uri: str, values: dict[str, Any]) -> SecretStr:
        async_uri = PostgresDsn.build(
            scheme="postgresql+asyncpg",
            user=values["POSTGRES_USER"],
            password=values["POSTGRES_PASSWORD"].get_secret_value(),
            path=f"/{values['POSTGRES_DB_NAME']}",
            port=values["POSTGRES_PORT"],
            host=values["POSTGRES_HOST"],
        )
        return SecretStr(value=async_uri)

    SYNC_POSTGRES_URI: SecretStr = ""  # use this URI to alembic migration

    @validator("SYNC_POSTGRES_URI", pre=True)
    def get_sync_psql_uri(cls, sync_psql_uri: str, values: dict[str, str]) -> SecretStr:
        async_uri = values["ASYNC_POSTGRES_URI"]
        sync_uri = async_uri.replace("postgresql+asyncpg", "postgresql+psycopg2")
        return SecretStr(value=sync_uri)

    # Postgres logs settings

    DB_ECHO_LOGS: bool = True

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
