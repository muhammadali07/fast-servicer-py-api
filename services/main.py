import uvicorn as uv

from fastapi import FastAPI

from api import api_router
from utils import engine, settings, Base

app = FastAPI(
    title=settings.PROJECT_NAME,
    docs_url="/api/docs"
)

app.include_router(api_router, prefix="/api/v1")


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    uv.run(app, host="0.0.0.0") 