from fastapi import APIRouter

from app import user_crud
from utils import RespApp
from schema import account, regisAccount


router = APIRouter()

@router.post("/regis-new-account")
async def RegistNewAccount(request: regisAccount):
    out_resp, e = await user_crud.create_new_account(request)
    if e != None:
        return RespApp(status="02", message=f"{e}", data=None)
    
    return RespApp(status="00", message="success", data=out_resp)
