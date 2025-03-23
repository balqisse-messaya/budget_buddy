import mysql.connector
import bcrypt
from CRUD.connecting import db_connection
from getpass import getpass

def validate_password(password):
    if (len(password) < 10 or
        not any(char.isupper() for char in password) or
        not any(char.islower() for char in password) or
        not any(char.isdigit() for char in password) or
        not any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/" for char in password)):
        return False
    return True

# User registration
def register_user():
    last_name = input("Nom de famille ?")
    first_name = input("Prénom ?")
    email = getpass("Adresse électronique ?")
    password = "plop"
    while not validate_password(password):
        password = input("Veuillez entrer un mot de passe sécurisé")
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    conn = db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (last_name, first_name, email, password) VALUES (%s, %s, %s, %s)",
                       (last_name, first_name, email, hashed_password))
        conn.commit()
        print("Success\nRegistration successful!")
    except mysql.connector.Error as err:
        print(f"Error\n{str(err)}")
    finally:
        cursor.close()
        conn.close()

# User login
def login_user():
    conn = db_connection()
    cursor = conn.cursor()
    email = input("Adresse électronique ?")
    password = getpass("Mot de passe ?")
    cursor.execute("SELECT id, password FROM users WHERE email = %s", [email])
    user = cursor.fetchone()
    if user and bcrypt.checkpw(password.encode('utf-8'), user[1].encode('utf-8')):
        print("Bienvenue !")
        print(user[0])
        return user[0] 
    else:
        print("Error\nInvalid email or password")
        return None

