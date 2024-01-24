from pydantic import BaseModel

class account(BaseModel):
    username : str = "muhalibalhtiar@gmail.com"
    password : str = "1234zzxx"
    secretKey : str = "xxxx"

class regisAccount(BaseModel):
    email : str = "muhalibalhtiar@gmail.com"
    password : str = "1234zzxx"
    role : str = "supervisor"