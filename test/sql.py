import mysql.connector as sql

mydb = sql.connect(
  host="localhost",
  user="tomi",
  password="root",
  database="python"
)

mycursor = mydb.cursor()
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")