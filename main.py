from fastapi import FastAPI
from routes import routes
from auth import auth

app = FastAPI()
app.include_router(routes.router)
app.include_router(auth.auth_router)

@app.get('/')
async def root():
    return {'message': 'Hello World'}