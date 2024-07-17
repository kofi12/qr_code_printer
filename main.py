from fastapi import FastAPI
from routes import routes
app = FastAPI()
app.include_router(routes.router)

@app.get('/')
async def root():
    return {'message': 'Hello World'}