import sqlite3

con = sqlite3.connect(r"e:\classroom\python\sep27\library.db")
cur = con.cursor()
cur.execute("select * from books order by price")

for t in cur.fetchall():
    print(f"{t[1]:30}  {t[3]}")

con.close()
