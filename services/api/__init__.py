from fastapi import APIRouter

from .testing import *
from .user_api import *

api_router = APIRouter()

api_router.include_router(testing.router, prefix='/greeting', tags=['Greeting'])
api_router.include_router(user_api.router, prefix='/user', tags=['User Management'])

