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

print(conn)