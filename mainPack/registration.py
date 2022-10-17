import sqlite3

def registration():
    print("please enter your email")
    email = input()
    with sqlite3.connect('../db/database.db') as db:
        cursor = db.cursor()
        cursor.execute("SELECT email FROM users WHERE email = :name", {"name": email})
        out_email = cursor.fetchone()
        db.commit()
    print(out_email)
    print("please enter your username")
    reg_usr = input()
    with sqlite3.connect('../db/database.db') as db:
        cursor = db.cursor()
        cursor.execute("SELECT username FROM users WHERE username = :name", {"name": reg_usr})
        out_username = cursor.fetchone()
        db.commit()
    print(out_username)

    print("please enter your password")
    reg_psd = input()

    if out_username == None or out_email == None:
        with sqlite3.connect('../db/database.db') as db:
            cursor = db.cursor()
            insertion = "INSERT INTO users (username, password, email) VALUES (?, ?, ?)"
            cursor.execute(insertion, (reg_usr, reg_psd, email))
            out_username = cursor.fetchone()
            db.commit()
            print("Regisration successful. You're in the base")
    else:
        print('User with such username or email already exists')








