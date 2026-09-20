from flask import Blueprint, render_template, request

mentor_bp = Blueprint("mentor", __name__)


@mentor_bp.route("/mentor", methods=["GET", "POST"])
def mentor_home():
    answer = None
    if request.method == "POST":
        question = request.form.get("question", "")
        answer = generate_local_mentor_response(question)
    return render_template("mentor.html", answer=answer)


def generate_local_mentor_response(question):
    q = question.lower()
    if "function" in q:
        return "A function is a reusable block of code that performs a task. It helps you organize code and avoid repetition. Example: def greet(name): return f'Hello {name}'"
    if "dictionary" in q:
        return "A dictionary stores data as key-value pairs. It is useful when you want to look up information by a meaningful name, like {'name': 'Alice', 'age': 23}."
    if "api" in q:
        return "An API allows one program to request data from another program over HTTP. In Python, the requests library is often used to get JSON responses."
    if "sqlite" in q:
        return "Use the sqlite3 module. Connect to a database file, create tables, and execute SQL statements to insert and read data."
    if "error" in q:
        return "Check the line mentioned in the error. Common causes are syntax mistakes, missing indentation, using a variable before it exists, or calling a function with the wrong arguments."
    if "learn" in q or "next" in q:
        return "Start by revising variables, conditions, loops, and functions. Then build small projects like a calculator, expense tracker, and to-do list before moving to files, SQLite, APIs, and web development."
    return "A good next step is to practice the concept with a small example, test it in the code editor, and then build a tiny project around it."
