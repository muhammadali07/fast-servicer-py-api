from fastapi import APIRouter

from app import testing_crud
from pkg import RespApp


router = APIRouter()

@router.get("/")
async def greeting():
    out_resp = await testing_crud.Greeting()
    return RespApp(status="00", message="success", data=out_resp)

@router.get("/greeting-for-all")
async def GreetingForAll():
    out_resp = await testing_crud.GreetingForAll()
    return RespApp(status="00", message="success", data=out_resp)