from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+psycopg://py_docx_fastapi:py_docx_fastapi@py_docx_fastapi_postgres:5432/py_docx_fastapi"

# Create an async engine with connection pooling
engine = create_async_engine(
    DATABASE_URL,
    echo=True,
    pool_size=10,          # Set the size of the pool
    max_overflow=5         # Allow up to 5 additional connections beyond pool_size
)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_db():
    async with async_session_maker() as session:
        yield session
