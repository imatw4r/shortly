from pydantic import BaseSettings, PostgresDsn, SecretStr
from functools import partial


class DatabaseSettings(BaseSettings):
    USER: str
    PASSWORD: SecretStr
    NAME: str
    HOST: str
    PORT: str = "5432"

    ECHO_LOGS: bool = True
    ENABLE_PROFILER: bool = True

    def _build_uri(self, schema: str) -> SecretStr:
        return SecretStr(
            value=partial(
                PostgresDsn.build,
                user=self.USER,
                password=self.PASSWORD.get_secret_value(),
                path=f"/{self.NAME}",
                port=self.PORT,
                host=self.HOST,
            )(scheme=schema)
        )

    def get_async_uri(self) -> SecretStr:
        return self._build_uri(schema="postgresql+asyncpg")

    def get_sync_uri(self) -> SecretStr:
        return self._build_uri(schema="postgresql+psycopg2")

    class Config:
        env_file = ".env"
        case_sensitive = True
        fields = {
            "USER": {"env": ["POSTGRES_USER"]},
            "PASSWORD": {"env": ["POSTGRES_PASSWORD"]},
            "NAME": {"env": ["POSTGRES_DB_NAME"]},
            "HOST": {"env": ["POSTGRES_HOST"]},
            "PORT": {"env": ["POSTGRES_PORT"]},
            "ECHO_LOGS": {"env": ["DB_ECHO_LOGS"]},
        }


class Settings(BaseSettings):
    db: DatabaseSettings = DatabaseSettings()

    class Config:
        env_file = ".env"
        case_sensitive = True
