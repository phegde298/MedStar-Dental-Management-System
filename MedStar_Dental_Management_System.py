#IMPORTS
from tabulate import tabulate
import datetime
import sys


#MYSQL PYTHON CONNECTIVITY
import mysql.connector as mycon
con = mycon.connect(host = "localhost", user = "root", password = "home", database = "dental")
if con.is_connected():
    print("connected successfully.")
cursor = con.cursor()



#HOME PAGE
def home_page():
    print('╔═════════════════════════════════════════════════════════╗')
    print('║                                                         ║')
    print('║             welcome to Medstar Dental Clinic!           ║')
    print('║                                                         ║')
    print('╚═════════════════════════════════════════════════════════╝')
    d=datetime.date.today()
    t=datetime.datetime.now()
    print("╔═════════════════════════════════════════════════════════╗")
    print()
    print("          Date: ",d.strftime("%A, %d %B %Y"))
    print("                                                           ")
    print("          Time: ",t.strftime("%H:%M:%S"))
    print()
    print("╚═════════════════════════════════════════════════════════╝")
    print("┌─────────────────────────────────────────────────────────┐")
    print("│             1. doctors                                  │")
    print("│             2. patients                                 │")
    print("│             3. about us                                 │")
    print("│             4. log out                                  │")
    print('└─────────────────────────────────────────────────────────┘')
    print()
    print()
    ctg = int(input("select category: "))
    if ctg == 1:
        doc_menu()
    elif ctg == 2:
        patient_menu()
    elif ctg == 3:
        about_us()
    elif ctg == 4:
        logout()
    else:
        invalid_input()
    
    
    
#DOCTOR MENU
def doc_menu():
    print("┌─────────────────────────────────────────────────────────┐")
    print("│             1. view doctors                             │")
    print("│             2. add doctor                               │")
    print("│             3. edit doctor                              │")
    print("│             4. remove doctor                            │")
    print("│             5. exit                                     │")
    print('└─────────────────────────────────────────────────────────┘')
    ch = int(input("enter option: "))
        
    if ch == 1:
        view_doc()
    elif ch == 2:
        new_doc()
    elif ch == 3:
        edit_doc()
    elif ch == 4:
        del_doc()
    elif ch == 5:
        home_page()
    else:
        invalid_input()



#VIEW DETAILS OF THE DOCTORS
def view_doc():
    print('┌─────────────────────────────────────────────────────────┐')
    print('│                       view doctors                      │')                                        
    print('└─────────────────────────────────────────────────────────┘')
    qry = "select * from doctors"
    cursor.execute(qry)
    doclist = cursor.fetchall()
    fields = ['doc id', 'DOJ', 'name', 'salary']
    print(tabulate(doclist, headers = fields))
    ch = int(input("to exit, press 1: "))
    if ch == 1:
        print('┌─────────────────────────────────────────────────────────┐')
        print('│                   returning back to menu                │')                                        
        print('└─────────────────────────────────────────────────────────┘')
        doc_menu()
    else:
        invalid_input()



#ADD A NEW DOCTOR
def new_doc():
    print(" add doctor ")
    print('┌─────────────────────────────────────────────────────────┐')
    print('│                       add doctor                        │')                                        
    print('└─────────────────────────────────────────────────────────┘')
    docID = int(input("doc id: "))
    DOJ = input("DOJ: ")
    name = input("name: ")
    sal = int(input("salary: "))
    new = (docID, DOJ, name, sal)
    qry = "insert into doctors values(%s, %s, %s, %s)"
    cursor.execute(qry, new)
    con.commit()
    print('┌─────────────────────────────────────────────────────────┐')
    print('│                      doctor added                       │')                                        
    print('└─────────────────────────────────────────────────────────┘')
    
    ch = input("press 0 to exit: ")
    if ch == '0':
        print('┌─────────────────────────────────────────────────────────┐')
        print('│                   returning back to menu                │')                                        
        print('└─────────────────────────────────────────────────────────┘')
        doc_menu()
    else:
        invalid_input()



