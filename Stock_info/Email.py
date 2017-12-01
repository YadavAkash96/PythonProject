import smtplib,sys

def sendUmail(to_add,sub,msg,from_e_add='ay1898@gmial.com',login='ay1898@gmail.com',password='xxxxxxx',smtpserver='smtp.gmail.com:587'):
    header='From: {}\n'.format(from_e_add)
    header+='to: {}\n'.format(to_add)
    header+='subject: {}\n\n'.format(sub)
    message =header + '\nName: {}\nYour purchased stock: {}\nPurchased Date: {}\nBuying Price: {}\nCurrent Stock Price: {}\n\n\t\tLOSS: {}%\n\n'.format(msg[2],msg[8],msg[12],msg[10],msg[14],msg[20])
    server=smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    problem=server.sendmail(from_e_add,to_add,message)
    server.quit()

    return problem



