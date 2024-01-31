import asyncio
from db.utils import init_db
from db.database import session_maker
from models import Admins
from loader import dp, bot
async def main():
    await init_db()
    db_session = session_maker()

    record = Admins()
    record.user_id = "3174658711"

    db_session.add(record)
    await db_session.commit()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, session_maker=session_maker)
    ...


if __name__ == '__main__':
    asyncio.run(main())
