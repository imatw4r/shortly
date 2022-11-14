from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from shortly.app.config import settings

from .base import metadata

ENGINE = create_engine(
    url=settings.db.get_async_uri().get_secret_value(),
    pool_pre_ping=True,
    echo=settings.db.ECHO_LOGS,
)

SESSION_FACTORY = sessionmaker(
    bind=ENGINE,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)
