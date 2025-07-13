from fastapi import FastAPI
from app.api import routes_funcionario

app = FastAPI(
    title="API ONLINE",
    description="API CRUD funcionários",
    version="1.0.0"
)

app.include_router(routes_funcionario.router)

@app.get("/")
async def root():
    """API CRUD funcionários Online"""
    return {
        "message": "API CRUD funcionários Online",
        "version": "1.0.0",
        "status": "running"
    }