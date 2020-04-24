#Banking
import sqlite3
conn=sqlite3.connect("Bank.db")
cur=conn.cursor()
#Open Account in Bank 
def Accountopening():
    applicationo=int(input("Enter Application number:-"))
    fullname=str(input("Enter Full name of user:-"))
    mobileno=int(input("Enter Mobileno with country code:--"))
    address=str(input("Enter the Address:-"))
    city=str(input("Enter the city:-"))
    pincode=int(input("Enter the pincode:-"))
    initialbalance=int(input("How much amount you are deposit in your account:-"))
    cur.execute('''insert into bank(Applicantno,Fullname,Mobileno,Address,City,Pincode,InitialBalance)values(?,?,?,?,?,?,?)''',(applicationo,fullname,mobileno,address,city,pincode,initialbalance))
    conn.commit()
    conn.close()
#Check the balanace
def checkbalance():
    appno=int(input("Enter the Applicant number:-"))
    cur.execute('''select Fullname,InitialBalance from bank where Applicantno=?''',(appno,))
    record=cur.fetchone()
    #Select Column value
    Name=str(record[0])
    money=float(record[1])
    print("Your Name:-",Name)
    print("Your Account balance:::-",money)
    conn.commit()
    conn.close()
#Withdrwal money from bank
def withdrawal():
    appno=int(input("Enter your application number:--"))
    withdrawalmoney=int(input("How much money withdrawal in your account:::-"))
    cur.execute('''select InitialBalance from bank where Applicantno=?''',(appno,))
    amount=cur.fetchone()
    #withdrawal
    money=float(amount[0])
    totalmoney=money-withdrawalmoney
    print("Remaining Balance::-",totalmoney)
    cur.execute('''update bank set InitialBalance=? where Applicantno=?''',(totalmoney,appno,))
    conn.commit()
    conn.close()
#Deposit Money
def deposit():
    appno=int(input("Enter your application number:--"))
    depositmoney=int(input("How much money deposit in your account:::-"))
    cur.execute('''select InitialBalance from bank where Applicantno=?''',(appno,))
    amount=cur.fetchone()
    #Deposit
    money=float(amount[0])
    totalmoney=money+depositmoney
    print("Updated Balance::-",totalmoney)
    cur.execute('''update bank set InitialBalance=? where Applicantno=?''',(totalmoney,appno,))
    conn.commit()
    conn.close()
#update user information
def updatename():
    appno=int("Enter your application number::-")
    newname=str(input("Enter new name::-"))
    cur.execute('''select Fullname from bank where Applicantno=?''',(appno,))
    fname=cur.fetchone()
    #newname
    name=str(fname[0])
    name=newname
    cur.execute('''update bank set Fullname=? where Applicantno=?''',(name,appno,))
    print("Name Successfully updated......")
    conn.commit()
    conn.close()
def updateaddress():
    appno=int(input("Enter your Application number::-"))
    newaddress=str(input("Enter the new address::-"))
    cur.execute('''select Address from bank where Applicantno=?''',(appno,))
    naddress=cur.fetchone()
    #New Address
    add=str(naddress[0])
    add=newaddress
    cur.execute('''update bank set Address=? where Applicantno=?''',(add,appno,))
    print("Address Successfully updated......")
    conn.commit()
    conn.close()
def updatecity():
    appno=int(input("Enter your Application number::-"))
    newcity=str(input("Enter the new new city::-"))
    newpincode=int(input("Enter new Pincode:::-"))
    cur.execute('''select City,Pincode from bank where Applicantno=?''',(appno,))
    newcipin=cur.fetchone()
    #New city and picode
    cty=str(newcipin[0])
    pin=int(newcipin[1])
    cty=newcity
    pin=newpincode
    cur.execute('''update bank set City=? where Applicantno=?''',(cty,appno,))
    cur.execute('''update bank set Pincode=? where Applicantno=?''',(pin,appno,))
    print("City and Pincode Successfully updated......")
    conn.commit()
    conn.close()
def updatephoneno():
    appno=int(input("Enter your Application number::-"))
    newphoneno=str(input("Enter the new Mobile number::-"))
    cur.execute('''select Mobileno from bank where Applicantno=?''',(appno,))
    nphone=cur.fetchone()
    #New Address
    phone=int(nphone[0])
    phone=newphoneno
    cur.execute('''update bank set Mobileno=? where Applicant=?''',(phone,appno,))
    print("Mobile Number Successfully updated......")
    conn.commit()
    conn.close()
#Bank service Details
user=str(input("Are you new user in bank?"))
if user=='y':
    Accountopening()
else:
    print("1.Check Balance \n 2.Withdrawal money \n 3.Deposit money \n 4.Information Update \n 5.exit")
    Choice=int(input("Enter the your choice::---"))
    if Choice==1:
        checkbalance()
    elif Choice==2:
        withdrawal()
    elif Choice==3:
        deposit()
    elif Choice==4:
        print("A.Change Name \n 2.Change Address \n 3.Change City \n 4.Change PhoneNo.")
        Choice1=int(input("Enter the Choice::-"))
        if Choice1==1:
            updatename()
        elif Choice1==2:
            updateaddress()
        elif Choice1==3:
            updatecity()
        elif Choice1==4:
            updatephoneno()
        else:
            print("Thank You for updation.......")
    else:
        print("Thank you for using banking services.........")