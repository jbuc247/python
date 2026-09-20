CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL DEFAULT 'Student',
    level TEXT NOT NULL DEFAULT 'Beginner',
    xp INTEGER NOT NULL DEFAULT 0,
    streak INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS progress (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    topic TEXT NOT NULL,
    completion_percentage INTEGER NOT NULL DEFAULT 0,
    FOREIGN KEY (user_id) REFERENCES users (id)
);

CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    difficulty TEXT NOT NULL,
    category TEXT NOT NULL,
    is_completed BOOLEAN NOT NULL DEFAULT 0,
    score INTEGER DEFAULT 0
);

-- Insert a default user only if not exists
INSERT INTO users (username, level, xp, streak)
SELECT 'Student', 'Python Builder', 1240, 7
WHERE NOT EXISTS (SELECT 1 FROM users WHERE id = 1);

-- Insert some mock progress
INSERT INTO progress (user_id, topic, completion_percentage)
SELECT 1, 'Python Functions', 78
WHERE NOT EXISTS (SELECT 1 FROM progress WHERE user_id = 1);
