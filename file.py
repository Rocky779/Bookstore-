import mysql.connector
mycon=mysql.connector.connect(host=&#39;localhost&#39;,user=&#39;root&#39;,passwd=&#39;pavitra&#39;,database=&#39;pavitra&#39;)
mycursor=mycon.cursor()
f1=open(r&quot;C:\Users\pavitra\Desktop\pavitra python\all accounts.txt&quot;,&#39;w&#39;)
rec=&#39;NAME&#39;+&quot; &quot;+&#39;EMAIL ADDRESS&#39;+&quot; &quot;+&quot;PASSWORD&quot;
nrec=rec+&#39;\n&#39;
f1.write(nrec)
f1.close()
f3=open(r&quot;C:\Users\pavitra\Desktop\pavitra python\buy.txt&quot;,&#39;w+&#39;)
rec=&#39;NAME&#39;
f3.write(rec)
f3.write(&#39;\n&#39;)
f3.close()
f4=open(r&quot;C:\Users\pavitra\Desktop\pavitra python\generes.txt&quot;,&#39;w+&#39;)
f4.write(&#39;1.adventure&#39;)
f4.write(&#39;\n&#39;)
f4.write(&#39;2.mystery&#39;)
f4.write(&#39;\n&#39;)
f4.write(&#39;3.science&#39;)
f4.close()
f5=open(r&quot;C:\Users\pavitra\Desktop\pavitra python\adventure.txt&quot;,&#39;w+&#39;)
f5.write(&#39;1 . ADVENTURE OF NARNIA of $ 15&#39;)
f5.write(&#39;\n&#39;)
f5.write(&#39;2 . LORD OF THE RINGS of $ 20&#39;)
f5.write(&#39;\n&#39;)
f5.write(&#39;3 . HARRY POTTER:DEATHLY HALLOWS of $ 25&#39;)
f5.close()

f6=open(r&quot;C:\Users\pavitra\Desktop\pavitra python\mystery.txt&quot;,&#39;w+&#39;)
f6.write(&#39;1 . magic tree house of $ 15&#39;)
f6.write(&#39;\n&#39;)

f6.write(&#39;2 . dan brown 1 of $ 20&#39;)
f6.write(&#39;\n&#39;)
f6.write(&#39;3 . dan brown 2 of $ 25&#39;)
f6.close()

f7=open(r&quot;C:\Users\pavitra\Desktop\pavitra python\science.txt&quot;,&#39;w+&#39;)
f7.write(&#39;1 . physics of $ 15&#39;)
f7.write(&#39;\n&#39;)
f7.write(&#39;2 . chemistry of $ 20&#39;)
f7.write(&#39;\n&#39;)
f7.write(&#39;3 . Biology of $ 30&#39;)
f7.close()

def fold(n):
f3=open(r&quot;C:\Users\pavitra\Desktop\pavitra python\buy.txt&quot;,&#39;r+&#39;)
f3.write(n)
f3.close()
def generes():
f4=open(r&quot;C:\Users\pavitra\Desktop\pavitra python\generes.txt&quot;,&#39;r+&#39;)
x=f4.read()
print(x)
f4.close()

def adventure():
f5=open(r&quot;C:\Users\pavitra\Desktop\pavitra python\adventure.txt&quot;,&#39;r+&#39;)
x=f5.read()
print(x)
f5.close()

def mystery():
f6=open(r&quot;C:\Users\pavitra\Desktop\pavitra python\mystery.txt&quot;,&#39;r+&#39;)
y=f6.read()
print(y)
f6.close()
def science():
f7=open(r&quot;C:\Users\pavitra\Desktop\pavitra python\science.txt&quot;,&#39;r+&#39;)
z=f7.read()
print(z)
f7.close()
def alldetails(n,e,p):
f1=open(r&quot;C:\Users\pavitra\Desktop\pavitra python\all accounts.txt&quot;,&#39;a&#39;)
rec=n+&quot; &quot;+e+&quot; &quot;+p
nrec=rec+&#39;\n&#39;
f1.write(nrec)
def permanentstorage(n,e,p):
q=&quot;insert into allaccounts values(&#39;{}&#39;,&#39;{}&#39;,&#39;{}&#39;)&quot;.format(n,e,p)
mycursor.execute(q)
mycon.commit()
def allbooks(n,l,c):
r=&quot; &quot;
for i in l:
if len(i)&gt;10:
a=i[4:10]
r=r+a
else:
a=i+&quot; &quot;
r=r+a

q=&quot;insert into accountdetails values(&#39;{}&#39;,&#39;{}&#39;,{})&quot;.format(n,r,c)
mycursor.execute(q)

mycon.commit()

e=0
while True:
cart=[]
cost=0
print(&#39;ADMIN?? ..... LOGIN TO SEE THE DETAILS&#39;)
print(&#39;\n&#39;)
print(&#39;\n&#39;)
print(&#39;HAVE AN ACCOUNT &#39;)
print(&#39;\n&#39;)
print(&#39;\n&#39;)
print(&#39;WANT TO CREATE AN ACCOUNT &#39;)
print(&#39;\n&#39;)
print(&#39;\n&#39;)
ask=input(&#39;enter EXISTS or CREATE OR ADMIN&#39;)
print(&#39;\n&#39;)
print(&#39;\n&#39;)
if ask==&#39;ADMIN&#39;:
print(&#39;HELLO ADMIN PLEASE ENTER THE :&#39;)
u=&#39;admin@gmail.com&#39;
p=&#39;abcd&#39;
user=input(&#39;enter username&#39;)
passwd=input(&#39;enter password&#39;)
if user==u and passwd==p:
print(&#39;WELCOME TO YOUR ADMIN ACCOUNT&#39;)
print(&#39;\n&#39;)
print(&#39;\n&#39;)
while True:

choice=input(&#39;DO YOU WANT TO SEE ALL ACCOUNTS PRESS A OR YOU WANT TO SEE ALL
DETAILS PRESS P&#39;)
if choice==&#39;A&#39;:
mycursor.execute(&quot;select * from allaccounts&quot;)
mydata=mycursor.fetchall()
for i in mydata:
print(i)
print(&#39;THERE YOU GO&#39;)
change=input(&#39;DO YOU WANT TO DELETE ANY RECORDS PRESS D OR PRESS N&#39;)
if change==&#39;D&#39;:
na=input(&#39;input the name to be deleted&#39;)
q=&quot;delete from allaccounts where name=&#39;{}&#39;&quot;.format(na)
q1=&quot;delete from accountdetails where name=&#39;{}&#39;&quot;.format(na)
mycursor.execute(q)
mycursor.execute(q1)
mycon.commit()
mycursor.execute(&quot;select * from allaccounts&quot;)
mydata=mycursor.fetchall()
for i in mydata:
print(i)
print(&#39;THERE YOU GO&#39;)
else:
pass
ch=input(&#39;continue admin account press c or logout press l&#39;)
if ch==&#39;c&#39;:
pass
else:
break
elif choice==&#39;P&#39;:
mycursor.execute(&quot;select * from accountdetails&quot;)
mydata=mycursor.fetchall()

for i in mydata:
print(i)
print(&#39;THERE YOU GO&#39;)
ch=input(&#39;continue admin account press c or logout press l&#39;)
if ch==&#39;c&#39;:
pass
else:
break
pl=input(&#39;do you want to continue using the site y/n&#39;)
print(&#39;\n&#39;)
if pl==&#39;n&#39;:
break

elif ask==&#39;EXISTS&#39;:
print(&#39;Please sign in&#39;)
print(&#39;\n&#39;)
f1=open(r&quot;C:\Users\pavitra\Desktop\pavitra python\all accounts.txt&quot;,&#39;r&#39;)
name=input(&#39;NAME&#39;)
print(&#39;\n&#39;)
email=input(&#39;EMAIL ADDRESS&#39;)
print(&#39;\n&#39;)
password=input(&#39;PASSWORD&#39;)
print(&#39;\n&#39;)
permanentstorage(name,email,password)
mycursor.execute(&#39;select * from allaccounts&#39;)
mydata=mycursor.fetchall()

for k in mydata:
if k[0]==name and k[1]==email and k[2]==password:
print(&#39;account found&#39; )
break

else:
print(&#39;sorry account does not exist&#39;)
print(&#39;\n&#39;)
print(&#39;please create a new account&#39;)
print(&#39;\n&#39;)
print(&#39;your account is created please proceed&#39;)
print(&#39;\n&#39;)
fold(name)
print(&#39;HELLO&#39;,name,&#39;WANT TO BUY BOOKS&#39;)
print(&#39;\n&#39;)
en=input(&#39;enter yes or no&#39;)
if en==&#39;yes&#39;:
generes()
l=0
while True:
ch=int(input(&#39;enter the choice&#39;))
print(&#39;\n&#39;)
if ch==1:
adventure()
print(&#39;\n&#39;)
print(&#39;loading....&#39;)
print(&#39;\n&#39;)
print(&#39;\n&#39;)
print(&#39;select books choice&#39;)
print(&#39;\n&#39;)

num=int(input(&#39;how many books do you want to buy&#39;))
print(&#39;\n&#39;)
g=1
while g&lt;=num:
cho=int(input(&#39;enter choice of adventure books&#39;))
print(&#39;\n&#39;)
f5=open(r&quot;C:\Users\pavitra\Desktop\pavitra python\adventure.txt&quot;,&#39;r+&#39;)
for i in f5:
j=i.split()
if int(j[0])==cho:
cart.append(i)
cost+=int(j[-1])
g+=1
else:
pass
ast=input(&#39;want to buy more books enter yes or no&#39;)
print(&#39;\n&#39;)
if ast==&#39;no&#39;:
print(&#39;your cart consists of the following books:&#39;)
print(&#39;\n&#39;)
for i in cart:
print(i[2:])
print(&#39;cost&#39;,cost)
break
elif ch==2:
mystery()
print(&#39;\n&#39;)
print(&#39;loading....&#39;)
print(&#39;\n&#39;)
print(&#39;\n&#39;)
print(&#39;select books choice&#39;)

print(&#39;\n&#39;)
num=int(input(&#39;how many books do you want to buy&#39;))
print(&#39;\n&#39;)
g=1
while g&lt;=num:
cho=int(input(&#39;enter choice of mystery books&#39;))
f6=open(r&quot;C:\Users\pavitra\Desktop\pavitra python\mystery.txt&quot;,&#39;r+&#39;)
for i in f6:
j=i.split()
if int(j[0])==cho:
cart.append(i)
cost+=int(j[-1])
g+=1
ast=input(&#39;want to buy more books enter yes or no&#39;)
print(&#39;\n&#39;)
if ast==&#39;no&#39;:
print(&#39;your cart consists of the following books:&#39;)
print(&#39;\n&#39;)
for i in cart:
print(i[2:])
print(&#39;cost&#39;,cost)
break
elif ch==3:
science()
print(&#39;\n&#39;)
print(&#39;loading....&#39;)
print(&#39;\n&#39;)
print(&#39;\n&#39;)
print(&#39;select books choice&#39;)
print(&#39;\n&#39;)
num=int(input(&#39;how many books do you want to buy&#39;))

print(&#39;\n&#39;)
g=1
while g&lt;=num:
cho=int(input(&#39;enter choice of science books&#39;))
print(&#39;\n&#39;)
f7=open(r&quot;C:\Users\pavitra\Desktop\pavitra python\science.txt&quot;,&#39;r+&#39;)
for i in f7:
j=i.split()
if int(j[0])==cho:
cart.append(i)
cost+= int(j[-1])
g+=1
ast=input(&#39;want to buy more books enter yes or no&#39;)
print(&#39;\n&#39;)
if ast==&#39;no&#39;:
print(&#39;your cart consists of the following books:&#39;)
print(&#39;\n&#39;)
for i in cart:
print(i[2:])
print(&#39;cost&#39;,cost)
break
else:
print(&#39;your cart consists of the following books:&#39;)
print(&#39;\n&#39;)
for i in cart:
print(i[2:])
print(&#39;cost&#39;,cost)
break
else:
print(&#39;your cart consists of the following books:&#39;)
print(&#39;\n&#39;)

for i in cart:
print(i)
print(&#39;cost&#39;,cost)
allbooks(name,cart,cost)
pl=input(&#39;do you want to continue using the site y/n&#39;)
print(&#39;\n&#39;)
if pl==&#39;n&#39;:
break

elif ask==&#39;CREATE&#39;:
print(&#39;Please create an account...&#39;)
print(&#39;\n&#39;)
r=1
name=input(&#39;NAME&#39;)
print(&#39;\n&#39;)
email=input(&#39;EMAIL ADDRESS&#39;)
print(&#39;\n&#39;)
password=input(&#39;PASSWORD&#39;)
print(&#39;\n&#39;)
alldetails(name,email,password)
fold(name)
permanentstorage(name,email,password)
print(&#39;HELLO&#39;,name,&#39;WANT TO BUY BOOKS&#39;)
print(&#39;\n&#39;)
en=input(&#39;enter yes or no&#39;)
print(&#39;\n&#39;)
if en==&#39;yes&#39;:
generes()
l=0
while True:
ch=int(input(&#39;enter the choice&#39;))

print(&#39;\n&#39;)
if ch==1:
adventure()
print(&#39;\n&#39;)
print(&#39;loading....&#39;)
print(&#39;\n&#39;)
print(&#39;\n&#39;)
print(&#39;select books choice&#39;)
print(&#39;\n&#39;)
num=int(input(&#39;how many books do you want to buy&#39;))
print(&#39;\n&#39;)
g=1
while g&lt;=num:
cho=int(input(&#39;enter choice of adventure books&#39;))
print(&#39;\n&#39;)
f5=open(r&quot;C:\Users\pavitra\Desktop\pavitra python\adventure.txt&quot;,&#39;r+&#39;)
for i in f5:
j=i.split()
if int(j[0])==cho:
cart.append(i)
cost+=int(j[-1])
g+=1
else:
pass
ast=input(&#39;want to buy more books enter yes or no&#39;)
print(&#39;\n&#39;)
if ast==&#39;no&#39;:
print(&#39;your cart consists of the following books:&#39;)
print(&#39;\n&#39;)
for i in cart:
print(i[2:])

print(&#39;cost&#39;,cost)
break
elif ch==2:
mystery()
print(&#39;\n&#39;)
print(&#39;loading....&#39;)
print(&#39;\n&#39;)
print(&#39;\n&#39;)
print(&#39;select books choice&#39;)
print(&#39;\n&#39;)
num=int(input(&#39;how many books do you want to buy&#39;))
print(&#39;\n&#39;)
g=1
while g&lt;=num:
cho=int(input(&#39;enter choice of mystery books&#39;))
print(&#39;\n&#39;)
f6=open(r&quot;C:\Users\pavitra\Desktop\pavitra python\mystery.txt&quot;,&#39;r+&#39;)
for i in f6:
j=i.split()
if int(j[0])==cho:
cart.append(i)
cost+=int(j[-1])
g+=1
ast=input(&#39;want to buy more books enter yes or no&#39;)
print(&#39;\n&#39;)
if ast==&#39;no&#39;:
print(&#39;your cart consists of the following books:&#39;)
print(&#39;\n&#39;)
for i in cart:
print(i[2:])
print(&#39;cost&#39;,cost)

break
elif ch==3:
science()
print(&#39;\n&#39;)
print(&#39;loading....&#39;)
print(&#39;\n&#39;)
print(&#39;\n&#39;)
print(&#39;select books choice&#39;)
print(&#39;\n&#39;)
num=int(input(&#39;how many books do you want to buy&#39;))
print(&#39;\n&#39;)
g=1
while g&lt;=num:
cho=int(input(&#39;enter choice of science books&#39;))
print(&#39;\n&#39;)
f7=open(r&quot;C:\Users\pavitra\Desktop\pavitra python\science.txt&quot;,&#39;r+&#39;)
for i in f7:
j=i.split()
if int(j[0])==cho:
cart.append(i)
cost+= int(j[-1])
g+=1
ast=input(&#39;want to buy more books enter yes or no&#39;)
print(&#39;\n&#39;)
if ast==&#39;no&#39;:
print(&#39;your cart consists of the following books:&#39;)
print(&#39;\n&#39;)
for i in cart:
print(i[2:])
print(&#39;cost&#39;,cost)
break

else:
print(&#39;your cart consists of the following books:&#39;)
print(&#39;\n&#39;)
for i in cart:
print(i[2:])
print(&#39;cost&#39;,cost)
break
else:
print(&#39;your cart consists of the following books:&#39;)
print(&#39;\n&#39;)
for i in cart:
print(i[2:])
print(&#39;cost&#39;,cost)
allbooks(name,cart,cost)
pl=input(&#39;do you want to continue using the site y/n&#39;)
print(&#39;\n&#39;)
if pl==&#39;n&#39;:
break
