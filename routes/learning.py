from flask import Blueprint, render_template

learning_bp = Blueprint('learning', __name__, url_prefix='/learning')

@learning_bp.route('/lesson/<lesson_id>')
def view_lesson(lesson_id):
    # Mock lesson data for now
    lesson = {
        'id': lesson_id,
        'title': 'Python Variables',
        'concept': 'A variable allows you to store information.',
        'example': 'name = "John"\nage = 18',
        'exercise': 'Create a variable called city and store your city inside it.',
        'starting_code': '# Write your code here\n'
    }
    return render_template('lesson.html', lesson=lesson)
