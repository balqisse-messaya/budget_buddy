import bcrypt
import sqlite3

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(' utf_8'), salt)
    return hashed

def verify_password(password, hashed):
    return bcrypt.checkpw(password.encode(' utf-8'), hashed)

def register_user(nom, prenom, email, password):
    conn = sqlite3.connect('budget_buddy.db')
    cursor = conn.cursor()
    hashed_password = hash_password(password)
    try:
        cursor.execute(''''
        'INSERT INTO users (nom, prenom email, mot_de_passe
        VALUES (?, ?, ?, ?)
        ''',(nom, prenom, email, hashed_password))
        conn.commit()
    except sqlite3.IntegrityError:
        print("L'utilisateur avec cet email existe déjà.")
    conn.close()
    

