from flask_wtf import FlaskForm
from wtforms import StringField,DateField,TextAreaField,SelectField,SubmitField
from wtforms.validators import DataRequired

class AssessmentForm(FlaskForm):
    assessment_title = StringField('Assessment Title', validators=[DataRequired()])
    module_code = StringField('Module Code', validators=[DataRequired()])
    deadline_date = DateField('Deadline Date', format='%Y-%m-%d', validators=[DataRequired()])
    short_description = TextAreaField('Short Description', validators=[DataRequired()])
    completion_status = SelectField('Completion Status', choices=[('Incomplete', 'Incomplete'), ('Complete', 'Complete')], validators=[DataRequired()])
    submit = SubmitField('Submit')