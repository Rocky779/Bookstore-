## Online Bookstore 
The Online Book Sale project utilizes and involves the following Python topics :

1)DATA FILE HANDLING

2)USER-DEFINED AND BUILT-IN FUNCTIONS

3)LOOPS AND VARIABLES

4)Python-Mysql connectivity.[bookstore.pdf](https://github.com/Rocky779/Bookstore-/files/10812163/bookstore.pdf)


This Project allows the User to go with either of three options:

1)Login as an admin: This option is available only for those who have the
admin username and password which is already defined as a variable in the
python code. Logging in as an admin will allow the admin to check the number
of customers who logged into their account to buy books , the different books
which they purchase and the total cost of the purchase. The admin is also
provided with the option to delete an account of a user .


2)Create an Account: With the help of option , the user gets an opportunity to
create a free account . Once the User has created the account , the user is
provided with a wide variety of books of many generes .Once the desired book
is selected, the user can choose to exit and get the total cost.

3)Use a created account: With the help of this option, the user can login with
the e-mail address and the password. Once the User is logged in his/her account
, the user is provided with a wide variety of books of many generes .Once the
desired book is selected, the user can choose to exit and get the total cost.

## INCORPORATED DECLARED VARIABLES:

1)f1: This is a file created to store information of the accounts created.

2) f3: This is a file created to store the name of the customer.

3) f4: This is a file created to store information the different generas of books .

4) f5: This is a file created to store information of the adventure books.

5) f6: This is a file created to store information of the myster y books.

6) f7: This is a file created to store information of the science books.

7)cart: This is a list used to store information of the books bought by the
customer.

8)cost: It stores to total cost of the books bought by the customer.

9)ask: Asks the user to choose an option to create an account or use a created
account.

10)num: number of books the user wants to buy

11)name:accepts the name of the user.

12)email:accepts the email address of the user.

13)password:accepts the password of the user.

14)en: asks the user if he/she wants to buy more books.

15)ch: asks the user to enter the choice of book.

16)choice: allows the admin to make a choice between viewing the account credentials of the users or viewing the purchase details of the users.

17)change: allows the admin to make a choice between deleting a user’s account or not deleting it.

18)q: used for storing the query to be executed using Python Mysql Connectivity.

## INCORPORATED USER-DEFINED FUNCTIONS

1)Fold(n):takes name of the user as a parameter and writes it into the file that stores the name of the customers.

2)Generes(): reads all the contents of the generes file.

3)Adventure():reads all the contents of the adventure file.

4)Mystery():reads all the contents of the mystery file.

5)Science():reads all the contents of the science file.

6)alldetails(n,e,p):takes name n , email e , password p as the parameters and concatenates the three into a single variable and writes that details of the customer into the allaccounts file.

7)Permanentstorage(n,e,p): This function stores all the login credentials of the customer into the allaccounts table in the Mysql database.

8)Allbooks(n,l,c):This function stores all the details of the purchase made by the customer in the alldetails table in the Mysql database

The following document contains the screenshots of the output of this program [bookstore.pdf](https://github.com/Rocky779/Bookstore-/files/10812169/bookstore.pdf)
