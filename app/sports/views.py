from flask import render_template, redirect, url_for, flash, request, abort
from flask_login import login_required, current_user
from app import db 
from . import sports_bp 
from .models import Event, Category 
from .forms import EventForm
from datetime import datetime


@sports_bp.route('/', methods=['GET'])
def event_list():
    query = request.args.get('q')
    if query:
        
        events = Event.query.filter(
            (Event.title.contains(query)) | (Event.description.contains(query))
        ).order_by(Event.date_time.desc()).all()
    else:
        
        events = Event.query.order_by(Event.date_time.desc()).all()
    
    return render_template('sports/event_list.html', events=events)


@sports_bp.route('/create', methods=['GET', 'POST'])
@login_required 
def create_event():
    form = EventForm()
    if form.validate_on_submit():
        event = Event(
            title=form.title.data,
            description=form.description.data,
            location=form.location.data,
            date_time=form.date_time.data,
            category=form.category.data,
            owner_id=current_user.id 
        )
        db.session.add(event)
        db.session.commit()
        flash('Подію успішно створено!', 'success')
        return redirect(url_for('sports.event_list'))
    
    return render_template('sports/event_form.html', form=form, title="Створити подію")


@sports_bp.route('/<int:id>')
def event_detail(id):
    event = Event.query.get_or_404(id)
    return render_template('sports/event_detail.html', event=event)


@sports_bp.route('/<int:id>/update', methods=['GET', 'POST'])
@login_required
def update_event(id):
    event = Event.query.get_or_404(id)
    
    
    if event.owner_id != current_user.id:
        abort(403) 
        
    form = EventForm(obj=event)
    
    if form.validate_on_submit():
        event.title = form.title.data
        event.description = form.description.data
        event.location = form.location.data
        event.date_time = form.date_time.data
        event.category = form.category.data
        
        db.session.commit()
        flash('Подію оновлено!', 'success')
        return redirect(url_for('sports.event_detail', id=event.id))
        
    return render_template('sports/event_form.html', form=form, title="Редагувати подію")


@sports_bp.route('/<int:id>/delete', methods=['POST'])
@login_required
def delete_event(id):
    event = Event.query.get_or_404(id)
    
    
    if event.owner_id != current_user.id:
        abort(403)
        
    db.session.delete(event)
    db.session.commit()
    flash('Подію видалено.', 'info')
    return redirect(url_for('sports.event_list'))