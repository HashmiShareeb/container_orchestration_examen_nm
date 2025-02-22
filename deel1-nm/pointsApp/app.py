from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://student:examen@database:5432/points'
db = SQLAlchemy(app)


class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    grade = db.Column(db.Integer, default=0)


@app.route('/')
def index():
    students = Student.query.all()
    return render_template('index.html', students=students)


@app.route('/create', methods=['POST'])
def create_student():
    name = request.form.get('name')
    student = Student(name=name)
    db.session.add(student)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/assign/<int:student_id>', methods=['POST'])
def assign_grade(student_id):
    grade = int(request.form.get('grade'))
    student = db.session.get(Student, student_id)
    student.grade = grade
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    # Within the application context
    with app.app_context():
        # Create tables
        db.create_all()

    # Run the application
    app.run(debug=True, host='127.0.0.0', port=5000)
