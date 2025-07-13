from fastapi import FastAPI
from app.api import routes_funcionario

app = FastAPI()

app.include_router(routes_funcionario.router)
