import sqlite3
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

def get_monthly_expenses():
    """ Récupère les dépenses mensuelles depuis la base de données."""
    conn = sqlite3.connect ('budegr_buddy.db')
    cursor = conn.cursor()
    cursor.execute(''''
    SELECT strftime('%Y-%m', date) AD month, SUM(montant)'
    From transactions
    WHERE type = 'retrait' --Dépenses uniquement
    GROUP BY month'
    ''')

    result = cursor.fetchall()
    conn.close()
    return result

def plot_expenses_in_tkinter(root):
    """Affiche le graphique des dépenses mensuelles dans la fenêtre tkinter."""
    data = get_monthly_expenses()
    months = [entry[0] for entry in data]
    amounts = [entry[1] for entry in data]

    fig, ax = plt.subplots()
    ax.bar(months, amounts, color='red')
    ax.set_xlabel('Month')
    ax.set_ylabel('Expenses ($)')
    ax.set_title('Monthly Expenses')
    ax.set_xticklabels(months, rotation=45)

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()

def show_graph_button(root):
    btn = tk.Button(root, text="Show monthly expenses graph", command=lambda: plot_expenses_in_tkinter(root))
    btn.pack(pady=20)

    root = tk.TK()
    root.title("Budget Buddy - Monthly Expenses")
    show_graph_button(root)
    root.mainloop()
    