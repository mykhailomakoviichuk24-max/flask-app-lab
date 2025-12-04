from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    
    username = StringField('Ім\'я користувача', validators=[DataRequired(), Length(min=2, max=20)])
    
    
    password = PasswordField('Пароль', validators=[DataRequired()])
    
    
    remember = BooleanField('Запам\'ятати мене')
    
    submit = SubmitField('Увійти')