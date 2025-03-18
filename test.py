import mysql.connector
from os import getenv
from dotenv import load_dotenv
from tkinter import *

load_dotenv()
username = getenv("USERNAME")
userpass = getenv("PASS")

def display_allproducts():

    try :

        connection = mysql.connector.connect(
            host = "localhost",
            user = username,
            password = userpass,
            database = "store"
        )
        usercurs = connection.cursor()

        usercurs.execute(
            """
                SELECT name_prod, name_cat, price AS prix, quantity as quantite
                FROM product JOIN category 
                ON product.id_cat = category.id_cat;
            """
        )
        rows = usercurs.fetchall()
        print(rows)
        usercurs.close()
        connection.close()
        return rows

    except mysql.connector.Error as error:
        print(f"Something went wrong: {error}")

main_window = Tk()

custom_display = Label(main_window, text="Application inventaire", font=("Helvetica, 18"))

custom_display.pack()

rows = display_allproducts()

liste = Listbox(main_window)
liste.pack()

for r in rows :
    liste.insert(END, r)

main_window.mainloop()