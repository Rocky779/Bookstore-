import mysql.connector
mycon=mysql.connector.connect(host='localhost',user='root',passwd='pavitra',database='pavitra')
mycursor=mycon.cursor()
f1=open(r"C:\Users\pavitra\Desktop\pavitra python\all accounts.txt",'w')
rec='NAME'+"    "+'EMAIL ADDRESS'+"    "+"PASSWORD"
nrec=rec+'\n'
f1.write(nrec)
f1.close()
f3=open(r"C:\Users\pavitra\Desktop\pavitra python\buy.txt",'w+')
rec='NAME'
f3.write(rec)
f3.write('\n')
f3.close()
f4=open(r"C:\Users\pavitra\Desktop\pavitra python\generes.txt",'w+')
f4.write('1.adventure')
f4.write('\n')
f4.write('2.mystery')
f4.write('\n')
f4.write('3.science')
f4.close()
f5=open(r"C:\Users\pavitra\Desktop\pavitra python\adventure.txt",'w+')
f5.write('1 . ADVENTURE OF NARNIA of $ 15')
f5.write('\n')
f5.write('2 . LORD OF THE RINGS of $ 20')
f5.write('\n')
f5.write('3 . HARRY POTTER:DEATHLY HALLOWS of $ 25')
f5.close()

f6=open(r"C:\Users\pavitra\Desktop\pavitra python\mystery.txt",'w+')
f6.write('1 . magic tree house of $ 15')
f6.write('\n')
f6.write('2 . dan brown 1 of $ 20')
f6.write('\n')
f6.write('3 . dan brown 2 of $ 25')
f6.close()

f7=open(r"C:\Users\pavitra\Desktop\pavitra python\science.txt",'w+')
f7.write('1 . physics of $ 15')
f7.write('\n')
f7.write('2 . chemistry of $ 20')
f7.write('\n')
f7.write('3 . Biology of $ 30')
f7.close()




def fold(n):
    f3=open(r"C:\Users\pavitra\Desktop\pavitra python\buy.txt",'r+')
    f3.write(n)
    f3.close()
def generes():
    f4=open(r"C:\Users\pavitra\Desktop\pavitra python\generes.txt",'r+')
    x=f4.read()
    print(x)
    f4.close()

def adventure():
    f5=open(r"C:\Users\pavitra\Desktop\pavitra python\adventure.txt",'r+')
    x=f5.read()
    print(x)
    f5.close()
def mystery():
    f6=open(r"C:\Users\pavitra\Desktop\pavitra python\mystery.txt",'r+')
    y=f6.read()
    print(y)
    f6.close()
def science():
    f7=open(r"C:\Users\pavitra\Desktop\pavitra python\science.txt",'r+')
    z=f7.read()
    print(z)
    f7.close()
def alldetails(n,e,p):
    f1=open(r"C:\Users\pavitra\Desktop\pavitra python\all accounts.txt",'a')
    rec=n+" "+e+"     "+p
    nrec=rec+'\n'
    f1.write(nrec)
def permanentstorage(n,e,p):
    q="insert into allaccounts values('{}','{}','{}')".format(n,e,p)
    mycursor.execute(q)
    mycon.commit()
def allbooks(n,l,c):
    r=" "
    for i in l:
        if len(i)>10:
            a=i[4:10]
            r=r+a
        else:
            a=i+"  "
            r=r+a
            
    q="insert into accountdetails values('{}','{}',{})".format(n,r,c)
    mycursor.execute(q)
    mycon.commit()
    
    
    
