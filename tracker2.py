import sqlite3
import db

def signup():
    conn = db.connect()
    cursor = conn.cursor()
    username = input("Choose a username: ")
    password = input("Choose a password: ")
    
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        print("Signup successful!")
        return cursor.lastrowid
    except sqlite3.IntegrityError:
        print("Username already exists.")
        return None
    finally:
        conn.close()

def login():
    conn = db.connect()
    cursor = conn.cursor()
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    cursor.execute("SELECT id FROM users WHERE username = ? AND password = ?", (username, password))
    result = cursor.fetchone()
    conn.close()
    
    if result:
        print("Login successful!")
        return result[0]
    else:
        print("Invalid username or password.")
        return None
