from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.models import Assessments
from .forms import AssessmentForm

@app.route('/')
def home():
    return render_template('home.html', title="Home")

@app.route('/create_assessment', methods=['GET', 'POST'])
def create_assessment():
    form = AssessmentForm()
    if form.validate_on_submit():
        flash('Success!')
        new_assessment = Assessments(
            title=form.assessment_title.data,
            moduleCode=form.module_code.data,
            deadline=form.deadline_date.data,
            description=form.short_description.data,
            status= form.completion_status.data == "Complete"
        )
        db.session.add(new_assessment)
        db.session.commit()
        return redirect(url_for('view'))
    return render_template('create.html', form=form)

@app.route('/view')
def view():
    show_completed = request.args.get('show_completed') == 'true'
    if show_completed:
        assessments = Assessments.query.filter(Assessments.status == True).all()
    else:
        assessments = Assessments.query.all()
    form = AssessmentForm()
    return render_template('view.html', form = form,assessments=assessments)

@app.route('/Edit_assessment<int:assessment_id>', methods=['GET', 'POST'])
def Edit_assessment(assessment_id):
    assessment = Assessments.query.get(assessment_id)
    form = AssessmentForm(object = assessment)
    if request.method == 'GET':
        form.assessment_title.data = assessment.title
        form.module_code.data = assessment.moduleCode
        form.deadline_date.data = assessment.deadline
        form.short_description.data = assessment.description
        form.completion_status.data = 'Complete' if assessment.status else 'Incomplete'
        
    if form.validate_on_submit():
        assessment.title = form.assessment_title.data
        assessment.moduleCode = form.module_code.data
        assessment.deadline = form.deadline_date.data
        assessment.description = form.short_description.data
        print (form.completion_status.data == "Complete")
        assessment.completion_status = (form.completion_status.data == 'Complete')
        db.session.commit()
        flash('Assessment updated successfully!')
        
        return redirect(url_for('view'))
    return render_template('edit.html', form=form,)

@app.route('/delete_assessment/<int:assessment_id>', methods=['POST'])
def delete_assessment(assessment_id):
    assessment = Assessments.query.get_or_404(assessment_id)
    form = AssessmentForm()

    db.session.delete(assessment)
    db.session.commit()
    
    flash('Assessment deleted successfully!')
    return redirect(url_for('view'))