#!/usr/bin/python
# -*- coding: utf-8 -*-

# http://zetcode.com/db/sqlitepythontutorial/

import sqlite3 as lite
import sys

DBFILE = 'documentationprojects.db'
DBFILE = 'notthere.db'

con = None
try:
    con = lite.connect(DBFILE)
    cur = con.cursor()
    cur.execute('SELECT SQLITE_VERSION()')
    row = cur.fetchone()
    print "SQLite version: %s" % row
except lite.Error, e:
    print "Error %s:" % e.args[0]
    sys.exit(1)
finally:
    if con:
        con.close()

con = None
con = lite.connect(DBFILE)
with con:
    cur = con.cursor()
    cur.execute('SELECT SQLITE_VERSION()')
    row = cur.fetchone()
    print "SQLite version: %s" % row

if con:
    con.close()
   

con = lite.connect('testcars.db')

with con:
    
    cur = con.cursor()    
    cur.execute("DROP TABLE IF EXISTS Cars")
    cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
    cur.execute("INSERT INTO Cars VALUES(1,'Audi',52642)")
    cur.execute("INSERT INTO Cars VALUES(2,'Mercedes',57127)")
    cur.execute("INSERT INTO Cars VALUES(3,'Skoda',9000)")
    cur.execute("INSERT INTO Cars VALUES(4,'Volvo',29000)")
    cur.execute("INSERT INTO Cars VALUES(5,'Bentley',350000)")
    cur.execute("INSERT INTO Cars VALUES(6,'Citroen',21000)")
    cur.execute("INSERT INTO Cars VALUES(7,'Hummer',41400)")
    cur.execute("INSERT INTO Cars VALUES(8,'Volkswagen',21600)")

if con:
    con.close()

cars = (
    (1, 'Audi', 52642),
    (2, 'Mercedes', 57127),
    (3, 'Skoda', 9000),
    (4, 'Volvo', 29000),
    (5, 'Bentley', 350000),
    (6, 'Hummer', 41400),
    (7, 'Volkswagen', 21600)
)


con = lite.connect('testcars.db')

with con:
    
    cur = con.cursor()    
    
    cur.execute("DROP TABLE IF EXISTS Cars")
    cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
    cur.executemany("INSERT INTO Cars VALUES(?, ?, ?)", cars)