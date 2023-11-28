CREATE DATABASE WeAreTheChosenOneHarry;

USE WeAreTheChosenOneHarry;

CREATE TABLE Characters(
    Name varchar(50) PRIMARY KEY,
    Age integer,
    house varchar(15),
    Cause_Of_Death varchar(25),
    Dead_Or_Alive boolean,
    ShopName varchar(20),
    Wowner varchar(50),
    Hname varchar(15)
);

CREATE TABLE Student(
    StudentName varchar(50) PRIMARY KEY
);

CREATE TABLE Professor(
    Name varchar(50) PRIMARY KEY
);

CREATE TABLE Takes(
    Cname varchar(15),
    Pname varchar(50),
    PRIMARY KEY(Cname, Pname)
);

CREATE TABLE Classes(
    Name varchar(15) PRIMARY KEY,
    Pname varchar(50)
);

CREATE TABLE Teachers(
    Teacher varchar(15),
    Cname varchar(15),
    PRIMARY KEY(Teacher, Cname)
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
    PRIMARY KEY(Sname, Cname)
);

CREATE TABLE Shops(
    Name varchar(20) PRIMARY KEY,
    Stype varchar(20)
);

CREATE TABLE Wands(
    Owner varchar(50) PRIMARY KEY,
    Main_material varchar(30),
    Core_material varchar(30)
);

CREATE TABLE Houses(
    Name varchar(15) PRIMARY KEY
);

CREATE TABLE Colors(
    Colors varchar(20),
    Hname varchar(15),
    PRIMARY KEY(Colors, Hname)
);

CREATE TABLE Movies(
    Name varchar(30) PRIMARY KEY,
    MOrder integer
);

CREATE TABLE Char_In_Movies(
    Cname varchar(50),
    Mname varchar(30),
    PRIMARY KEY(Cname, Mname)
);

CREATE TABLE Creatures(
    Species varchar(20) PRIMARY KEY,
    Avg_Weight float,
    Friendly_Or_Dangerous boolean
);

CREATE TABLE An_In_Mov(
    Aname varchar(20),
    Mname varchar(30),
    PRIMARY KEY(Aname, Mname)
);

-- INSERT INTO Characters VALUES('Harry Potter', 40, 'Gryffindor', NULL, True, NULL, 'Harry Potter')