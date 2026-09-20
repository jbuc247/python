import re


def evaluate_project(project, user_code: str):
    score = 0
    total = 10
    checks = []

    if "def " in user_code or "if __name__" in user_code:
        score += 2
        checks.append("Structure looks reasonable.")
    if "input(" in user_code or "print(" in user_code:
        score += 2
        checks.append("Program includes user interaction or output.")
    if "return " in user_code or "def " in user_code:
        score += 2
        checks.append("Core function logic appears present.")
    if "try:" in user_code or "except" in user_code:
        score += 2
        checks.append("Error handling is partially considered.")
    if "sqlite3" in user_code or "json" in user_code or "csv" in user_code:
        score += 2
        checks.append("Relevant data handling is used.")

    final_score = min(score, total)
    return {
        "score": final_score,
        "total": total,
        "checks": checks,
        "summary": "Your submission was reviewed against the project requirements and code quality markers.",
    }


def get_quiz_result(user_answers, questions):
    correct = 0
    wrong = 0
    explanations = []
    for index, question in enumerate(questions):
        answer = user_answers.get(str(index), "")
        if str(answer).strip().lower() == str(question["correct_answer"]).strip().lower():
            correct += 1
        else:
            wrong += 1
            explanations.append({
                "question": question["question"],
                "correct_answer": question["correct_answer"],
                "explanation": question["explanation"],
            })
    total = len(questions)
    percentage = round((correct / total) * 100, 2) if total else 0
    return {"correct": correct, "wrong": wrong, "total": total, "percentage": percentage, "explanations": explanations}


def evaluate_submission(execution_result: dict, requirements: list) -> dict:
    """
    Evaluates a user's code execution result against a set of requirements.
    """
    if not execution_result.get("success"):
        return {
            "score": 0,
            "max_score": len(requirements),
            "passed": False,
            "feedback": ["Your code encountered an error. Please fix the error and try again."],
        }

    score = 0
    feedback = []
    stdout = execution_result.get("stdout", "")

    for req in requirements:
        if req["type"] == "output_contains":
            if req["value"] in stdout:
                score += 1
            else:
                feedback.append(f"Expected output to contain '{req['value']}'")
        elif req["type"] == "output_matches_regex":
            if re.search(req["value"], stdout):
                score += 1
            else:
                feedback.append(f"Output did not match expected pattern: {req['value']}")

    max_score = len(requirements)
    passed = score == max_score

    if passed:
        feedback = ["Excellent! Your code met all requirements."]

    return {
        "score": score,
        "max_score": max_score,
        "passed": passed,
        "feedback": feedback,
    }
