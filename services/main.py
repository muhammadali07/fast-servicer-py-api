import uvicorn as uv

from fastapi import FastAPI

from api import api_router

app = FastAPI()

app.include_router(api_router, prefix="/api/v1")

if __name__ == "__main__":
    uv.run(app, host="0.0.0.0") 