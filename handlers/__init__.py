from aiogram import Router
from . import user, admin
from .user import router as r
router = Router(name=__name__)
router.include_routers(r)