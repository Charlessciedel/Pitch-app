from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import Required, Length


class PostForm(FlaskForm):
    CATEGORIES=[('PICK-UP PITCH', 'PICK-UP PITCH'), ('BIASHARA PITCH', 'BIASHARA PITCH'), ('PREMIUM PITCH', 'PREMIUM PITCH'), ('MANENO PITCH', 'MANENO PITCH')]
    category=SelectField("Categories",choices=CATEGORIES)
    post=TextAreaField("Post",validators=[Required()])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    comment = TextAreaField('')
    submit = SubmitField('Submit')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.', validators=[Required()])
    submit = SubmitField('Submit')