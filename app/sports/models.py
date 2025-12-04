from app import db  
from datetime import datetime
from sqlalchemy.orm import relationship


class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    
    events = relationship('Event', backref='category', lazy=True)

    def __repr__(self):
        return self.name


class Event(db.Model):
    __tablename__ = 'event'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
   
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    
    
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'<Event {self.title}>'