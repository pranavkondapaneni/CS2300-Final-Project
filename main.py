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

print("WELCOME TO THE HPDATABASE!")
print("Enter 1 to log in")
print("     -- OR --")
print("Enter 2 to create an account")
accountChoice = input("Choice: ")
os.system('cls' if os.name == 'nt' else 'clear')

loop = True
while (loop == True):
    if(accountChoice == "1"):
        username = input("Username: ")
        cursor.execute("SELECT Username FROM User;")
        usernamesFromDB = cursor.fetchall()
        if (username,) in usernamesFromDB:
            answer = "yes"
            while(answer == "yes"):
                password = input("Password: ")
                cursor.execute("SELECT Password FROM User;")
                passwordsFromDB = cursor.fetchall()
                os.system('cls' if os.name == 'nt' else 'clear')
                if (password,) not in passwordsFromDB:
                    print("Password incorrect")
                    answer = input("Would you like to reenter your password? yes/no: ")
                    if (answer == "no"):
                        accountChoice = input("Reenter username and password? Enter 1. Create new account? Enter 2: ")
                else:
                    answer = "no"
                    loop = False
                os.system('cls' if os.name == 'nt' else 'clear')
        else:
            accountChoice = input("This username doesn't exist. if you would like to reenter, enter 1, otherwise, enter 2: ")

    if(accountChoice == "2"):
        createUsername = input("Enter your username: ")
        createPassword = input("Enter your password: ")
        createEmail = input("Enter your email ID: ")
        os.system('cls' if os.name == 'nt' else 'clear')
        loop = False
        try:
            cursor.execute("INSERT INTO User VALUES('{}', '{}', '{}');".format(createUsername, createPassword, createEmail))
        except mysql.connector.Error as e:
            print("The username you have entered already exists, please enter a new username!")
            loop = True
endIt = input("endit: ")


# cursor.execute("INSERT INTO Classes VALUES('Light Arts', 'Harry Potter');")
conn.commit()

# cursor.execute("SELECT * FROM Characters;")
# result = cursor.fetchall()
# print(result[0][1])