#EDIT DETAILS OF EXISTING DOCTORS
def edit_doc():
    ch = int(input("enter id: "))
    qry = "select * from doctors where doctor_id = %s"
    cursor.execute(qry,[ch])
    rlt = cursor.fetchall()
    if len(rlt) == 0:
        print('┌─────────────────────────────────────────────────────────┐')
        print('│              error occurred, doctor not found           │')                                        
        print('└─────────────────────────────────────────────────────────┘')
    else:
        print("┌─────────────────────────────────────────────────────────┐")
        print("│             1. edit DOJ                                 │")
        print("│             2. edit doctor name                         │")
        print("│             3. edit salary                              │")
        print('└─────────────────────────────────────────────────────────┘')
        opt = int(input("enter option: "))
        if opt == 1:
            DOJ = input("update DOJ: ")
            qry2 = "update doctors set DOJ = %s where doctor_id = %s"
            cursor.execute(qry2,[DOJ, ch])
            con.commit()
            print('┌─────────────────────────────────────────────────────────┐')
            print('│                     updated successfully                │')                                        
            print('└─────────────────────────────────────────────────────────┘')
            ch = int(input("press 1 to exit: "))
            if ch == 1:
                print('┌─────────────────────────────────────────────────────────┐')
                print('│                 returning back to menu                  │')                                        
                print('└─────────────────────────────────────────────────────────┘')
                doc_menu()
            else:
                invalid_input()
        if opt == 2:
            name = input("update name: ")
            qry2 = "update doctors set name = %s where doctor_id = %s"
            cursor.execute(qry2, [name, ch])
            con.commit()
            print('┌─────────────────────────────────────────────────────────┐')
            print('│                    updated successfully                 │')                                        
            print('└─────────────────────────────────────────────────────────┘')
            ch = int(input("press 1 to exit: "))
            if ch == 1:
                print('┌─────────────────────────────────────────────────────────┐')
                print('│                  returning back to menu                 │')                                        
                print('└─────────────────────────────────────────────────────────┘')
                doc_menu()
            else:
                invalid_input()
        if opt == 3:
            sal = int(input("update salary: "))
            qry2 = "update doctors set salary = %s where doctor_id = %s"
            cursor.execute(qry2, [sal, ch])
            con.commit()
            print('┌─────────────────────────────────────────────────────────┐')
            print('│                    updated successfully                 │')                                        
            print('└─────────────────────────────────────────────────────────┘')
            ch = int(input("press 1 to exit: "))
            if ch == 1:
                print('┌─────────────────────────────────────────────────────────┐')
                print('│                  returning back to menu                 │')                                        
                print('└─────────────────────────────────────────────────────────┘')
                doc_menu()
            else:
                invalid_input()



#REMOVE AN EXISTING DOCTOR
def del_doc():
    print('┌─────────────────────────────────────────────────────────┐')
    print('│                        remove doctor                    │')                                        
    print('└─────────────────────────────────────────────────────────┘')
    docID = input("enter doc id: ")
    qry = "delete from doctors where doctor_id = %s"
    cursor.execute(qry,[docID])
    con.commit()
    print('┌─────────────────────────────────────────────────────────┐')
    print('│                       doctor removed                    │')                                        
    print('└─────────────────────────────────────────────────────────┘')
    ch = int(input("press 1 to exit: "))
    if ch == 1:
        print('┌─────────────────────────────────────────────────────────┐')
        print('│                  returning back to menu                 │')                                        
        print('└─────────────────────────────────────────────────────────┘')
        doc_menu()
    else:
        invalid_input()



