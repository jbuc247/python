from flask import Blueprint, render_template, request, jsonify

quizzes_bp = Blueprint('quizzes', __name__, url_prefix='/quizzes')

@quizzes_bp.route('/')
def index():
    # Mock list of quizzes
    quizzes = [
        {'id': 1, 'title': 'Python Basics', 'difficulty': 'Beginner', 'questions': 10},
        {'id': 2, 'title': 'Functions & Scope', 'difficulty': 'Intermediate', 'questions': 8},
        {'id': 3, 'title': 'Data Structures', 'difficulty': 'Intermediate', 'questions': 12},
    ]
    return render_template('quizzes.html', quizzes=quizzes)

@quizzes_bp.route('/<int:quiz_id>')
def view_quiz(quiz_id):
    # Mock quiz data
    quiz = {
        'id': quiz_id,
        'title': 'Python Basics',
        'questions': [
            {
                'id': 1,
                'type': 'multiple_choice',
                'question': 'Which of the following is a mutable data type in Python?',
                'options': ['Tuple', 'String', 'List', 'Integer'],
                'answer': 'List'
            },
            {
                'id': 2,
                'type': 'multiple_choice',
                'question': 'What is the output of print(2 ** 3)?',
                'options': ['6', '8', '9', 'Error'],
                'answer': '8'
            }
        ]
    }
    return render_template('quiz_take.html', quiz=quiz)

@quizzes_bp.route('/<int:quiz_id>/submit', methods=['POST'])
def submit_quiz(quiz_id):
    data = request.get_json()
    answers = data.get('answers', {})
    
    # In a real app, fetch the correct answers from DB
    correct_answers = {
        '1': 'List',
        '2': '8'
    }
    
    score = 0
    feedback = {}
    
    for q_id, answer in answers.items():
        if correct_answers.get(q_id) == answer:
            score += 1
            feedback[q_id] = {'correct': True, 'explanation': 'Correct!'}
        else:
            feedback[q_id] = {'correct': False, 'explanation': f'Incorrect. The correct answer is {correct_answers.get(q_id)}.'}
            
    return jsonify({
        'score': score,
        'total': len(correct_answers),
        'feedback': feedback
    })
