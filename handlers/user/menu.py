from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
router = Router(name=__name__)
# router.message.middleware()


@router.message(F.text, Command("hello"))
async def hello_msg(message: Message):
    await message.answer(f'Hello, {message.from_user.id}')