import sqlite3
connection = sqlite3.connect("feedback.db")
cursor = connection.cursor()
cmd = """
CREATE TABLE IF NOT EXISTS FEEDBACK(
    id integer primary key AUTOINCREMENT,
    fullname text not null,
    usn varchar(10) not null,
    contact varchar(10) not null,
    email varchar(50) not null,
    message text not null
)"""

cursor.execute(cmd)
connection.commit()

cmd = "INSERT INTO FEEDBACK(fullname, usn, contact, email, message) VALUES (?,?,?,?,?)"
cursor.execute(cmd, ("John Doe", "1RV17CS001", "9876543210", "john.doe@example.com", "Great service!"))
connection.commit()

cursor.execute(cmd, ("shama", "1mw7CS001", "6363428833", "john123.doe@example.com", "Good service!"))
connection.commit()

cursor.execute("SELECT * FROM FEEDBACK")
print(cursor.fetchall())
r=cursor.execute("SELECT * FROM FEEDBACK where fullname =?",("shama",)).fetchall()
print(r)
connection.commit()