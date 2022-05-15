from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User
from ..requests import get_Quote
from .. import db
from .forms import UpdateProfile
from flask_login import login_required

@main.route('/')
def index():

    quote = get_Quote()

    title = 'JAYMMY-TECH'
    return render_template('index.html', title = title, quote = quote)

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