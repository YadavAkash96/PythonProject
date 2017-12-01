import DBinterface
import WEBScraping
import Xlsinterface

while 1>0:
    print "1.insert into userDB"
    print "2.insert into symboleDB"
    print "3.select from userDB"
    print "4.select from symboleDB"
    print "5.update userDB"
    print "6.update symboleDB"
    print "7.delete userDB"
    print "8.delete symboleDB"
    print "9.deleteall either userDB or symboleDB"
    print "10.select from newDB"
    print "11.insert into newDB"
    print "12.Delete all from newDB"
    print "13. Report "
    choice = input("Enter any number from above option: ")
    if choice==1:
        DBinterface.insertuserDB()
    elif choice==2:
        DBinterface.insertsymboleDB()
    elif choice==3:
        DBinterface.selectfromuserDB()
    elif choice==4:
        DBinterface.selectfromsymboleDB()
    elif choice==5:
        id = input("Enter userID for update: ")
        args=raw_input("what u want to update(name,email_id,aadahar_id)?,enter value followed by,: ").strip().split(',')
        dic={}
        for i in args:
            if i=='aadahar_id':
                dic[i] = input("Enter {}: ".format(i))
            else:
                dic[i] = raw_input("Enter {}: ".format(i))
        DBinterface.updateuserDB(id,dic)
    elif choice==6:
        id = input("Enter userID for update: ")
        args = raw_input("what u want to update(date,symbol,buying_price)?,enter value followed by,: ").strip().split(',')
        dic = {}
        for i in args:
            if i == 'buying_price':
                dic[i] = input("Enter {}: ".format(i))
            else:
                dic[i] = raw_input("Enter {}: ".format(i))
        DBinterface.updatesymboleDB(id,dic)
    elif choice==7:
        id=input("Enter userID for delete: ")
        DBinterface.deletefrmuserDB(id)
    elif choice==8:
        id = input("Enter userID for delete: ")
        DBinterface.deletefrmsymboleDB(id)
    elif choice==9:
        DBinterface.deleteall()
    elif choice==10:
        WEBScraping.selectfrmnewDB()
    elif choice==11:
        WEBScraping.insertintonewDB()
    elif choice==12:
        WEBScraping.deletefrmnewDB()
    elif choice==13:
        Xlsinterface.Report()
    else:
        pass
    choice=input("u want to continue(1) or quit(0)? ")
    if choice!=1:
        break
