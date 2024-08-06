from fastapi import FastAPI
from .routes.routes import router
from .auth.auth import auth_router

app = FastAPI()
app.include_router(router)
app.include_router(auth_router)

@app.get('/')
async def root():
    return {'message': 'Hello World'}