import asyncio
from app.db.session import engine
from app.db.base import Base

async def test():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        print("✅ Tabelas criadas com sucesso!")

asyncio.run(test())
    