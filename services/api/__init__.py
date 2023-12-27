from fastapi import APIRouter

from .testing import *

api_router = APIRouter()

api_router.include_router(testing.router, prefix='/greeting', tags=['Greeting'])

