from sqlalchemy.orm import Mapped, mapped_column
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from vdmap.db.models.base import Base


class Users(Base, UserMixin):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str]
    password: Mapped[str]

    def set_password(self, password):
        self.__setattr__("password", generate_password_hash(password))

    def check_password(self, password):
        return check_password_hash(self.__getattribute__("password"), password)

    def __repr__(self):
        return f"User(id={self.id},email={self.email})"

