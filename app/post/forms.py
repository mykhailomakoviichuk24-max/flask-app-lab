from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SelectField, SelectMultipleField, SubmitField
from wtforms.validators import DataRequired
from app.auth.models import User
from app.post.models import Tag

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    text = TextAreaField('Content', validators=[DataRequired()])
    type = SelectField('Type', choices=[('News', 'News'), ('Publication', 'Publication'), ('Other', 'Other')])
    enabled = BooleanField('Enabled', default=True)
    
    
    author_id = SelectField('Author', coerce=int, validators=[DataRequired()])
    
   
    tags = SelectMultipleField('Tags', coerce=int)
    
    submit = SubmitField('Create Post')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.author_id.choices = [(u.id, u.username) for u in User.query.order_by(User.username).all()]
        
        
        self.tags.choices = [(t.id, t.name) for t in Tag.query.order_by(Tag.name).all()]