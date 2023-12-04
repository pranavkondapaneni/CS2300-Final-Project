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

#Search function
def search_db(table_name):
    print("Do you want to filter your search?")
    choice = input("type '1' for yes or '2' for no. Type '3' to go to main menu")

    if choice == "1":
        print("Do you want to see a single column, single tuple or multiple tuples")
        filter = input("If you want to see a single column enter 1, if you want to see a single tuple enter 2, if you want to see multiple tuples enter 3")

        if filter == "1":
            col = input("Enter name of column")
            search_query = f"SELECT {col} FROM {table_name};"
        if filter == "2":
            print("Must use primary Key!")
            search_col = input("Enter primary key for the table")
            search_val = input("Enter the value you want to serach")
            col = "*"
            search_query = f"SELECT {col} FROM {table_name} WHERE {search_col} = '{search_val}';"
        if filter == "3":
            col = "*"
            search_col = input("Enter column that is not the primary key (i.e age, color, material)")
            search_val = input("Enter a value")
            search_query = f"SELECT {col} FROM {table_name} WHERE {search_col} = {search_val};"
    
    if choice == "2":
        search_query = f"SELECT * FROM {table_name};"

    if choice == "3":
        return 0

    try:
        cursor.execute(search_query)
        results = cursor.fetchall()

        if results:
            print("Search Results:")
            for result in results:
                print(result)
        else:
            print("no results found")
    except mysql.connector.Error as e:
        print(e)   

print("WELCOME TO THE HPDATABASE!")
print("Enter 1 to log in")
print("     -- OR --")
print("Enter 2 to create an account")
print("     -- OR --")
print("Enter 3 to search the database")
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

    if(accountChoice == "3"):
        table = input("Input the table you want to search")
        search_db(table)
        loop = False


print("Enter choice")

endIt = input("endit: ")




# cursor.execute("INSERT INTO Classes VALUES('Light Arts', 'Harry Potter');")
conn.commit()

# cursor.execute("SELECT * FROM Characters;")
# result = cursor.fetchall()
# print(result[0][1])