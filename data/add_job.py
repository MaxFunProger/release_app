from flask import Flask
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, BooleanField, DateField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import EmailField
from flask import redirect
from datetime import datetime


class JobForm(FlaskForm):
    team_leader = IntegerField('Team Leader Id', validators=[DataRequired()])
    job = StringField('Title', validators=[DataRequired()])
    work_size = IntegerField('Need hours to do', validators=[DataRequired()])
    collaborators = StringField('Involved colonists id', validators=[DataRequired()])
    start_date = DateField('Start date', validators=[DataRequired()], default=datetime.now())
    end_date = DateField('End date', validators=[DataRequired()], default=datetime.now())
    is_finished = BooleanField('Is job finished?')
    submit = SubmitField('Submit')
