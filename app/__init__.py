from flask import Flask
from loguru import logger
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import MetaData


metadata = MetaData(naming_convention={
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
})


app = Flask(__name__)
app.config.from_pyfile('../config.py')


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../app.db'
db = SQLAlchemy(app, metadata=metadata)
migrate = Migrate(app, db)


logger.add("logs/contact_form.log", rotation="10 MB", retention="1 month", level="INFO", 
           format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}")


from app.auth.views import auth_bp
app.register_blueprint(auth_bp)

from app.post import post_bp
app.register_blueprint(post_bp)


from app.products import models
from app.auth import models
from app.post import models

from app import views