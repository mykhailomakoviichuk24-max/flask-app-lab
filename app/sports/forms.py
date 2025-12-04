from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateTimeLocalField, SubmitField
from wtforms.validators import DataRequired, Length
from wtforms_sqlalchemy.fields import QuerySelectField
from .models import Category 


def choice_query():
    return Category.query.all()

class EventForm(FlaskForm):
    title = StringField('Назва події', validators=[DataRequired(), Length(min=3, max=100)])
    description = TextAreaField('Опис', validators=[DataRequired()])
    location = StringField('Місце проведення', validators=[DataRequired()])
    
    date_time = DateTimeLocalField('Дата та час', format='%Y-%m-%dT%H:%M', validators=[DataRequired()])
    
    
    category = QuerySelectField(
        'Категорія спорту', 
        query_factory=choice_query, 
        allow_blank=False, 
        get_label='name' 
    )
    
    submit = SubmitField('Зберегти')