from db.database import engine, Base, DBSession
from models import User
from sqlalchemy.future import select


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def drop_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


async def get_user_by_tgid(tg_id: int) -> User | None:
    db_session = DBSession()
    query = select(User).where(User.user_id == str(tg_id))
    result = await db_session.execute(query)
    usr = result.scalar_one_or_none()
    await db_session.close()
    return usr
