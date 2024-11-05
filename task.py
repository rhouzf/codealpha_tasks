import sqlite3
import os

def login(username, password):
    if len(username) == 0:
        print("Nom d'utilisateur requis")
        return

    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()

    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)

    print(f"Le mot de passe est : {password}")

    user = cursor.fetchone()
    if user:
        print("Connexion réussie")
    else:
        print("Nom d'utilisateur ou mot de passe incorrect")

    conn.close()

login("admin", "1234")
