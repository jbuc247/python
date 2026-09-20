import re

def evaluate_submission(execution_result: dict, requirements: list) -> dict:
    """
    Evaluates a user's code execution result against a set of requirements.
    
    Args:
        execution_result: dict containing 'stdout', 'stderr', and 'success'
        requirements: list of dicts, e.g., [{'type': 'output_contains', 'value': 'Hello World'}]
        
    Returns:
        A dict with score and feedback.
    """
    if not execution_result['success']:
        return {
            'score': 0,
            'max_score': len(requirements),
            'passed': False,
            'feedback': ['Your code encountered an error. Please fix the error and try again.']
        }
        
    score = 0
    feedback = []
    
    stdout = execution_result.get('stdout', '')
    
    for req in requirements:
        if req['type'] == 'output_contains':
            if req['value'] in stdout:
                score += 1
            else:
                feedback.append(f"Expected output to contain '{req['value']}'")
        elif req['type'] == 'output_matches_regex':
            if re.search(req['value'], stdout):
                score += 1
            else:
                feedback.append(f"Output did not match expected pattern: {req['value']}")
        # Additional requirement types can be added here (e.g., AST inspection)
        
    max_score = len(requirements)
    passed = score == max_score
    
    if passed:
        feedback = ['Excellent! Your code met all requirements.']
        
    return {
        'score': score,
        'max_score': max_score,
        'passed': passed,
        'feedback': feedback
    }
