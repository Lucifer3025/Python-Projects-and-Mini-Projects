import pymysql as sql
import sys

con = sql.connect(host="localhost", user="root", password="SqlLUCIFER1#", database="python", charset="utf8")

def delete():
    try:
        eid = int(input("Enter the employee id="))
        qry = f"delete from empinfo where id={eid}"
        cur = con.cursor()
        cur.execute(qry)
        con.commit()
        if cur.rowcount == 1:
            print("Record deleted successfully!!")
        else:
            print("Record was not deleted!!")
    except ValueError:
        print("Invalid input. Please enter a valid integer for employee id.")
    except Exception as e:
        print(f"Error occurred: {str(e)}")

def create():
    try:
        id = int(input("Enter the employee id="))
        name = input("Enter your name=")
        gender = input("Enter your gender=")
        email = input("Enter your email=")
        passo = input("Enter your Password=")
        date = input("Enter your Date=")
        dept = input("Enter your dept=")
        cur = con.cursor()
        qry = "insert into empinfo values(%d,'%s','%s','%s','%s','%s','%s')" % (id, name, gender, email, passo, date, dept)
        cur.execute(qry)
        con.commit()
        if cur.rowcount == 1:
            print("Record inserted successfully")
        else:
            print("Error in inserting the record")
    except ValueError:
        print("Invalid input. Please enter valid data for employee id.")
    except Exception as e:
        print(f"Error occurred: {str(e)}")
    finally:
        con.commit()

def displayall():
    try:
        qry = "select * from empinfo"
        cur = con.cursor()
        cur.execute(qry)
        if cur.rowcount != 0:
            for i in cur.fetchall():
                print(f"|{i[0]}\t|{i[1]}\t|{i[2]}|{i[3]}\t|{i[4]}\t|{i[5]}\t|")
        else:
            print("No record")
    except Exception as e:
        print(f"Error occurred: {str(e)}")

def update():
    try:
        id = input("Enter your id=")
        cur = con.cursor()
        cur.execute(f"select * from empinfo where eid={id}")
        if cur.rowcount == 1:
            print("->Press 1 to update name.")
            print("->Press 2 to update gender.")
            print("->Press 3 to update email id.")
            print("->Press 4 to update password.")
            print("->Press 5 to update joining date.")
            print("->Press 6 to update department name.")
            print("->Press 7 to go back to previous menu.")
            ch = int(input("Enter your choice="))
            if ch == 1:
                n = input("Enter your name=")
                qry = f"update empinfo set name='{n}' where eid={id}"
            elif ch == 2:
                g = input("Enter gender=")
                qry = f"update empinfo set gender='{g}' where eid={id}"
            elif ch == 3:
                e = input("Enter email id=")
                qry = f"update empinfo set email='{e}' where eid={id}"
            elif ch == 4:
                p = input("Enter password=")
                qry = f"update empinfo set password='{p}' where eid={id}"
            elif ch == 5:
                d = input("Enter joining date=")
                qry = f"update empinfo set jdate='{d}' where eid={id}"
            elif ch == 6:
                dp = input("Enter department=")
                qry = f"update empinfo set passo='{dp}' where eid={id}"
            else:
                return
            if ch < 7:
                cur.execute(qry)
                con.commit()
                if cur.rowcount == 1:
                    print("Record updated!!")
                else:
                    print("Failed to update!")
        else:
            print("Invalid employee id!!")
    except ValueError:
        print("Invalid input. Please enter a valid integer for employee id or choice.")
    except Exception as e:
        print(f"Error occurred: {str(e)}")

while True:
    try:
        print("What operation would you like to perform?")
        print("1. Create your employee data.")
        print("2. Delete your employee data.")
        print("3. Display your employee data.")
        print("4. Update employee data.")
        print("5. Exit.")
        a = int(input("Enter your choice from 1 to 5: "))
        
        if a == 1:
            create()
        elif a == 2:
            delete()
        elif a == 3:
            displayall()
        elif a == 4:
            update()
        elif a == 5:
            con.close()
            sys.exit()
        else:
            print("Invalid input. Please enter a number from 1 to 5.")
    except ValueError:
        print("Invalid input. Please enter a valid integer for your choice.")
    except Exception as e:
        print(f"Error occurred: {str(e)}")
