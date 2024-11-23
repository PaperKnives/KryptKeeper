from imports import *

def create_tables():
    try:
        connection = sqlite3.connect('account.db')
        connection.execute('''CREATE TABLE IF NOT EXISTS FBox_user(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_name TEXT,
        pass_word TEXT
        )''')

        connection.execute('''CREATE TABLE IF NOT EXISTS personal_files(
        file_id INTEGER PRIMARY KEY AUTOINCREMENT,
        new_file_name TEXT,
        key TEXT,
        file BLOB
        )''')
    except Exception as e:
        messagebox.showerror('Could not create db', f"{e}")
