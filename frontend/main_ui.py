import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import tkinter as tk
from tkinter import messagebox
from backend.database import init_db
from backend.auth import register_user
from backend.transaction import add_transaction, get_transaction
from frontend.graphs import plot_expenses_in_tkinter
from tkinter import Tk, Label, Canvas
from PIL import Image, ImageTk

def open_registration_window():
    registration_window = tk.Toplevel(root)
    registration_window.title("Inscription")
    registration_window.geometry("400x400")
    
    tk.Label(registration_window, text="Nom", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10)
    entry_nom = tk.Entry(registration_window, font=("Arial", 12))
    entry_nom.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(registration_window, text="Prénom", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=10)
    entry_prenom = tk.Entry(registration_window, font=("Arial", 12))
    entry_prenom.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(registration_window, text="Email", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=10)
    entry_email = tk.Entry(registration_window, font=("Arial", 12))
    entry_email.grid(row=2, column=1, padx=10, pady=10)

    tk.Label(registration_window, text="Mot de passe", font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=10)
    entry_password = tk.Entry(registration_window, show="*", font=("Arial", 12))
    entry_password.grid(row=3, column=1, padx=10, pady=10)

    def register_user():
        nom = entry_nom.get()
        prenom = entry_prenom.get()
        email = entry_email.get()
        password = entry_password.get()

        if nom and prenom and email and password:
            messagebox.showinfo("Succès", "Utilisateur enregistré avec succès.")
            registration_window.destroy()
        else:
            messagebox.showwarning("Attention", "Tous les champs sont requis.")

    tk.Button(registration_window, text="S'inscrire", command=register_user, font=("Arial", 12), bg="#f8c8d8").grid(row=4, columnspan=2, pady=20)

def open_login_window():
    login_window = tk.Toplevel(root)
    login_window.title("Se connecter")
    login_window.geometry("400x300")
    
    tk.Label(login_window, text="Email", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10)
    entry_email = tk.Entry(login_window, font=("Arial", 12))
    entry_email.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(login_window, text="Mot de passe", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=10)
    entry_password = tk.Entry(login_window, show="*", font=("Arial", 12))
    entry_password.grid(row=1, column=1, padx=10, pady=10)

    def login_user():
        email = entry_email.get()
        password = entry_password.get()
        if email and password:
            messagebox.showinfo("Succès", "Connexion réussie.")
            login_window.destroy()
        else:
            messagebox.showwarning("Attention", "Veuillez entrer un email et un mot de passe.")

    tk.Button(login_window, text="Se connecter", command=login_user, font=("Arial", 12), bg="#f8c8d8").grid(row=2, columnspan=2, pady=20)

transactions = []

def add_transaction_ui():
    add_window = tk.Toplevel(root)
    add_window.title("Ajouter une Transaction")
    add_window.geometry("400x300")

    tk.Label(add_window, text="Référence", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10)
    entry_reference = tk.Entry(add_window, font=("Arial", 12))
    entry_reference.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(add_window, text="Description", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=10)
    entry_description = tk.Entry(add_window, font=("Arial", 12))
    entry_description.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(add_window, text="Montant", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=10)
    entry_amount = tk.Entry(add_window, font=("Arial", 12))
    entry_amount.grid(row=2, column=1, padx=10, pady=10)

    tk.Label(add_window, text="Type de transaction", font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=10)
    entry_type = tk.Entry(add_window, font=("Arial", 12))
    entry_type.grid(row=3, column=1, padx=10, pady=10)

    def add_transaction():
        reference = entry_reference.get()
        description = entry_description.get()
        amount = entry_amount.get()
        transaction_type = entry_type.get()

        if reference and description and amount and transaction_type:
            transactions.append({
                "Référence": reference,
                "Description": description,
                "Montant": amount,
                "Type": transaction_type
            })
            messagebox.showinfo("Succès", "Transaction ajoutée avec succès.")
            add_window.destroy()
        else:
            messagebox.showwarning("Attention", "Tous les champs doivent être remplis.")

    tk.Button(add_window, text="Ajouter", command=add_transaction, font=("Arial", 12), bg="#f8c8d8").grid(row=4, columnspan=2, pady=20)


def show_transaction_ui():
    show_window = tk.Toplevel(root)
    show_window.title("Transactions")
    show_window.geometry("500x400")

    listbox = tk.Listbox(show_window, width=50, height=15)
    listbox.pack(padx=10, pady=10)

    for transaction in transactions:
        listbox.insert(tk.END, f"Référence: {transaction['Référence']} | Montant: {transaction['Montant']} | Type: {transaction['Type']}")

root = tk.Tk()
root.title("Budget Buddy - Gestion Financière")

root.geometry("1200x800")
root.configure(bg="#f4f4f4")

title_label = tk.Label(root, text="BUDGET BUDDY", font=("Arial Black", 30, "bold"), fg="white", bg="#f8c8d8", relief="solid", bd=2)
title_label.pack(pady=20)

button_frame = tk.Frame(root)
button_frame.pack(pady=30)

btn_register = tk.Button(button_frame, text="S'inscrire", font=("Arial", 12, "bold"), fg="black", bg="#f8c8d8", width=20, height=2, command=open_registration_window)
btn_register.grid(row=0, column=0, padx=10, pady=10)

btn_login = tk.Button(button_frame, text="S'identifier", font=("Arial", 12, "bold"), fg="black", bg="#f8c8d8", width=20, height=2, command=open_login_window)
btn_login.grid(row=0, column=1, padx=10, pady=10)

btn_add_transaction = tk.Button(button_frame, text="Ajouter une transaction", font=("Arial", 12, "bold"), fg="black", bg="#f8c8d8", width=20, height=2, command=add_transaction_ui)
btn_add_transaction.grid(row=1, column=0, padx=10, pady=10)

btn_show_transactions = tk.Button(button_frame, text="Voir les transactions", font=("Arial", 12, "bold"), fg="black", bg="#f8c8d8", width=20, height=2, command=show_transaction_ui)
btn_show_transactions.grid(row=1, column=1, padx=10, pady=10)


root.mainloop()












