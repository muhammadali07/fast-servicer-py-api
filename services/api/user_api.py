from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app import user_crud
from utils import RespApp, get_async_session
from schema import account, regisAccount



router = APIRouter()

@router.post("/regis-new-account")
async def RegistNewAccount(
    request: regisAccount,
    db: AsyncSession = Depends(get_async_session)
    ):
    out_resp, e = await user_crud.create_new_account(request, db)
    if e != None:
        return RespApp(status="02", message=f"{e}", data=None)
    
    return RespApp(status="00", message="success", data=out_resp)

@router.get("/get-list-new-account")
async def GetListNewAccount(
    page: int = 0,
    limit: int = 10,
    keyword: str = None,
    db: AsyncSession = Depends(get_async_session)
    ):
    out_resp, e = await user_crud.get_list_new_account(page, limit, keyword, db)
    if e != None:
        return RespApp(status="02", message=f"{e}", data=None)
    
    return RespApp(status="00", message="success", data=out_resp)
