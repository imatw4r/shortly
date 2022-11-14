from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from shortly.app.config import settings

SQLALCHEMY_ENGINE = create_engine(
    url=settings.db.get_async_uri().get_secret_value(),
    pool_pre_ping=True,
    echo=settings.db.ECHO_LOGS,
)

SQLALCHEMY_SESSION_FACTORY = sessionmaker(
    bind=SQLALCHEMY_ENGINE,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)
