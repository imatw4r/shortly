from pydantic import BaseSettings, PostgresDsn, SecretStr


class DatabaseSettings(BaseSettings):
    USER: str
    PASSWORD: SecretStr
    NAME: str
    HOST: str
    PORT: str = "5432"

    ECHO_LOGS: bool = True
    ENABLE_PROFILER: bool = True

    def get_async_uri(self) -> SecretStr:
        uri = PostgresDsn.build(
            scheme="postgresql+asyncpg",
            user=self.USER,
            password=self.PASSWORD.get_secret_value(),
            path=f"/{self.NAME}",
            port=self.PORT,
            host=self.HOST,
        )
        return SecretStr(value=uri)

    def get_sync_uri(self) -> SecretStr:
        async_uri = self.get_sync_uri().get_secret_value()
        return SecretStr(value=async_uri.replace("postgresql+asyncpg", "postgresql+psycopg2"))

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
