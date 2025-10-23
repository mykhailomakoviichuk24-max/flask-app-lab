from flask import Flask


app = Flask(__name__)


app.config.from_pyfile('../config.py')


from app.auth.views import auth_bp


app.register_blueprint(auth_bp)


from app import views