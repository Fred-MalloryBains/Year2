from flask_wtf import FlaskForm
from wtforms import StringField,DateTimeField,TextAreaField,SelectField,SubmitField
from wtforms.validators import DataRequired, Length
from flask_wtf.csrf import CSRFProtect
from wtforms.fields import DateTimeLocalField
from flask import Flask

# csrf protection
csrf = CSRFProtect()
app = Flask(__name__)
csrf.init_app(app)


# created a form class for the assessment form that matches the database
# the form has the same fields as the database table and same data types
# has error checking to make sure data is present and of appropiate format
class AssessmentForm(FlaskForm):
    assessment_title = StringField('Assessment Title', validators=[DataRequired(), Length(max = 50)])
    module_code = StringField('Module Code', validators=[DataRequired(), Length(max = 50)])
    deadline_date = DateTimeLocalField('Deadline Date', format='%Y-%m-%dT%H:%M', validators=[DataRequired()])
    short_description = TextAreaField('Short Description', validators=[DataRequired(), Length(max = 500)])
    completion_status = SelectField('Completion Status', choices=[('Incomplete', 'Incomplete'), ('Complete', 'Complete')], validators=[DataRequired()])
    submit = SubmitField('Submit')