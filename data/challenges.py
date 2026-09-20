CHALLENGES = [
    {
        "title": "Build a Simple Calculator",
        "difficulty": "Beginner",
        "description": "Create a calculator that asks for two numbers and an operation.",
        "requirements": "\n1. Accept two numbers.\n2. Accept +, -, *, /.\n3. Print the result.\n4. Handle invalid input gracefully.",
        "hints": "Use input(), float(), and if/elif to choose the operation.",
        "solution": "def calculator():\n    num1 = float(input('First number: '))\n    op = input('Operator: ')\n    num2 = float(input('Second number: '))\n    if op == '+':\n        print(num1 + num2)\n    elif op == '-':\n        print(num1 - num2)\n    elif op == '*':\n        print(num1 * num2)\n    elif op == '/':\n        print(num1 / num2)\n    else:\n        print('Invalid operator')\n",
        "challenge_date": "2026-09-20"
    },
    {
        "title": "Number Guessing Game",
        "difficulty": "Beginner",
        "description": "Create a game where the player guesses a random number.",
        "requirements": "\n1. Pick a random number between 1 and 10.\n2. Ask the player to guess.\n3. Tell them if the guess is too high or too low.\n4. Repeat until correct.",
        "hints": "Use random.randint() and a while loop.",
        "solution": "import random\nsecret = random.randint(1, 10)\nwhile True:\n    guess = int(input('Guess a number 1-10: '))\n    if guess < secret:\n        print('Too low')\n    elif guess > secret:\n        print('Too high')\n    else:\n        print('Correct!')\n        break\n",
        "challenge_date": "2026-09-21"
    }
]
