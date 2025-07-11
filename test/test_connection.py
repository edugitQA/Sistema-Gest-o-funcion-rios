import asyncio
from app.db.session import engine

async def test_connection():
    async with engine.begin() as conn:
        await conn.run_sync(lambda _: print("conexão bem-sucedida"))

asyncio.run(test_connection())