e=0    
while True:
        cart=[]
        cost=0
        print('ADMIN?? ..... LOGIN TO SEE THE DETAILS')
        print('\n')
        print('\n')
        print('HAVE AN ACCOUNT  ')
        print('\n')
        print('\n')
        print('WANT TO CREATE AN ACCOUNT ')
        print('\n')
        print('\n')
        ask=input('enter EXISTS or CREATE OR ADMIN')
        print('\n')
        print('\n')
        if ask=='ADMIN':
            print('HELLO ADMIN PLEASE ENTER THE :')
            u='admin@gmail.com'
            p='abcd'
            user=input('enter username')
            passwd=input('enter password')
            if user==u and passwd==p:
                print('WELCOME TO YOUR ADMIN ACCOUNT')
                print('\n')
                print('\n')
                while True:
                    choice=input('DO YOU WANT TO SEE ALL ACCOUNTS PRESS A OR YOU WANT TO SEE ALL DETAILS PRESS P')
                    if choice=='A':
                        mycursor.execute("select * from allaccounts")
                        mydata=mycursor.fetchall()
                        for i in mydata:
                            print(i)
                        print('THERE YOU GO')
                        change=input('DO YOU WANT TO DELETE ANY RECORDS PRESS D OR PRESS N')
                        if change=='D':
                            na=input('input the name to be deleted')
                            q="delete from allaccounts where name='{}'".format(na)
                            q1="delete from accountdetails where name='{}'".format(na)
                            mycursor.execute(q)
                            mycursor.execute(q1)
                            mycon.commit()
                            mycursor.execute("select * from allaccounts")
                            mydata=mycursor.fetchall()
                            for i in mydata:
                                 print(i)
                            print('THERE YOU GO')
                        else:
                            pass
                        ch=input('continue admin account press c or logout press l')
                        if ch=='c':
                           pass
                        else:
                           break
                    elif choice=='P':
                        mycursor.execute("select * from accountdetails")
                        mydata=mycursor.fetchall()
                        for i in mydata:
                            print(i)
                        print('THERE YOU GO')
                        ch=input('continue admin account press c or logout press l')
                        if ch=='c':
                             pass
                        else:
                             break
            pl=input('do you want to continue using the site y/n')
            print('\n')
            if pl=='n':
                break
                    
                    
                
                
                
            
        elif ask=='EXISTS':
            print('Please sign in')
            print('\n')
            f1=open(r"C:\Users\pavitra\Desktop\pavitra python\all accounts.txt",'r')
            name=input('NAME')
            print('\n')
            email=input('EMAIL ADDRESS')
            print('\n')
            password=input('PASSWORD')
            print('\n')
            permanentstorage(name,email,password)
            mycursor.execute('select * from allaccounts')
            mydata=mycursor.fetchall()
            for k in mydata:
                if k[0]==name and k[1]==email and k[2]==password:
                    print('account found' )
                    break
            
                    
            else:
                print('sorry account does not exist')
                print('\n')
                print('please create a new account')
                print('\n')
                print('your account is created please proceed')
                print('\n')
            fold(name)
            print('HELLO',name,'WANT TO BUY BOOKS')
            print('\n')
            en=input('enter yes or no')
            if en=='yes':
                generes()
                l=0
                while True:
                    ch=int(input('enter the choice'))
                    print('\n')
                    if ch==1:
                        adventure()
                        print('\n')
                        print('loading....')
                        print('\n')
                        print('\n')
                        print('select books choice')
                        print('\n')
                        num=int(input('how many books do you want to buy'))
                        print('\n')
                        g=1
                        while g<=num:
                            cho=int(input('enter choice of adventure books'))
                            print('\n')
                            f5=open(r"C:\Users\pavitra\Desktop\pavitra python\adventure.txt",'r+')
                            for i in f5:
                                j=i.split()
                                if int(j[0])==cho:
                                    cart.append(i)
                                    cost+=int(j[-1])
                                    g+=1
                                else:
                                    pass
                        ast=input('want to buy more books enter yes or no')
                        print('\n')
                        if ast=='no':
                            print('your cart consists of the following books:')
                            print('\n')
                            for i in cart:
                                print(i[2:])
                            print('cost',cost)
                            break
                    elif ch==2:
                        mystery()
                        print('\n')
                        print('loading....')
                        print('\n')
                        print('\n')
                        print('select books choice')
                        print('\n')
                        num=int(input('how many books do you want to buy'))
                        print('\n')
                        g=1
                        while g<=num:
                            cho=int(input('enter choice of mystery books'))
                            f6=open(r"C:\Users\pavitra\Desktop\pavitra python\mystery.txt",'r+')
                            for i in f6:
                                j=i.split()
                                if int(j[0])==cho:
                                    cart.append(i)
                                    cost+=int(j[-1])
                                    g+=1
                        ast=input('want to buy more books enter yes or no')
                        print('\n')
                        if ast=='no':
                            print('your cart consists of the following books:')
                            print('\n')
                            for i in cart:
                                 print(i[2:])
                            print('cost',cost)
                            break
                    elif ch==3:
                        science()
                        print('\n')
                        print('loading....')
                        print('\n')
                        print('\n')
                        print('select books choice')
                        print('\n')
                        num=int(input('how many books do you want to buy'))
                        print('\n')
                        g=1
                        while g<=num:
                            cho=int(input('enter choice of science books'))
                            print('\n')
                            f7=open(r"C:\Users\pavitra\Desktop\pavitra python\science.txt",'r+')
                            for i in f7:
                                j=i.split()
                                if int(j[0])==cho:
                                    cart.append(i)
                                    cost+= int(j[-1])
                                    g+=1
                        ast=input('want to buy more books enter yes or no')
                        print('\n')
                        if ast=='no':
                            print('your cart consists of the following books:')
                            print('\n')
                            for i in cart:
                                 print(i[2:])
                            print('cost',cost)
                            break    
                    else:
                        print('your cart consists of the following books:')
                        print('\n')
                        for i in cart:
                             print(i[2:])
                        print('cost',cost)
                        break
            else:
               print('your cart consists of the following books:')
               print('\n')
               for i in cart:
                  print(i)
               print('cost',cost)
            allbooks(name,cart,cost)   
            pl=input('do you want to continue using the site y/n')
            print('\n')
            if pl=='n':
                break
            
        elif ask=='CREATE':
            print('Please create an account...')
            print('\n')
            r=1
            name=input('NAME')
            print('\n')
            email=input('EMAIL ADDRESS')
            print('\n')
            password=input('PASSWORD')
            print('\n')
            alldetails(name,email,password)
            fold(name)
            permanentstorage(name,email,password)
            print('HELLO',name,'WANT TO BUY BOOKS')
            print('\n')
            en=input('enter yes or no')
            print('\n')
            if en=='yes':
                generes()
                l=0
                while True:
                    ch=int(input('enter the choice'))
                    print('\n')
                    if ch==1:
                        adventure()
                        print('\n')
                        print('loading....')
                        print('\n')
                        print('\n')
                        print('select books choice')
                        print('\n')
                        num=int(input('how many books do you want to buy'))
                        print('\n')
                        g=1
                        while g<=num:
                            cho=int(input('enter choice of adventure books'))
                            print('\n')
                            f5=open(r"C:\Users\pavitra\Desktop\pavitra python\adventure.txt",'r+')
                            for i in f5:
                                j=i.split()
                                if int(j[0])==cho:
                                    cart.append(i)
                                    cost+=int(j[-1])
                                    g+=1
                                else:
                                    pass
                        ast=input('want to buy more books enter yes or no')
                        print('\n')
                        if ast=='no':
                            print('your cart consists of the following books:')
                            print('\n')
                            for i in cart:
                                    print(i[2:])
                            print('cost',cost)
                            break
                    elif ch==2:
                        mystery()
                        print('\n')
                        print('loading....')
                        print('\n')
                        print('\n')
                        print('select books choice')
                        print('\n')
                        num=int(input('how many books do you want to buy'))
                        print('\n')
                        g=1
                        while g<=num:
                            cho=int(input('enter choice of mystery books'))
                            print('\n')
                            f6=open(r"C:\Users\pavitra\Desktop\pavitra python\mystery.txt",'r+')
                            for i in f6:
                                j=i.split()
                                if int(j[0])==cho:
                                    cart.append(i)
                                    cost+=int(j[-1])
                                    g+=1
                        ast=input('want to buy more books enter yes or no')
                        print('\n')
                        if ast=='no':
                            print('your cart consists of the following books:')
                            print('\n')
                            for i in cart:
                                 print(i[2:])
                            print('cost',cost)
                            break
                    elif ch==3:
                        science()
                        print('\n')
                        print('loading....')
                        print('\n')
                        print('\n')
                        print('select books choice')
                        print('\n')
                        num=int(input('how many books do you want to buy'))
                        print('\n')
                        g=1
                        while g<=num:
                            cho=int(input('enter choice of science books'))
                            print('\n')
                            f7=open(r"C:\Users\pavitra\Desktop\pavitra python\science.txt",'r+')
                            for i in f7:
                                j=i.split()
                                if int(j[0])==cho:
                                    cart.append(i)
                                    cost+= int(j[-1])
                                    g+=1
                        ast=input('want to buy more books enter yes or no')
                        print('\n')
                        if ast=='no':
                            print('your cart consists of the following books:')
                            print('\n')
                            for i in cart:
                                 print(i[2:])
                            print('cost',cost)
                            break    
                    else:
                        print('your cart consists of the following books:')
                        print('\n')
                        for i in cart:
                            print(i[2:])
                        print('cost',cost)
                        break
            else:
                print('your cart consists of the following books:')
                print('\n')
                for i in cart:
                     print(i[2:])
                print('cost',cost)
            allbooks(name,cart,cost)
            pl=input('do you want to continue using the site y/n')
            print('\n')
            if pl=='n':
                break
