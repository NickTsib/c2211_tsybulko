import sqlite3

connection = sqlite3.connect("pet_DB.sl3", 5)
cur = connection.cursor()
cur.execute("INSERT INTO info_pet (name, type , age) VALUES ('Kesha', 'parrot', 4);")
cur.execute("INSERT INTO info_pet (name, type , age) VALUES ('Gavkun', 'dog', 7);")
cur.execute("INSERT INTO info_pet (name, type , age) VALUES ('Myrchuk', 'cat', 2);")
cur.execute("INSERT INTO info_pet (name, type , age) VALUES ('Okyn', 'fish', 120);")
connection.commit()
connection.close()