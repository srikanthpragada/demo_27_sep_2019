import sqlite3

con = sqlite3.connect(r"e:\classroom\python\sep27\library.db")
cur = con.cursor()
cur.execute("select round(avg(price)), min(price), max(price) from books")

row = cur.fetchone()

print(f"Average price : {row[0]}")
print(f"Minimum price : {row[1]}")
print(f"Maximum price : {row[2]}")

con.close()
