import sqlite3

con = sqlite3.connect(r"e:\classroom\python\sep27\library.db")
cur = con.cursor()
title = input("Enter Title :")
author = input("Enter Author :")
price = input("Enter Price :")

cur.execute("insert into books(title,author,price) values(?,?,?)",
            (title, author, price))
con.commit()
con.close()
