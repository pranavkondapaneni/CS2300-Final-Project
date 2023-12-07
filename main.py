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

# primaryKeyDict = {
#     "Characters" : "Name",
#     "Student" : Name
# }

#Search function
os.system('cls' if os.name == 'nt' else 'clear')

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


def update_db():
    table_name = input("Enter the name of the table you would like to update: ")
    update_column = input("Enter the name of the column you would like to update: ")
    new_value = input("What would you like to update the value to?: ")
    remain_same_column = input("Which column would keep the same value: ")
    remain_same_othercolumnvalue = input("Enter that value: ")
    if table_name == "Characters" and update_column == "house":
        update_query = f"UPDATE {table_name} SET {update_column} = '{new_value}', Hname = '{new_value}' WHERE {remain_same_column} = '{remain_same_othercolumnvalue}';"
    else:
        update_query = f"UPDATE {table_name} SET {update_column} = '{new_value}' WHERE {remain_same_column} = '{remain_same_othercolumnvalue}';"
    try:
        cursor.execute(update_query)
    except mysql.connector.Error as e: 
        print(e)
    try:
        cursor.execute(f"SELECT {remain_same_column} FROM {table_name} WHERE {remain_same_column} = '{remain_same_othercolumnvalue}';")
    except mysql.connector.Error as e:
        print(e)
        print("The tuple you are trying to change doesn't exist.")

def deleteFrom_db():
    table_name = input("Enter the name of the table you would like to delete from: ")
    primary_key_col = input("Enter the primary key column for the table: ")
    primary_key_value = input(f"Enter the {primary_key_col} value of the tuple to delete: ")

    delete_query = f"DELETE FROM {table_name} WHERE {primary_key_col} = '{primary_key_value}';"

    try:
        cursor.execute(delete_query)
        # conn.commit()

        if cursor.rowcount > 0:
            print("Deleted the tuple.")
        else:
            print("Could not find that tuple to delete.")
    except mysql.connector.Error as e:
        print(e)

def insertInto_db():
    loop = "y"
    while loop == "y":
        table_name = input("Enter the name of the table you would like to insert into: ")
        if table_name == "Characters":
            charName = input("Name: ")
            charAge = input("Age: ")
            charHouse = input("House: ")
            charDOA = input("Is this character alive? \'True\' or \'False\': ")
            if charDOA == "False":
                charCauseOfDeath = input("Cause of death: ")
            elif charDOA == "True":
                charCauseOfDeath = "NULL"
            try:
                cursor.execute(f"INSERT INTO Characters VALUES('{charName}', {charAge}, '{charHouse}', '{charCauseOfDeath}', {charDOA}, NULL, '{charHouse}');")
            except mysql.connector.Error as e:
                print(e)

# --------------------------------------------
        elif table_name == "Student":
            stuName = input("Name: ")
            try:
                cursor.execute(f"INSERT INTO Student VALUES('{stuName}');")
            except mysql.connector.Error as e:
                print(e)
            else:
                try:
                    stuClassChoice = input("Would you like to enter a class this student takes? yes/no: ")
                    while stuClassChoice == "yes":
                        className = input("Class name: ")
                        cursor.execute(f"INSERT INTO Takes VALUES('{className}', '{stuName}');")
                except mysql.connector.Error as e:
                    print(e)

# --------------------------------------------
        elif table_name == "Professor":
            profName = input("Name: ")
            try:
                cursor.execute(f"INSERT INTO Professor VALUES('{profName}');")
            except mysql.connector.Error as e:
                print(e)

# --------------------------------------------
        elif table_name == "Classes":
            classTabName = input("Name: ")
            ProfessorName = input("Pname: ")
            try:
                cursor.execute(f"INSERT INTO Classes VALUES('{classTabName}', '{ProfessorName}');")
            except mysql.connector.Error as e:
                print(e)
                additional = input("Would you like to add additional teachers?")
                while additional == "yes":
                    addName = input("Name: ")
                    try:
                        cursor.execute(f"INSERT INTO Teachers VALUES('{classTabName}', '{addName}')")
                    except mysql.connector.Error as e:
                        print(e)
                    additional = input("Would you like to add additional teachers?")

# --------------------------------------------
        elif table_name == "Spells":
            spellName = input("Name: ")
            spellSpell = input("Spell: ")
            spellDeadly = input("Deadly? True/False: ")
            spellEffect = input("Effect: ")
            try:
                cursor.execute(f"INSERT INTO Spell VALUES('{spellName}', '{spellSpell}', {spellDeadly}, '{spellEffect}');")
            except mysql.connector.Error as e:
                print(e)
            else:
                caster = input("Who cases this spell? ")
                try:
                    cursor.execute(f"INSERT INTO Casts VALUES('{spellName}', '{caster}');")
                except mysql.connector.Error as e:
                    print(e)

