import mysql.connector
from os import getenv
from dotenv import load_dotenv

load_dotenv()
username = getenv("USERNAME")
userpass = getenv("PASS")

# Database connection
def db_connection():
    return mysql.connector.connect(
        host="localhost",
        user=username,
        password=userpass,
        database="budget_buddy"
    )