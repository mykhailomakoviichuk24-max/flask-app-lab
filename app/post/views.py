from flask import render_template, redirect, url_for, flash
from . import post_bp
from .forms import PostForm
from .models import Post, Tag
from app import db

@post_bp.route('/create', methods=['GET', 'POST'])
def create_post():
    form = PostForm()
    
    if form.validate_on_submit():
        
        post = Post(
            title=form.title.data,
            text=form.text.data,
            type=form.type.data,
            enabled=form.enabled.data,
            user_id=form.author_id.data
        )
        
        
        for tag_id in form.tags.data:
            tag = db.session.get(Tag, tag_id)
            if tag:
                post.tags.append(tag) 
        
        db.session.add(post)
        db.session.commit()
        
        flash('Post created successfully!', 'success')
        return redirect(url_for('post.post_detail', id=post.id))
        
    return render_template('posts/create_post.html', form=form)

@post_bp.route('/<int:id>')
def post_detail(id):
    post = db.session.get(Post, id)
    return render_template('posts/post_detail.html', post=post)