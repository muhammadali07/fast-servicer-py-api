from datastore import user_datastore
from schema import regisAccount

async def create_new_account(data: regisAccount):
    try:    
        if data.email == "" :
            raise Exception("email harus di isi")
        
        if data.password == "" :
            raise Exception("password harus di isi")
    
        if data.role == "" :
            raise Exception("role harus di isi")

        resCreateAccount, e = user_datastore.registNewAccount(data)
        if e != None:
            raise Exception(f"{e}")
        
        return resCreateAccount, None


    except Exception as e:
        return data, e
