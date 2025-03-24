import sqlite3

def some_function():
    from frontend import main_ui


def init_db():
    
    conn = sqlite3.connect('budget_buddy.db')
    cursor = conn.cursor()

    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            prenom TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            mot_de_passe TEXT NOT NULL
        )
    ''')

    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            reference TEXT NOT NULL,
            description TEXT,
            montant REAL NOT NULL,
            date TEXT NOT NULL,
            type TEXT NOT NULL,
            user_id INTEGER,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    ''')

    
    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_db()
    print("Base de données initialisée.")

