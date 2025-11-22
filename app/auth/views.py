from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, current_user, logout_user, login_required
from app import db, bcrypt
from . import auth_bp
from .forms import RegistrationForm, LoginForm
from .models import User


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    
    if current_user.is_authenticated:
        return redirect(url_for('auth.account'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        
        user = User(username=form.username.data, email=form.email.data)
        
        user.set_password(form.password.data)
        
        db.session.add(user)
        db.session.commit()
        
        flash('Ваш акаунт створено! Тепер ви можете увійти.', 'success')
        return redirect(url_for('auth.login'))
        
    return render_template('auth/register.html', title='Register', form=form)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('auth.account'))
        
    form = LoginForm()
    if form.validate_on_submit():
        
        user = User.query.filter_by(email=form.email.data).first()
        
        
        if user and user.check_password(form.password.data):
            
            login_user(user, remember=form.remember.data)
            
            
            next_page = request.args.get('next')
            
            flash('Ви успішно увійшли в систему!', 'success')
            return redirect(next_page) if next_page else redirect(url_for('auth.account'))
        else:
            flash('Вхід не вдався. Перевірте email та пароль.', 'danger')
            
    return render_template('auth/login.html', title='Login', form=form)


@auth_bp.route('/logout')
def logout():
    logout_user()
    flash('Ви вийшли з системи.', 'info')
    return redirect(url_for('auth.login'))


@auth_bp.route('/account')
@login_required
def account():
    return render_template('auth/account.html', title='Account')


@auth_bp.route('/users')
@login_required
def all_users():
    users = User.query.all()
    count = len(users)
    return render_template('auth/users.html', users=users, count=count)