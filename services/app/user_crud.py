from sqlalchemy.ext.asyncio import AsyncSession
from datastore import user_datastore
from schema import regisAccount

async def create_new_account(data: regisAccount, db_session:AsyncSession):
    async with db_session as session:
        try:  
            print(data)  
            if data.email == "" :
                raise Exception("email harus di isi")
            
            if data.password == "" :
                raise Exception("password harus di isi")
        
            if data.role == "" :
                raise Exception("role harus di isi")

            resCreateAccount, e = await user_datastore.registNewAccount(data, session)
            if e != None:
                raise Exception(f"{e}")
            
            await session.commit()

            return resCreateAccount, None


        except Exception as e:
            return data, e
