from aiogram import Router

from . import start, menu

router = Router(name=__name__)
router.include_routers(start.router, menu.router)