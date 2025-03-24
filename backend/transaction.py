import sqlite3
from datetime import datetime

def add_transaction(reference, description, amount, transaction_type, user_id):
    conn = sqlite3.connect('budget_buddy.db')
    cursor = conn.cursor()

    if amount<= 0:
        return False
    
    cursor.execute('''
    INSERT TO transactions (reference, description, amout, date, type, user_id'
    VALUES ?, ?, ?, ?, ?, ?)'
    ''', (reference, description, amount, datetime.now().strftime('%Y-%m-%D %H:%M:%S'), transaction_type, user_id))

    conn.commit()
    conn.close()
    return True

def get_transaction(user_id):
    conn = sqlite3.connect('budget_buddy.db')
    cursor= conn.cursor()

    cursor.execute('SELECT * From transactions WHERE user_id = ?', (user_id))
    transactions = cursor.fetchall()

    conn.close()
    return transactions