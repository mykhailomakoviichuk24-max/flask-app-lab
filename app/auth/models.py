from app import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String

class User(db.Model):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(100), nullable=False)

    
    posts: Mapped[list["Post"]] = relationship("Post", back_populates="author")

    def __repr__(self):
        return f'<User {self.username}>'