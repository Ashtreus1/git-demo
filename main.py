import sqlite3

conn = sqlite3.connect('demo.db')

info = conn.cursor()

info.execute('''CREATE TABLE IF NOT EXISTS users(
			id INTEGER PRIMARY KEY,
			name TEXT NOT NULL,
			age INTEGER
)''')

info.execute("INSERT INTO users (name, age) VALUES (?, ?)",
	('Alice', 30))
info.execute("INSERT INTO users (name, age) VALUES (?, ?)",
	('Bob', 40))
info.execute("INSERT INTO users (name, age) VALUES (?, ?)",
	('John', 20))
	
info.execute("SELECT * FROM users")
rows = info.fetchall()

for row in rows:
	print(row)

info.close()
conn.close()