#PATIENT MENU
def patient_menu():
    print("┌─────────────────────────────────────────────────────────┐")
    print("│             1. view patients                            │")
    print("│             2. add patient                              │")
    print("│             3. edit patient                             │")
    print("│             4. remove patient                           │")
    print("│             5. exit                                     │")
    print('└─────────────────────────────────────────────────────────┘')
        
    ch = int(input("enter option: "))
    if ch == 1:
        view_patient()
    elif ch == 2:
        new_patient()
    elif ch == 3:
        edit_patient()
    elif ch == 4:
        del_patient()
    elif ch == 5:
        home_page()
    else:
        invalid_input()



#VIEW DETAILS OF THE PATIENTS
def view_patient():
    print('┌─────────────────────────────────────────────────────────┐')
    print('│                       view patient                      │')                                        
    print('└─────────────────────────────────────────────────────────┘')
    qry = "select * from patients"
    cursor.execute(qry)
    ptlist = cursor.fetchall()
    fields = ['patient id', 'date', 'name', 'fee']
    print(tabulate(ptlist, headers = fields))
    ch = int(input("to exit, press 1: "))
    if ch == 1:
        print('┌─────────────────────────────────────────────────────────┐')
        print('│                   returning back to menu                │')                                        
        print('└─────────────────────────────────────────────────────────┘')
        patient_menu()
    else:
        invalid_input()



#ADD A NEW PATIENT
def new_patient():
    print('┌─────────────────────────────────────────────────────────┐')
    print('│                        add patient                      │')                                        
    print('└─────────────────────────────────────────────────────────┘')
    ptid = int(input("patient id: "))
    date = input("date: ")
    name = input("name: ")
    fee = int(input("fee: "))
    new = (ptid, date, name, fee)
    qry = "insert into patients values(%s, %s, %s, %s)"
    cursor.execute(qry, new)
    con.commit()
    print('┌─────────────────────────────────────────────────────────┐')
    print('│                        patient added                    │')                                        
    print('└─────────────────────────────────────────────────────────┘')
    ch = input("press 0 to exit: ")
    if ch == '0':
        print('┌─────────────────────────────────────────────────────────┐')
        print('│                  returning back to menu                 │')                                        
        print('└─────────────────────────────────────────────────────────┘')
        patient_menu()
    else:
        invalid_input()



#EDIT DETAILS OF EXISTING PATIENTS
def edit_patient():
    ch = int(input("enter id: "))
    qry = "select * from patients where patient_id = %s"
    cursor.execute(qry,[ch])
    rlt = cursor.fetchall()
    if len(rlt) == 0:
        print('┌─────────────────────────────────────────────────────────┐')
        print('│           error occurred, patient not found             │')                                        
        print('└─────────────────────────────────────────────────────────┘')
    else:
        print("┌─────────────────────────────────────────────────────────┐")
        print("│             1. edit date                                │")
        print("│             2. edit patient name                        │")
        print("│             3. edit fee                                 │")
        print('└─────────────────────────────────────────────────────────┘')
            
        opt = int(input("enter option: "))
        if opt == 1:
            date = input("update date: ")
            qry2 = "update patients set date = %s where patient_id = %s"
            cursor.execute(qry2,[date, ch])
            con.commit()
            print('┌─────────────────────────────────────────────────────────┐')
            print('│                   updated successfully                  │')                                        
            print('└─────────────────────────────────────────────────────────┘')
            ch = int(input("press 1 to exit: "))
            if ch == 1:
                print('┌─────────────────────────────────────────────────────────┐')
                print('│                 returning back to menu                  │')                                        
                print('└─────────────────────────────────────────────────────────┘')
                patient_menu()
            else:
                invalid_input()
        if opt == 2:
            name = input("update name: ")
            qry2 = "update patients set name = %s where patient_id = %s"
            cursor.execute(qry2, [name, ch])
            con.commit()
            print('┌─────────────────────────────────────────────────────────┐')
            print('│                  updated successfully                   │')                                        
            print('└─────────────────────────────────────────────────────────┘')
            ch = int(input("press 1 to exit: "))
            if ch == 1:
                print('┌─────────────────────────────────────────────────────────┐')
                print('│                   returning back to menu                │')                                        
                print('└─────────────────────────────────────────────────────────┘')
                patient_menu()
            else:
                invalid_input()
        if opt == 3:
            fee = int(input("update fee: "))
            qry2 = "update patients set fee = %s where patient_id = %s"
            cursor.execute(qry2, [fee, ch])
            con.commit()
            print('┌─────────────────────────────────────────────────────────┐')
            print('│                     updated successfully                │')                                        
            print('└─────────────────────────────────────────────────────────┘')
            ch = int(input("press 1 to exit: "))
            if ch == 1:
                print('┌─────────────────────────────────────────────────────────┐')
                print('│                   returning back to menu                │')                                        
                print('└─────────────────────────────────────────────────────────┘')
                patient_menu()
            else:
                invalid_input()



