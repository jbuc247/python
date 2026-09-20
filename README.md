# Python Learning Lab

Python Learning Lab is a browser-based learning platform built for local use in Termux/Android and desktop browsers. It helps a beginner move from Python fundamentals to advanced software development through lessons, quizzes, daily challenges, coding exercises, projects, and progress tracking.

## Features

- Personalized onboarding assessment
- Structured learning roadmap from beginner to advanced
- Interactive lesson pages with exercises and code checkpoints
- Coding challenge runner with timeouts and output capture
- Quiz and project scoring tools
- 100-project library grouped by skill level
- Personal project workspace with file editing and execution
- Browser-based terminal for local commands
- XP, streaks, and weak-topic tracking
- Responsive design for mobile and desktop browsers

## Requirements

- Python 3.10+
- Flask
- SQLite (built into Python)

## Termux installation

```bash
pkg update
pkg install python
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Then open the browser at:

```text
http://localhost:5000
```

## Local development

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

## Project structure

```text
python_learning_lab/
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── database/
│   ├── __init__.py
│   ├── database.py
│   └── init_db.py
├── routes/
│   ├── __init__.py
│   ├── dashboard.py
│   ├── lessons.py
│   ├── quizzes.py
│   ├── challenges.py
│   ├── projects.py
│   ├── terminal.py
│   ├── progress.py
│   ├── settings.py
│   └── mentor.py
├── services/
│   ├── __init__.py
│   ├── code_runner.py
│   ├── evaluator.py
│   ├── progress.py
│   └── recommendations.py
├── data/
│   ├── lessons.py
│   ├── quizzes.py
│   ├── challenges.py
│   └── projects.py
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── assessment.html
│   ├── lessons.html
│   ├── lesson_detail.html
│   ├── quizzes.html
│   ├── challenges.html
│   ├── project_library.html
│   ├── project_detail.html
│   ├── workspace.html
│   ├── terminal.html
│   ├── progress.html
│   ├── settings.html
│   └── mentor.html
├── static/
│   ├── css/style.css
│   └── js/app.js
├── user_projects/
└── database/learning_lab.db
```

## Code execution and security

This application executes user-submitted Python code and shell commands in a controlled local environment. It captures stdout and stderr, applies a timeout, and blocks common dangerous patterns such as shell injection sequences and broad destructive commands.

Important notes:

- By default the app binds to 127.0.0.1.
- Do not expose the application on a public network unless you understand the risks.
- The browser terminal is intentionally limited and should not be treated as unrestricted shell access.
- This is a local learning environment, not a multi-user sandbox.

## Troubleshooting

- If the browser shows a connection error, ensure the Flask app is running in the same device and the port is open.
- If Python packages are missing, run `pip install -r requirements.txt`.
- If the database is corrupted or missing, delete the SQLite file and restart the app to recreate it.

## Extending the app

- Add new lessons in `data/lessons.py`
- Add quizzes in `data/quizzes.py`
- Add new project entries in `data/projects.py`
- Add new challenge definitions in `data/challenges.py`
