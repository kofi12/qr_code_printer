from fastapi import FastAPI
from .routes.qr_routes import qr_router
from .routes.auth_route import auth_router

app = FastAPI()
app.include_router(qr_router)
app.include_router(auth_router)

@app.get('/')
async def root():
    return {'message': 'Hello World'}