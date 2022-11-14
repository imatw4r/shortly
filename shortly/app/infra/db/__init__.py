from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from shortly.app.config import settings

SQLALCHEMY_ENGINE = create_engine(
    url=settings.ASYNC_POSTGRES_URI,
    pool_pre_ping=True,
    echo=settings.DB_ECHO_LOGS,
)

SQLALCHEMY_SESSION_FACTORY = sessionmaker(
    bind=SQLALCHEMY_ENGINE,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)
