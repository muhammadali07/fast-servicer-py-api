from models import user_models

async def registNewAccount(data):
    paramInsert = user_models.Users(
        email = data.email,
        password= data.password,
        role = data.role
    )

    return data
