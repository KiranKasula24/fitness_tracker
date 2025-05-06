"""import sqlite3

# Connect to database (or create one if it doesn't exist)
conn = sqlite3.connect('fitness_tracker.db')
cursor = conn.cursor()

# Create user table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
''')

# Create fitness data table
cursor.execute('''
CREATE TABLE IF NOT EXISTS fitness_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    date TEXT,
    weight INTEGER,
    height INTEGER,
    BMI REAL,
    stepsOnDate INTEGER,
    caloriesIntake INTEGER,
    waterIntake REAL,
    sleepHours INTEGER,
    FOREIGN KEY(user_id) REFERENCES users(id)
)
''')

conn.commit()


from getpass import getpass

def signup():
    username = input("Enter a new username: ")
    password = getpass("Enter a new password: ")

    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        print("✅ Account created successfully.")
    except sqlite3.IntegrityError:
        print("❌ Username already exists. Try again.")

def login():
    username = input("Username: ")
    password = getpass("Password: ")

    cursor.execute("SELECT id FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()
    if user:
        print(f"✅ Welcome back, {username}!")
        return user[0]  # user ID
    else:
        print("❌ Invalid login.")
        return None


"""