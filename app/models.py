from flask_login import UserMixin
from app import db, login_manager
from sqlalchemy.orm import relationship

# Функція для завантаження користувача (потрібна Flask-Login)
@login_manager.user_loader
def load_user(user_id):
    # Припускаємо, що модель користувача називається User
    return db.session.get(User, int(user_id))

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False) # Пароль (хешований)
    
    # Зв'язок: Користувач може мати багато подій (вимога №10)
    events = relationship('Event', backref='owner', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"