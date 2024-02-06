from models import user_models
from sqlalchemy import select, or_, and_

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
    
async def getListNewAccount(page, limit, keyword, session):
    try:
        terms = []
        if keyword not in (None, ""):
            terms.append(
                or_(
                    (user_models.Users.email.ilike(f"%{keyword.lower()}%")),
                    (user_models.Users.role.ilike(f"%{keyword.lower()}%"))
                )
            )

        offset = (page*limit)
        sql = select(user_models.Users).filter(and_(*(terms))).offset(offset).limit(limit)
        proxy_rows = await session.execute(sql)
        data = proxy_rows.scalars().all()
        
        return data, None
    except Exception as e:
        return data, e
    