# --------------------------------------------
        elif table_name == "Shops":
            shopName = input("Name: ")
            shopType = input("Type: ")
            try:
                cursor.execute(f"INSERT INTO Shops VALUES('{shopName}', '{shopType}');")
            except mysql.connector.Error as e:
                print(e)
            else:
                shopOwner = input("Who owns this shop? ")
                try:
                    cursor.execute(f"UPDATE Characters SET ShopName = '{shopName}' WHERE Name = '{shopOwner}';")
                except mysql.connector.Error as e:
                    print(e)
# Otherwise don't add the shop name
# --------------------------------------------
        elif table_name == "Wands":
            wandOwner = input("Owner: ")
            wandMainMaterial = input("Main material: ")
            wandCoreMaterial = input("Core Material: ")
            try:
                cursor.execute(f"INSERT INTO Wands VALUES('{wandOwner}', '{wandMainMaterial}', '{wandCoreMaterial}');")
            except mysql.connector.Error as e:
                print(e)

# --------------------------------------------
        elif table_name == "Houses":
            print("Are you really really sure you want to add a house? This info hasn't changed in centuries.")
            houseName = input("Name: ")
            try:
                cursor.execute(f"INSERT INTO Houses VALUES('{houseName}');")
            except mysql.connector.Error as e:
                print(e)

# --------------------------------------------
        elif table_name == "Movies":
            movieName = input("Name: ")
            movieOrder = input("# in sequence: ")
            try:
                cursor.execute(f"INSERT INTO Movies VALUES('{movieName}', {movieOrder});")
            except mysql.connector.Error as e:
                print(e)
            else:
                addCharacters = input("Would you like to add more characters? yes/no ")
                while (addCharacters == "yes"):
                    charMovName = input("Character name: ")
                    try:
                        cursor.execute(f"INSERT INTO Char_In_Movies VALUES('{charMovName}', '{movieName}');")
                    except mysql.connector.Error as e:
                        print(e)
                    addCharacters = input("Would you like to add more characters? yes/no ")

# --------------------------------------------
        elif table_name == "Creatures":
            creaturesSpecies = input("Species: ")
            creaturesAvgWeight = input("Average Weight: ")
            friendlyOrDangerous = input("Is the creature friendly? True/False ")
            try:
                cursor.execute(f"INSERT INTO Creatures VALUES('{creaturesSpecies}', '{creaturesAvgWeight}', {friendlyOrDangerous});")
            except mysql.connector.Error as e:
                print(e)
            else:
                addCreatures = "yes"
                while (addCreatures == "yes"):
                    creaMovName = input("Which movie was this creature in?: ")
                    try:
                        cursor.execute(f"INSERT INTO Char_In_Movies VALUES('{creaturesSpecies}', '{creaMovName}');")
                    except mysql.connector.Error as e:
                        print(e)
                    addCreatures = input("Was this creature in any other movies? yes/no ")

# --------------------------------------------
        else:
            print("This table does not exist.")
        loop = input("Would you like to continue inserting? y/n: ")
        os.system('cls' if os.name == 'nt' else 'clear')

loop = True
while (loop == True):
    print("WELCOME TO THE HPDATABASE!")
    print("Enter 1 to log in")
    print("     -- OR --")
    print("Enter 2 to create an account")
    print("     -- OR --")
    print("Enter 3 to search the database")
    accountChoice = input("Choice: ")
    os.system('cls' if os.name == 'nt' else 'clear')
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
            print("This username doesn't exist")

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
        


modifyChoice = input("Do you want to (1) Insert, (2) Update, (3) Delete, or (4) end?: ")
while modifyChoice != "4":
    if modifyChoice == "1":
        insertInto_db()
    if modifyChoice == "2":
        update_db()
    if modifyChoice == "3":
        deleteFrom_db()
    modifyChoice = input("Do you want to (1) Insert, (2) Update, (3) Delete, or (4) end?: ")
    conn.commit()


endIt = input("endit: ")


# cursor.execute("INSERT INTO Classes VALUES('Light Arts', 'Harry Potter');")
conn.commit()

# cursor.execute("SELECT * FROM Characters;")
# result = cursor.fetchall()
# print(result[0][1])