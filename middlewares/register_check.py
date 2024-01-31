from typing import Any, Callable, Union

from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from sqlalchemy.engine import ScalarResult
from models import User


class RegisterCheck(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable,
            event: Union[Message, CallbackQuery],
            data: dict
    ) -> Any:
        session_maker: sessionmaker = data['session_maker']

        async with session_maker() as session:
            async with session.begin():
                session: AsyncSession
                result: ScalarResult = await session.execute(select(User).where(User.user_id == str(event.from_user.id)))
                user: User = result.one_or_none()

                if user:
                    if isinstance(event, Message):
                        await event.answer('Already registered!')
                    pass
                else:
                    user = User(user_id=str(event.from_user.id))
                    await session.merge(user)
                    if isinstance(event, Message):
                        await event.answer('Hello new user!')
                    else:
                        await event.message.answer('Hello new user!')
        return await handler(event, data)
