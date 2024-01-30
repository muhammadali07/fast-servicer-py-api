from models import user_models

async def registNewAccount(data, session):
    try:
        paramsInsert = user_models.Users(
        email = data.email,
        password= data.password,
        role = data.role
        )

        session.add(paramsInsert)
        return data, None
    except Exception as e:
        return data, e
    