#REMOVE AN EXISTING PATIENT
def del_patient():
    print('┌─────────────────────────────────────────────────────────┐')
    print('│                      remove patient                     │')                                        
    print('└─────────────────────────────────────────────────────────┘')
    ptid = input("enter patient id: ")
    qry = "delete from patients where patient_id = %s"
    cursor.execute(qry,[ptid])
    con.commit()
    print('┌─────────────────────────────────────────────────────────┐')
    print('│                      patient removed                    │')                                        
    print('└─────────────────────────────────────────────────────────┘')
    ch = int(input("press 1 to exit: "))
    if ch == 1:
        print('┌─────────────────────────────────────────────────────────┐')
        print('│                   returning back to menu                │')                                        
        print('└─────────────────────────────────────────────────────────┘')
        patient_menu()
    else:
        invalid_input()



#LOGIN AND SIGN UP MENU
def login():
    print("┌─────────────────────────────────────────────────────────┐")
    print("│             1. sign up                                  │")
    print("│             2. sign in                                  │")
    print('└─────────────────────────────────────────────────────────┘')
    ch = int(input('choose option: '))
    if ch == 1:
        username = input("username: ")
        password = input("password: ")
        cursor.execute("insert into signup values(username,password)")
        con.commit()
        print("┌─────────────────────────────────────────────────────────┐")
        print("│                  sign up successful                     │")
        print('└─────────────────────────────────────────────────────────┘')
    if ch == 2:
        print("┌─────────────────────────────────────────────────────────┐")
        print("│                          login                          │")
        print('└─────────────────────────────────────────────────────────┘')
        for i in range(3):
            u = input("enter system username: ")
            if u == "ph298":
                print("please enter your password")
            else:
                print("incorrect username")
            p = input("enter system password: ")
            if p == "03904":
                print("┌─────────────────────────────────────────────────────────┐")
                print("│                    login successful                     │")
                print('└─────────────────────────────────────────────────────────┘')
                home_page()
            else:
                print("incorrect password")
                signin()

          
          
#LOGOUT
def logout():
    ch = input("please confirm that you want to logout: (y/n) ")
    if ch == "y" or ch == 'Y':
        print('╔═════════════════════════════════════════════════════════╗')
        print('║                                                         ║')
        print('║       Thank you for visiting Medstar Dental Clinic!     ║')
        print('║                                                         ║')
        print('╚═════════════════════════════════════════════════════════╝')
        sys.exit()
    elif ch == 'n' or ch == 'N':
        home_page()
    else:
        invalid_input()
      
      
      
#INVALID INPUT
def invalid_input():
    print('┌─────────────────────────────────────────────────────────┐')
    print('│             error occurred, invalid input               │')                                        
    print('└─────────────────────────────────────────────────────────┘')
    ch = int(input("press 1 to return: "))
    if ch == 1:
        home_page()
  
  
  
#ABOUT US
def about_us():
    f1=open('about_us.txt',"r")
    l=f1.readlines()
    while l :
        print(l)
        break
    f1.close()
    print()
    home_page()


login()
home_page()

