from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

import settings

# PostgresSQL Client
engine = create_async_engine(
    f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}/{settings.POSTGRES_DB}",
    echo=True,
)
SessionLocal = async_sessionmaker(
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    bind=engine,
)


def get_session() -> AsyncSession:
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.expunge_all()
        db.close()
