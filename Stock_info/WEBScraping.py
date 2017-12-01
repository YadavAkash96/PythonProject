import sqlite3,sys,datetime,urllib,re

def create():
    try:
        db=sqlite3.connect('newDB')
        cursor=db.cursor()
        cursor.execute('''create table newDB(id int not null,date varchar(30) not null,p_date varchar(30) not null,symbol varchar(30) not null,buying_price int not null,c_price int not null,foreign key(id) references userDB(id) )''')
    except Exception as E:
        print E
        sys.exit(1)
    db.close()
    return

def selectfrmnewDB():
    try:
        db=sqlite3.connect('newDB')
        cursor=db.cursor()
        cursor.execute('''select * from newDB''')
    except Exception as E:
        print E
        sys.exit(1)
    else:
        for row in cursor.fetchall():
            print row
    db.close()
    return

def deletefrmnewDB():
    try:
        db=sqlite3.connect('newDB')
        cursor=db.cursor()
        #cursor.execute('''delete from newDB where id={}'''.format(id))
        cursor.execute('''delete from newDB''')
    except Exception as E:
        print E
        sys.exit(1)
    else:
        db.commit()
    db.close()
    return

def insertintonewDB():
    try:
        deletefrmnewDB()
        db = sqlite3.connect('symboleDB')
        cursor = db.cursor()
        cursor.execute('''select * from symboleDB''')
    except Exception as E:
        print E
        sys.exit(1)
    else:
        for row in cursor.fetchall():
            try:
                db1=sqlite3.connect('newDB')
                cursor=db1.cursor()
                id=row[0]
                p_date=row[1]
                symbol=row[2]
                buying_price=row[3]
                date=datetime.date.today()
                c_price=webscrap(symbol)
                if type(c_price)==str:
                    c_price=c_price.strip().split(',')
                    join=''
                    for i in xrange(len(c_price)):
                        join=join+c_price[i]
                    join=float(join)
                    c_price=join
                cursor.execute('''insert into newDB values(?,?,?,?,?,?)''',(id,date,p_date,symbol,buying_price,c_price))
            except Exception as E:
                print E
                sys.exit(1)
            else:
                db1.commit()
            db1.close()

    db.close()
    return

def webscrap(symbol):
    baseurl=r'https://finance.google.com/finance?q='
    sym=symbol
    url=baseurl+sym
    urlObj=urllib.urlopen(url)
    readhtml=urlObj.read()
    match = re.search('<span id="ref_\d+_l">(.*)</span>', readhtml)
    if match:
        c=match.group(1)
    else:
        print sym
        print "Error!sorry:("
    return c



