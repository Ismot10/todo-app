<<<<<<< HEAD
import os

=======
>>>>>>> c2a363565545af7a2d65ece1739857f971f7c6c2
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# Initialize Flask app
app = Flask(__name__)
<<<<<<< HEAD
app.config['SECRET_KEY'] = '90c8005869ae1d043dc5ccfd274d3436'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///D:/todo-app/instance/todo.db'

=======
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/todo.db'
>>>>>>> c2a363565545af7a2d65ece1739857f971f7c6c2
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)
<<<<<<< HEAD
 

# Get the absolute path to the todo.db file inside the instance folder
db_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'instance', 'todo.db')

# Update the database URI with the absolute path
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'

=======
>>>>>>> c2a363565545af7a2d65ece1739857f971f7c6c2

# Create a form for adding tasks
class TaskForm(FlaskForm):
    task = StringField('Task', validators=[DataRequired()])
    submit = SubmitField('Add Task')

# Create a database model for tasks
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)

# Home route - Display To-Do List
@app.route('/', methods=['GET', 'POST'])
def index():
    form = TaskForm()
    tasks = Task.query.all()
    if form.validate_on_submit():
        new_task = Task(content=form.task.data)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('index.html', form=form, tasks=tasks)

# Delete task route
@app.route('/delete/<int:task_id>')
def delete(task_id):
    task_to_delete = Task.query.get_or_404(task_id)
    db.session.delete(task_to_delete)
    db.session.commit()
    return redirect(url_for('index'))

<<<<<<< HEAD
# Create tables and run the app within an application context
if __name__ == '__main__':
    with app.app_context():  # Ensure the app context is active
        db.create_all()  # Create tables in the database
    app.run(debug=True)

=======
# Start the app
if __name__ == "__main__":
    db.create_all()  # Create tables in the database
    app.run(debug=True)
>>>>>>> c2a363565545af7a2d65ece1739857f971f7c6c2
