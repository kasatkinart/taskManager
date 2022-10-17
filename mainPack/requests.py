import sqlite3

reg_email = input()

def reg_request(field, value):
    with sqlite3.connect('../db/database.db') as db:
        cursor = db.cursor()
        cursor.execute("SELECT ? FROM users WHERE ? = ?", (field, field, value))
        out = cursor.fetchone()
        db.commit()
        return out

print(reg_request('field', reg_email))