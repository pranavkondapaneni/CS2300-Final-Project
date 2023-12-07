CREATE DATABASE HPDatabase;

USE HPDatabase;

CREATE TABLE Characters(
    Name varchar(50) PRIMARY KEY,
    Age integer,
    house varchar(15) CHECK(house='Gryffindor' or house='Slytherin' or house='Ravenclaw' or house='Hufflepuff'),
    Cause_Of_Death varchar(25),
    Dead_Or_Alive boolean,
    ShopName varchar(20),
    Hname varchar(15)
);

CREATE TABLE Student(
    Name varchar(50) PRIMARY KEY,
    FOREIGN KEY (Name) REFERENCES Characters(Name) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Professor(
    Name varchar(50) PRIMARY KEY,
    FOREIGN KEY (Name) REFERENCES Characters(Name) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Takes(
    Cname varchar(15),
    Sname varchar(50),
    PRIMARY KEY(Cname, Sname),
    FOREIGN KEY (Sname) REFERENCES Student(Name) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Classes(
    Name varchar(15) PRIMARY KEY,
    Pname varchar(50) NOT NULL UNIQUE,
    FOREIGN KEY (Pname) REFERENCES Professor(Name) ON DELETE CASCADE ON UPDATE CASCADE
);

ALTER TABLE Takes ADD FOREIGN KEY (Cname) REFERENCES Classes(Name) ON DELETE CASCADE ON UPDATE CASCADE;

CREATE TABLE Teachers(
    Teacher varchar(15),
    Cname varchar(15),
    PRIMARY KEY(Teacher, Cname),
    FOREIGN KEY (Cname) REFERENCES Classes(Name) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Spells(
    Name varchar(50) PRIMARY KEY,
    Spell varchar(50),
    Deadly_or_No boolean,
    Effect varchar(50)
);

CREATE TABLE Casts(
    Sname varchar(50),
    Cname varchar(50),
    PRIMARY KEY(Sname, Cname),
    FOREIGN KEY (Sname) REFERENCES Spells(Name) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (Cname) REFERENCES Characters(Name) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Shops(
    Name varchar(20) PRIMARY KEY,
    Stype varchar(20)
);

ALTER TABLE Characters ADD FOREIGN KEY (ShopName) REFERENCES Shops(Name) ON DELETE SET NULL ON UPDATE CASCADE;

CREATE TABLE Wands(
    Owner varchar(50) PRIMARY KEY,
    Main_material varchar(30),
    Core_material varchar(30),
    FOREIGN KEY (Owner) REFERENCES Characters(Name) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Houses(
    Name varchar(15) PRIMARY KEY CHECK(Name='Gryffindor' or Name='Slytherin' or Name='Ravenclaw' or Name='Hufflepuff')
);

ALTER TABLE Characters ADD FOREIGN KEY (Hname) REFERENCES Houses(Name) ON DELETE SET NULL ON UPDATE CASCADE;

CREATE TABLE Colors(
    Colors varchar(20),
    Hname varchar(15),
    PRIMARY KEY(Colors, Hname),
    FOREIGN KEY (Hname) REFERENCES Houses(Name) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Movies(
    Name varchar(30) PRIMARY KEY,
    MOrder integer
);

CREATE TABLE Char_In_Movies(
    Cname varchar(50),
    Mname varchar(30),
    PRIMARY KEY(Cname, Mname),
    FOREIGN KEY (Cname) REFERENCES Characters(Name) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (Mname) REFERENCES Movies(Name) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Creatures(
    Species varchar(20) PRIMARY KEY,
    Avg_Weight float,
    Friendly_Or_Dangerous boolean
);

CREATE TABLE An_In_Mov(
    Aname varchar(20),
    Mname varchar(30),
    PRIMARY KEY(Aname, Mname),
    FOREIGN KEY (Aname) REFERENCES Creatures(Species) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (Mname) REFERENCES Movies(Name) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE User(
    Username varchar(20),
    Password varchar(20),
    Email varchar(320),
    PRIMARY KEY(Username)
);

INSERT INTO Houses VALUES('Gryffindor');
INSERT INTO Houses VALUES('Slytherin');
INSERT INTO Houses VALUES('Ravenclaw');
INSERT INTO Houses VALUES('Hufflepuff');
-- INSERT INTO Wands VALUES('Harry Potter', 'Gold', 'Silver');


INSERT INTO Characters VALUES('Harry Potter', 40, 'Gryffindor', NULL, True, NULL, 'Gryffindor');
INSERT INTO Characters VALUES('Draco Malfoy', 43, 'Slytherin', NULL, True, NULL, 'Gryffindor');
-- INSERT INTO Characters VALUES('Ron Weasly', 40 , 'Gryffindor', NULL, true, NULL, 'Gryffindor');
-- INSERT INTO Professor VALUES('Harry Potter');
-- INSERT INTO Shops VALUES('Olivanders', 'wand store');
INSERT INTO User VALUES('Pranav', 'thepassword', 'pranav@imthebest.com');