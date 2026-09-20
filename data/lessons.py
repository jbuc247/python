LESSONS = [
    {
        "slug": "python-variables",
        "title": "Python Variables",
        "category": "Python Basics",
        "difficulty": "Beginner",
        "description": "Store and reuse values in your programs.",
        "summary": "Learn how variables work in Python.",
        "order_index": 1,
        "content": """
        <h3>Python Variables</h3>
        <p>A variable is a container for storing data. You create a variable by assigning a value to a name.</p>
        <pre>name = "Alice"
age = 22
print(name)
print(age)</pre>
        <p>Why it matters: variables let you store user input, calculations, and project data.</p>
        <p>Practice: create a variable called city and store your city name in it.</p>
        """
    },
    {
        "slug": "python-data-types",
        "title": "Data Types",
        "category": "Python Basics",
        "difficulty": "Beginner",
        "description": "Understand strings, integers, floats, booleans, and lists.",
        "summary": "Learn the main Python data types.",
        "order_index": 2,
        "content": """
        <h3>Data Types</h3>
        <p>Python has built-in data types like strings, integers, floats, booleans, and lists.</p>
        <pre>name = "Sam"
score = 95
pi = 3.14
is_ready = True
numbers = [1, 2, 3]</pre>
        <p>Why it matters: different values behave differently in programs.</p>
        <p>Exercise: store a boolean called finished and print it.</p>
        """
    },
    {
        "slug": "python-conditions",
        "title": "Conditions",
        "category": "Python Basics",
        "difficulty": "Beginner",
        "description": "Use if, else, and elif to make choices.",
        "summary": "Learn decision-making in Python.",
        "order_index": 3,
        "content": """
        <h3>Conditions</h3>
        <p>Conditions allow your program to make decisions based on truth values.</p>
        <pre>age = 18
if age >= 18:
    print("Adult")
else:
    print("Minor")</pre>
        <p>Why it matters: programs often need to react differently depending on data.</p>
        <p>Exercise: write a check for passing a score of 70 or more.</p>
        """
    },
    {
        "slug": "python-loops",
        "title": "Loops",
        "category": "Python Basics",
        "difficulty": "Beginner",
        "description": "Repeat actions using for and while loops.",
        "summary": "Learn how loops help automate repetitive work.",
        "order_index": 4,
        "content": """
        <h3>Loops</h3>
        <p>Loops let you repeat tasks without writing the same code many times.</p>
        <pre>for number in [1, 2, 3, 4]:
    print(number)</pre>
        <p>Why it matters: loops are used in data processing, games, and automation.</p>
        <p>Exercise: print each item in a list of fruits.</p>
        """
    },
    {
        "slug": "python-functions",
        "title": "Functions",
        "category": "Python Fundamentals",
        "difficulty": "Beginner",
        "description": "Organize code into reusable blocks.",
        "summary": "Learn functions and parameters.",
        "order_index": 5,
        "content": """
        <h3>Functions</h3>
        <p>A function is a reusable block of code that performs a task.</p>
        <pre>def greet(name):
    return f"Hello, {name}!"

print(greet("Maya"))</pre>
        <p>Why it matters: functions reduce repetition and improve structure.</p>
        <p>Exercise: write a function that adds two numbers and returns the result.</p>
        """
    },
    {
        "slug": "python-lists-and-dicts",
        "title": "Lists and Dictionaries",
        "category": "Python Fundamentals",
        "difficulty": "Beginner",
        "description": "Store grouped data in useful structures.",
        "summary": "Learn lists and dictionaries.",
        "order_index": 6,
        "content": """
        <h3>Lists and Dictionaries</h3>
        <p>Lists store ordered collections and dictionaries store key-value pairs.</p>
        <pre>students = ["Ava", "Ben"]
profile = {"name": "Ava", "age": 21}</pre>
        <p>Why it matters: these structures are used in almost every real project.</p>
        <p>Exercise: create a dictionary with a name and email.</p>
        """
    },
    {
        "slug": "python-files",
        "title": "File Handling",
        "category": "Python Fundamentals",
        "difficulty": "Intermediate",
        "description": "Read and write data to files.",
        "summary": "Learn saving data and reading configuration files.",
        "order_index": 7,
        "content": """
        <h3>File Handling</h3>
        <p>Files let programs persist data between runs.</p>
        <pre>with open("notes.txt", "w") as file:
    file.write("Hello world")</pre>
        <p>Why it matters: apps often need to save records, logs, and settings.</p>
        <p>Exercise: write a short line into a file and read it back.</p>
        """
    },
    {
        "slug": "python-errors",
        "title": "Exceptions and Errors",
        "category": "Python Fundamentals",
        "difficulty": "Intermediate",
        "description": "Handle problems gracefully in code.",
        "summary": "Learn try/except and debugging basics.",
        "order_index": 8,
        "content": """
        <h3>Exceptions and Errors</h3>
        <p>Errors are common. Python lets you catch exceptions and react without crashing.</p>
        <pre>try:
    value = int("abc")
except ValueError:
    print("That was not a number.")</pre>
        <p>Why it matters: user input and external files can fail unexpectedly.</p>
        <p>Exercise: write code that catches a division by zero error.</p>
        """
    },
    {
        "slug": "python-oop",
        "title": "Object-Oriented Programming",
        "category": "Intermediate Python",
        "difficulty": "Intermediate",
        "description": "Use classes and objects to model real problems.",
        "summary": "Learn classes, objects, and methods.",
        "order_index": 9,
        "content": """
        <h3>Object-Oriented Programming</h3>
        <p>Classes define blueprints, and objects are the concrete instances created from them.</p>
        <pre>class Dog:
    def __init__(self, name):
        self.name = name

pet = Dog("Luna")
print(pet.name)</pre>
        <p>Why it matters: OOP is useful for modeling apps, systems, and data.</p>
        <p>Exercise: create a class called Book with a title attribute.</p>
        """
    },
    {
        "slug": "python-sqlite",
        "title": "SQLite with Python",
        "category": "Databases",
        "difficulty": "Intermediate",
        "description": "Store and query structured data locally.",
        "summary": "Learn to use SQLite in Python.",
        "order_index": 10,
        "content": """
        <h3>SQLite with Python</h3>
        <p>SQLite lets you store data in a local database file.</p>
        <pre>import sqlite3
conn = sqlite3.connect("data.db")
conn.execute("CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, text TEXT)")</pre>
        <p>Why it matters: databases are essential for real-world apps.</p>
        <p>Exercise: create a table called tasks with a description column.</p>
        """
    },
    {
        "slug": "python-apis",
        "title": "Working with APIs",
        "category": "APIs",
        "difficulty": "Intermediate",
        "description": "Connect your programs to web services.",
        "summary": "Learn how HTTP APIs work.",
        "order_index": 11,
        "content": """
        <h3>Working with APIs</h3>
        <p>An API gives your program a way to request and send data using HTTP.</p>
        <pre>import requests
response = requests.get("https://api.github.com")
print(response.status_code)</pre>
        <p>Why it matters: APIs power apps, dashboards, bots, automation, and integrations.</p>
        <p>Exercise: request a public API and print the status code.</p>
        """
    },
]
