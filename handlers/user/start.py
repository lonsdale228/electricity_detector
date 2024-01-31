from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.methods import TelegramMethod
from aiogram.types import Message

from db.database import DBSession
from db.utils import get_user_by_tgid
from middlewares.register_check import RegisterCheck
from models import User
db_session = DBSession()
router = Router(name=__name__)
router.message.middleware(RegisterCheck())
@router.message(CommandStart())
async def start_command(message: Message) -> TelegramMethod:
    # user_id = message.from_user.id
    # usr = await get_user_by_tgid(user_id)
    #
    # if not usr:
    #     user = User()
    #     user.user_id = user_id
    #     db_session.add(user)
    #     await db_session.commit()
    #     await db_session.close()
    #     return message.answer(text="Hello, u are new!")
    # else:
    #     return message.answer(text="Hi again!")
    # await message.answer('Hi!')
    ...