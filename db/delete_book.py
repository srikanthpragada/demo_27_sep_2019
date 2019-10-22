import sqlite3
import sys

try:
    con = sqlite3.connect(r"e:\classroom\python\sep27\library.db")
except Exception as ex:
    print("Connection error : ", ex)
    sys.exit(1)  # stop program


cur = con.cursor()
id = input("Enter id :")

try:
    cur.execute("delete from books where id = ?", (id,))
    if cur.rowcount == 1:
        print("Successfully Deleted Book!")
        con.commit()
    else:
        print("Id is not found!")

except Exception as ex:
    print("Error : ", ex)
finally:
    con.close()
