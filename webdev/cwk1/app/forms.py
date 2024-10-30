from flask_wtf import FlaskForm
from wtforms import StringField,DateTimeField,TextAreaField,SelectField,SubmitField
from wtforms.validators import DataRequired, Length
from flask_wtf.csrf import CSRFProtect
from wtforms.fields import DateTimeLocalField
from flask import Flask

csrf = CSRFProtect()
app = Flask(__name__)
csrf.init_app(app)

class AssessmentForm(FlaskForm):
    assessment_title = StringField('Assessment Title', validators=[DataRequired(), Length(max = 50)])
    module_code = StringField('Module Code', validators=[DataRequired(), Length(max = 50)])
    deadline_date = DateTimeLocalField('Deadline Date', format='%Y-%m-%dT%H:%M', validators=[DataRequired()])
    short_description = TextAreaField('Short Description', validators=[DataRequired(), Length(max = 250)])
    completion_status = SelectField('Completion Status', choices=[('Incomplete', 'Incomplete'), ('Complete', 'Complete')], validators=[DataRequired()])
    submit = SubmitField('Submit')