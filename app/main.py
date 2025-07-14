from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import routes_funcionario
from app.api import routes_auth, routes_funcionario, routes_protegidas

app = FastAPI(
    title="API ONLINE",
    description="API CRUD funcionários",
    version="1.0.0"
)

# Habilita CORS para permitir requisições do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ou especifique o domínio do frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(routes_funcionario.router)
app.include_router(routes_auth.router)
app.include_router(routes_protegidas.router)

@app.get("/")
async def root():
    """API CRUD funcionários Online"""
    return {
        "message": "API CRUD funcionários Online",
        "version": "1.0.0",
        "status": "running"
    }