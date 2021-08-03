#SOURCE CODE FOR School MANAGEMENT
print("****School Management System****")

#creating database
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="password")
mycursor=mydb.cursor()
mycursor.execute("create database if not exists pyschool")
#mycursor.execute("------------------------------------")
mycursor.execute("use pyschool")
#creating required tables 
mycursor.execute("create table if not exists pystudent(name varchar(50) not null,class varchar(25) not null,roll_no varchar(25),gender char(1))")
#mycursor.exeute("create table if not exists pystudent(name varchar(50) not null, class varchar(25) not null, roll_no varchar(25) not null, gender char(1) not null)")
mycursor.execute("create table if not exists pystaff(name varchar(50) not null,gender char(1),subject varchar(25) not null,Salary varchar(25))")
mydb.commit()
while(True):    
    print("1=Enter Data for new student")
    print("2=Enter Data for new Staff Data")
    print("3=Search Student Data")
    print("4=Search Staff Data")
    print("5=Remove student record")
    print("6=Remove staff record")
    print("7=Exit")
    ch=int(input("Enter your choice:"))
    
#to create new entry for student
    if(ch==1):
        print("All information prompted are mandatory to be filled")
        name=input("Enter name(limit 35 characters):")
        classs=str(input("Enter Class:"))
        #classs=input("Enter class: ")
        roll_no=str(input("Enter Roll Number:"))
        gender=str(input("Enter Gender(M/F):"))
        mycursor.execute("insert into pystudent values('"+name+"','"+classs+"','"+roll_no+"','"+gender+"')")
        #mycursor.execute("insert into pystudent values('"++"')")
        mydb.commit()
        print("Student record has been saved successfully!!")
        
#to create new entry for staff
    elif(ch==2):
        sname=str(input("Enter Staff member name:"))
        gender=str(input("Enter Gender(M/F):"))
        dep=str(input("Enter department or subject:"))
        sal=int(input("Enter Salary"))
        mycursor.execute("insert into pystaff values('"+sname+"','"+gender+"','"+dep+"','"+str(sal)+"')")
        mydb.commit()
        print("Staff record has been saved successfully!!!")

#display student info
    elif(ch==3):
        roll_no=str(input("Enter student roll_no:"))
        mycursor.execute("select * from pystudent where roll_no='"+roll_no+"'")
        #mycursor.execute("select * from pystudent where roll_no='"+variable name+"'")
        for i in mycursor:
            name,classs,roll_no,gender=i
            #name,classs,rno,gender=[(name),(classs),(roll_no),(gender)]
            #print(f"name:- {name}")
            print(f'Name:- {name}')
            print(f'Class:- {classs}')
            print(f'Roll Number:- {roll_no}')
            print(f'gender:- {gender}')

#display staff info
    elif(ch==4):
        name=str(input("Enter Name"))
        mycursor.execute("select * from pystaff where name='"+name+"'")
        for i in mycursor:#[(name),(gender),(dep),(sal),()]
            name,gender,dep,sal=i
            print(f"Name:- {name}")
            print(f"gender:- {gender}")
            print(f"departmant:- {dep}")
            print(f"sal:- {sal}")
#delete student
    elif(ch==5):
        r_no=str(input("Enter Roll Number"))
        mycursor.execute("delete from pystudent where roll_no='"+r_no+"'")
        mydb.commit()
        print("Student Record is successfully Deleted")
#delete staff
    elif(ch==6):
        name=str(input("Enter Name"))
        mycursor.execute("delete from pystaff where name='"+name+"'")
        mydb.commit()
        print("Staff Record is successfully Deleted")
    elif(ch==7):
        break
        
        
