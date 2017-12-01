import sys,sqlite3
import Email

def Report():
    infile=open(r'D:\python\ethan\Stock_info - Copy\xlsinterface.csv','w+')
    infile.write('id,name,email-id,aadhar-id,symbol,b_price,b_date,c_price,c_date,profit%,loss%\n')
    infile.flush()
    try:
        db=sqlite3.connect('newDB')
        cursor=db.cursor()
        cursor.execute('''select * from newDB''')
    except Exception as E:
        print E
        sys.exit(1)
    else:
        for row in cursor.fetchall():
            try:
                db1=sqlite3.connect('userDB')
                cursor=db1.cursor()
                cursor.execute('''select * from userDB''')
            except Exception as E:
                print E
                sys.exit(1)
            else:
                for data in cursor.fetchall():
                    if data[0]==row[0]:
                        lis=[str(data[0]),',',data[1],',',data[2],',',str(data[3]),',']
                        break
            db1.close()
            if row[5]-row[4]>0:
                profit=row[5]-row[4]
                per_profit=(profit/row[4])*100
                per_loss=0
                lis.extend([row[3], ',', str(row[4]), ',', str(row[2]), ',', str(row[5]), ',', str(row[1]), ',',str(per_profit), ',', str(per_loss), '\n'])
                infile.writelines(lis)
            elif row[5]-row[4]<0:
                loss=abs(row[5]-row[4])
                per_loss=(loss/row[4])*100
                per_profit=0
                lis.extend([row[3], ',', str(row[4]), ',', str(row[2]), ',', str(row[5]), ',', str(row[1]), ',',str(per_profit), ',', str(per_loss), '\n'])
                infile.writelines(lis)
                if per_loss>5:
                    msg=lis
                    Email.sendUmail(lis[4], 'STOCK MARKET REPORT',msg)
            else:
                per_loss=0
                per_profit=0
                lis.extend([row[3],',', str(row[4]),',', str(row[2]),',', str(row[5]),',', str(row[1]),',',str(per_profit),',',str(per_loss),'\n'])
                infile.writelines(lis)
    db.close()
    infile.close()
    return






