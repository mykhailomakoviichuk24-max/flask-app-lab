from flask import Flask
from loguru import logger
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import MetaData
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# 1. Налаштування Naming Convention
metadata = MetaData(naming_convention={
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
})

# 2. Створення додатка
app = Flask(__name__)
app.config.from_pyfile('../config.py')

# 3. Налаштування БД
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../app.db'
db = SQLAlchemy(app, metadata=metadata)
migrate = Migrate(app, db)

# 4. Налаштування авторизації
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'info'

# 5. Логування
logger.add("logs/contact_form.log", rotation="10 MB", retention="1 month", level="INFO", 
           format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}")

# 6. Реєстрація Blueprint-ів
from app.auth import auth_bp
app.register_blueprint(auth_bp)

from app.post import post_bp
app.register_blueprint(post_bp)

# 7. Імпорт моделей (для міграцій)
from app.auth import models
from app.post import models
from app.products import models  # <--- ОСЬ ЦЕЙ РЯДОК БУВ ПРОПУЩЕНИЙ!

# 8. Імпорт views
from app import views