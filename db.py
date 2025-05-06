import sqlite3

def connect():
    return sqlite3.connect("fitness_tracker.db")

def create_tables():
    conn = connect()
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS fitness_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        gender TEXT,
        height REAL,
        weight REAL,
        bmi REAL,
        goal INTEGER,
        sleep_hours INTEGER,
        water REAL,
        calorie_intake REAL,
        steps INTEGER,
        calories_burnt_steps REAL,
        workout_type INTEGER,
        workout_duration INTEGER,
        calories_burnt_workout REAL,
        net_calories REAL,
        date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    ''')
    
    conn.commit()
    conn.close()



def save_fitness_data(user_id, gender, height, weight, bmi, goal, sleep, water,
                      cal_intake, steps, cb_steps, workout_type, workout_dur,
                      cb_workout, net_calories):
    conn = connect()
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO fitness_data (
            user_id, gender, height, weight, bmi, goal, sleep_hours, water,
            calorie_intake, steps, calories_burnt_steps,
            workout_type, workout_duration, calories_burnt_workout,
            net_calories
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        user_id, gender, height, weight, bmi, goal, sleep, water,
        cal_intake, steps, cb_steps, workout_type, workout_dur,
        cb_workout, net_calories
    ))
    
    conn.commit()
    conn.close()

import sqlite3

def get_last_entries(user_id, n=3):
    conn = sqlite3.connect("fitness_tracker.db")
    cursor = conn.cursor()

    cursor.execute('''
        SELECT gender, height, weight, bmi, sleep_hours, water, calorie_intake,
               calories_burnt_steps, calories_burnt_workout, net_calories
        FROM fitness_data
        WHERE user_id = ?
        ORDER BY id DESC
        LIMIT ?
    ''', (user_id, n))

    rows = cursor.fetchall()
    conn.close()

    return rows
