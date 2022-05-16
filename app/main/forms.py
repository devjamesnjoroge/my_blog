from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField
from wtforms.validators import DataRequired

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [DataRequired()])
    submit = SubmitField('Submit')

class CreateBlog(FlaskForm):

    title = StringField('Blog Title', validators=[DataRequired()])
    author = StringField('Name to appear on blog', validators=[DataRequired()])
    blog = TextAreaField('Your Blog', validators=[DataRequired()])
    tags = StringField('Hashtags for blog topics', validators=[DataRequired()])

    submit = SubmitField('Upload Blog')


class submitComment(FlaskForm):
    comment = TextAreaField('Leave a message',validators=[DataRequired()])
    submit = SubmitField('Comment')