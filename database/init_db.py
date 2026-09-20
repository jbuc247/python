from database.database import get_connection
from data.lessons import LESSONS
from data.quizzes import QUIZZES
from data.challenges import CHALLENGES
from data.projects import PROJECTS


def bootstrap_default_data():
    conn = get_connection()
    try:
        for lesson in LESSONS:
            conn.execute(
                """
                INSERT OR IGNORE INTO lessons (
                    slug, title, category, difficulty, description, content, summary, order_index
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    lesson["slug"],
                    lesson["title"],
                    lesson["category"],
                    lesson["difficulty"],
                    lesson["description"],
                    lesson["content"],
                    lesson["summary"],
                    lesson["order_index"],
                ),
            )

        for quiz in QUIZZES:
            conn.execute(
                """
                INSERT OR IGNORE INTO quizzes (
                    slug, title, topic, difficulty, description, total_questions
                ) VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    quiz["slug"],
                    quiz["title"],
                    quiz["topic"],
                    quiz["difficulty"],
                    quiz["description"],
                    quiz["total_questions"],
                ),
            )

            quiz_id = conn.execute(
                "SELECT id FROM quizzes WHERE slug = ?",
                (quiz["slug"],),
            ).fetchone()
            if quiz_id:
                for q in quiz["questions"]:
                    conn.execute(
                        """
                        INSERT OR IGNORE INTO quiz_questions (
                            quiz_id, question, options, correct_answer, explanation, question_type
                        ) VALUES (?, ?, ?, ?, ?, ?)
                        """,
                        (
                            quiz_id[0],
                            q["question"],
                            " | ".join(q["options"]),
                            q["correct_answer"],
                            q["explanation"],
                            q.get("question_type", "multiple_choice"),
                        ),
                    )

        for challenge in CHALLENGES:
            conn.execute(
                """
                INSERT OR IGNORE INTO daily_challenges (
                    title, difficulty, description, requirements, hints, solution, challenge_date
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    challenge["title"],
                    challenge["difficulty"],
                    challenge["description"],
                    challenge["requirements"],
                    challenge["hints"],
                    challenge["solution"],
                    challenge.get("challenge_date", "2026-01-01"),
                ),
            )

        for project in PROJECTS:
            conn.execute(
                """
                INSERT OR IGNORE INTO projects (
                    slug, name, difficulty, category, description, skills, requirements,
                    learning_objectives, hints, test_cases, extension_ideas, expected_behavior, solution
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    project["slug"],
                    project["name"],
                    project["difficulty"],
                    project["category"],
                    project["description"],
                    project["skills"],
                    project["requirements"],
                    project["learning_objectives"],
                    project["hints"],
                    project["test_cases"],
                    project["extension_ideas"],
                    project["expected_behavior"],
                    project["solution"],
                ),
            )

        conn.commit()
    finally:
        conn.close()
