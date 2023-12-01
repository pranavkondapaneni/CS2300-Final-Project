import mysql.connector
# You can remove the two imports below and delete line 6 if you want to directly type your password in
from dotenv import load_dotenv
import os

load_dotenv()

conn = mysql.connector.connect(
    host = "localhost",
    user="root",
    password=os.getenv('PASSWORD')
)

cursor = conn.cursor()

cursor.execute("USE HPDatabase;")

# cursor.execute("INSERT INTO Classes VALUES('Light Arts', 'Harry Potter');")
# conn.commit()

# cursor.execute("SELECT * FROM Characters;")
# result = cursor.fetchall()
# print(result[0][1])