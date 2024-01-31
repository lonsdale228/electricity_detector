from aiogram.utils.link import create_tg_link
from sqlalchemy import Integer, Column, Boolean, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from db.database import Base


class Admins(Base):
    __tablename__ = 'admins'

    id: Mapped = Column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped = Column(String, nullable=False)


class User(Base):
    __tablename__ = 'users'

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id = mapped_column(String, nullable=False, unique=True)
    addresses = relationship("Address", back_populates="user")
    is_admin = mapped_column(Boolean, default=False)

    @property
    def url(self) -> str:
        return create_tg_link("user", id=self.id)

class Address(Base):
    __tablename__ = 'addresses'

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    location = mapped_column(String)
    name = mapped_column(String)
    user_id = mapped_column(String, ForeignKey('users.user_id'))
    is_public = mapped_column(Boolean, default=False)
    is_active = mapped_column(Boolean, default=True)
    notify = mapped_column(Boolean, default=False)
    user = relationship("User", back_populates="addresses")

class ApiUsers(Base):
    __tablename__ = 'api_users'

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    api_key = mapped_column(String, nullable=False)
