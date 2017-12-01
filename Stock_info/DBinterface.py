'''
Module for DB interface
it hold create,insert,select,delete,update function
'''
import sqlite3,sys
def create():
    try:
        db = sqlite3.connect('userDB')
        cursor = db.cursor()
        cursor.execute(
            '''create table userDB(id int primary key,name varchar(200) not null,email_id varchar(200) not null,aadahar_id int not null unique) ''')
    except Exception as E:
        print E
    db.close()
    try:
        db = sqlite3.connect('symboleDB')
        cursor1 = db.cursor()
        cursor1.execute('''create table symboleDB(id int not null,date varchar(30) not null,symbol varchar(20) not null,buying_price int not null,foreign key(id) references userDB(id) ) ''')
    except Exception as E:
        print E
        sys.exit(1)
    db.close()
    return

def insertuserDB():
    try:
        db = sqlite3.connect('userDB')
        cursor = db.cursor()
        id = input("Enter userID: ")
        name = raw_input("Enter user NAME: ")
        email = raw_input("Enter user Email-ID: ")
        aadhar = input("Enter user Aadhar number: ")
        cursor.execute('''insert into userDB values(?,?,?,?)''', (id, name, email, aadhar))
    except Exception as E:
        print E
        sys.exit(1)
    else:
        db.commit()
    db.close()
    return
def insertsymboleDB():
    try:
        db = sqlite3.connect('symboleDB')
        cursor = db.cursor()
        id = input("Enter userID: ")
        date = raw_input("Enter buying date : ")
        symbol = raw_input("Enter share NAME: ")
        price = input("Enter price of ur share: ")
        cursor.execute('''insert into symboleDB values(?,?,?,?)''', (id, date, symbol, price))
    except Exception as E:
        print E
        sys.exit(1)
    else:
        db.commit()
    db.close()
    return
def selectfromuserDB():
    try:
        db=sqlite3.connect('userDB')
        cursor=db.cursor()
        cursor.execute('''select * from userDB''')
    except Exception as E:
        print E
        sys.exit(1)
    else:
        for row in cursor.fetchall():
            print row
    db.close()
    return


def selectfromsymboleDB():
    try:
        db = sqlite3.connect('symboleDB')
        cursor = db.cursor()
        cursor.execute('''select * from symboleDB''')
    except Exception as E:
        print E
        sys.exit(1)
    else:
        for row in cursor.fetchall():
            print row
    db.close()
    return


def updateuserDB(id,kwargs):
    try:
        db=sqlite3.connect('userDB')
        cursor=db.cursor()
        key_values=kwargs.items()
        n=len(key_values)
        for i in xrange(n):
            cursor.execute('''update userDB set '{}' = '{}' where id= {} '''.format(key_values[i][0],key_values[i][1],id))
    except Exception as E:
        print E
        sys.exit(1)
    else:
        db.commit()
    db.close()

    return

def updatesymboleDB(id,kwargs):
    try:
        db=sqlite3.connect('symboleDB')
        cursor=db.cursor()
        key_values = kwargs.items()
        n = len(key_values)
        for i in xrange(n):
            cursor.execute('''update symboleDB set '{}' = '{}' where id= {} '''.format(key_values[i][0],key_values[i][1],id))
    except Exception as E:
        print E
        sys.exit(1)
    else:
        db.commit()
    db.close()
    return
def deletefrmuserDB(id):#also delete from symboleDB
    try:
        db=sqlite3.connect('userDB')
        cursor=db.cursor()
        cursor.execute('''delete from userDB where id = {}'''.format(id))
    except Exception as E:
        print E
        sys.exit(1)
    else:
        db.commit()
    db.close()
    try:
        db=sqlite3.connect('symboleDB')
        cursor=db.cursor()
        cursor.execute('''delete from symboleDB where id = {}'''.format(id))
    except Exception as E:
        print E
        sys.exit(1)
    else:
        db.commit()
    db.close()
    return

def deletefrmsymboleDB(id):
    try:
        db=sqlite3.connect('symboleDB')
        cursor=db.cursor()
        cursor.execute('''delete from symboleDB where id = {}'''.format(id))
    except Exception as E:
        print E
        sys.exit(1)
    else:
        db.commit()
    db.close()
    return

def deleteall():
    prompt=raw_input("Delete all from userDB or symboleDB ?, select anyone: ")
    try:
        if prompt=='userDB':
            db=sqlite3.connect('userDB')
            cursor=db.cursor()
            cursor.execute('''delete * from userDB ''')
        elif prompt=='symboleDB':
            db = sqlite3.connect('symboleDB')
            cursor = db.cursor()
            cursor.execute('''delete * from symboleDB ''')
        else:
            print "wrong input! sorry"

    except Exception as E:
        print E
        sys.exit(1)
    else:
        db.commit()
    db.close()
    return



