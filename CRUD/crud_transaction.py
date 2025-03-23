import mysql.connector
import bcrypt
from CRUD.connecting import db_connection
from getpass import getpass
from datetime import datetime

# Deposit money
def deposit(user_id):
    conn = db_connection()
    cursor = conn.cursor()
    amount = int(input("Combien voulez-vous déposer ?"))
    datetr = datetime.today().strftime('%Y-%m-%d')
    category = input("loisirs, alimentation ou pot-de-vin ?")
    typetr = "deposit",
    id_recipient = 0
    sql_insert_query = """INSERT INTO transactions (user_id, category, amount, datetr, typetr, id_recipient) VALUES (%s, %s, %s, %s, %s, %s) """
    tuple1 = (user_id, category, amount, datetr, typetr, id_recipient)
    cursor.execute (sql_insert_query, tuple1)

    # adding amount to user account
    cursor.execute("SELECT balance FROM users WHERE id =%s", [user_id])
    user_balance = cursor.fetchone()
    user_balance += amount
    cursor.execute("UPDATE users SET balance = user_balance WHERE id = user_id")
    conn.commit()

    cursor.close()
    conn.close()
    print("Success\nTransaction added successfully!")

def withdraw(user_id):
    
    conn = db_connection()
    cursor = conn.cursor()
    amount = int(input("Combien voulez-vous retirer ?"))
    datetr = datetime.today().strftime('%Y-%m-%d')
    category = input("loisirs, alimentation ou pot-de-vin ?")
    typetr = "withdrawal",
    id_recipient = 0
    sql_insert_query = """INSERT INTO transactions (user_id, category, amount, datetr, typetr, id_recipient) VALUES (%s, %s, %s, %s, %s, %s) """
    tuple1 = (user_id, category, amount, datetr, typetr, id_recipient)
    cursor.execute (sql_insert_query, tuple1)

    # removing amount to user account
    cursor.execute("SELECT balance FROM users WHERE id =%s", [user_id])
    user_balance = cursor.fetchone()
    user_balance -= amount
    cursor.execute("UPDATE users SET balance = user_balance WHERE id = user_id")
    conn.commit()

    cursor.close()
    conn.close()