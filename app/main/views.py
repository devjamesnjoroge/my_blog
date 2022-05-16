from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import Post, User, Comment
from ..requests import get_Quote
from .. import db, photos
from .forms import CreateBlog, UpdateProfile, submitComment
from flask_login import current_user, login_required

@main.route('/')
def index():

    quote = get_Quote()

    posts = Post.query.all()

    admin = None

    if current_user.is_authenticated:

        if current_user._get_current_object().email == 'james.njoroge@student.moringaschool.com':

            admin = True

    title = 'JAYMMY-TECH'
    return render_template('index.html', title = title, quote = quote, admin = admin, posts = posts)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        user.save_user()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/post', methods = ['GET', 'POST'])
@login_required
def post():
    create_post = CreateBlog()

    if current_user._get_current_object().email != 'james.njoroge@student.moringaschool.com':
        abort(403)

    if create_post.validate_on_submit():

        new_post = Post(
            title = create_post.title.data,
            blog = create_post.blog.data,
            author = create_post.author.data,
            tags = create_post.tags.data,
            user_id = current_user._get_current_object().id
            )

        new_post.save_post()

        return redirect(url_for('main.index'))

    return render_template('post.html', create_post = create_post)

@main.route('/post/page/<int:post_id>')
def page(post_id):

    post = Post.query.filter_by(id = post_id).first()

    return render_template('page.html', post = post)


@main.route('/comment/<int:post_id>', methods = ['POST','GET'])
@login_required
def comments(post_id):
    form = submitComment()
    post = Post.query.get(post_id)
    all_comments = Comment.query.filter_by(post_id = post_id).all()
    if form.validate_on_submit():
        comment = form.comment.data
        post_id = post_id
        user_id = current_user._get_current_object().id
        new_comment = Comment(comment = comment,user_id = user_id,post_id = post_id)
        new_comment.save_c()
        return redirect(url_for('.comments', post_id = post_id))
    return render_template('comments.html', form =form, post = post,all_comments=all_comments)
