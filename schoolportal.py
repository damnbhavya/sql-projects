import mysql.connector as sql
import sys
mycon = sql.connect(host="localhost", user = "root",
passwd = "0104", database = "schoolportal")
cur = mycon.cursor()

def login():
   global admin
   print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
   admin = input("ENTER YOUR ADMISSION NUMBER : ")
   passd = input("ENTER YOUR ACCOUNT PASSWORD : ")
   print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
   query = "SELECT * FROM LOGIN_DETAILS"
   cur = mycon.cursor()
   cur.execute(query)
   data = cur.fetchall()

   for row in data:
      if(admin in row) and (passd in row):
         print("LOGIN SUCCESSFULL")
         menu()
   print("WRONG ADMISSION NO OR PASSWORD")
   mainmenu()

def signup():
   global admin
   print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
   admin = input("ENTER NEW ADMISSION NUMBER : ")
   passd = input("ENTER A STRONG PASSWORD : ")
   print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")

   try:
      query = """INSERT INTO LOGIN_DETAILS VALUES
      ('{}','{}')""".format(admin,passd)
      cur = mycon.cursor()
      cur.execute(query)
      mycon.commit()
      print("SIGNED UP SUCCESSFULLY")
      menu()
   except sql.IntegrityError:
      print("ID EXISTS ALREADY")
      menu()
   except Exception:
      print("OUT OF RANGE INPUT")
      signup()

def password():
   global admin
   print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
   admin = input("ENTER THE ADMISSION NUMBER : ")
   passd = input("ENTER NEW PASSWORD : ")
   print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")

   try:
      query = """UPDATE LOGIN_DETAILS SET PASSWORD =
      '{}' WHERE ADMIN_NO = '{}'""".format(passd, admin)
      cur = mycon.cursor()
      cur.execute(query)
      mycon.commit()
      print("PASSWORD FOR ", admin, " IS UPDATED")
      mainmenu()
   except Exception:
      print("PASSWORD IS OUT OF RANGE. (RANGE = 1-20)")
      password()

def ad_login():
   print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
   user_id = input("ENTER YOUR USER ID : ")
   user_pass = input("ENTER YOUR PASSWORD : ")
   print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
   query = "SELECT * FROM ADMINISTRATOR"
   cur = mycon.cursor()
   cur.execute(query)
   data = cur.fetchall()

   for row in data:
      if(user_id in row) and (user_pass in row):
         print("ADMINISTRATOR LOGIN SUCCESSFULL")
         ad_menu()
   print("WRONG USER ID OR PASSWORD")
   mainmenu()

def ad_signup():
   print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
   user_id = input("ENTER NEW ADMISSION NUMBER : ")
   user_pass = input("ENTER A STRONG PASSWORD : ")
   print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
   try:
      query = """INSERT INTO ADMINISTRATOR VALUES
      ('{}','{}')""".format(user_id,user_pass)
      cur = mycon.cursor()
      cur.execute(query)
      mycon.commit()
      print("SIGNED UP AS ADMINISTRATOR")
      ad_menu()
   except sql.IntegrityError:
      print("ADMINISTRATOR ID EXISTS ALREADY")
      ad_menu()
   except Exception:
      print("OUT OF RANGE INPUT")
      ad_signup()

def ad_password():
   print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
   user_id = input("ENTER THE ADMISSION NUMBER : ")
   user_pass = input("ENTER NEW PASSWORD : ")
   print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
   try:
      query = """UPDATE ADMINISTRATOR SET PASSWORD = '{}'
      WHERE USER_ID = '{}'""".format(user_pass, user_id)
      cur = mycon.cursor()
      cur.execute(query)
      mycon.commit()
      print("PASSWORD FOR ", user_id, " IS UPDATED")
      mainmenu()
   except Exception:
      print("PASSWORD IS OUT OF RANGE. (RANGE = 1-20)")
      ad_password()

def ad_menu():
   print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
   print("ADMINISTRATOR OPTIONS LOADING ■ ■ ■")
   print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
   print("1. VIEW STUDENT LIST")
   print("2. ADD NEW STUDENT CLUB")
   print("3. DELETE A STUDENT CLUB")
   print("4. CHANGE CLUB INCHARGE")
   print("5. BACK TO MAIN MENU")
   print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
   ch2 = input("ENTER THE ACTION : ")
   if ch2 == '1':
      slist()
   elif ch2 == '2':
      clubadd()
   elif ch2 == '3':
      clubdelete()
   elif ch2 == '4':
      incharge()
   elif ch2 == '5':
      mainmenu()
   else:
      print("INVALID ACTION")

def slist():
   query = "SELECT * FROM STUDENT_DETAILS"
   cur = mycon.cursor()
   cur.execute(query)
   data = cur.fetchall()
   print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
   print('%5s'%"ADMIN NO",'%10s'%"NAME",'%12s'%"CLASS",'%12s'%"ADDRESS",
   '%15s'%"PHONE NO",'%14s'%"GENDER",'%15s'%"STUDENT CLUB")
   print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
   for i in data:
      print('%5s'%i[0],'%15s'%i[1],'%8s'%i[2],'%14s'%i[3],
      '%16s'%i[4],'%12s'%i[5],'%15s'%i[6])
   print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
   ad_menu()

def clubadd():
   query = "SELECT * FROM CLUB_DETAILS"
   cur = mycon.cursor()
   cur.execute(query)
   data = cur.fetchall()
   print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
   print('%5s'%"CLUB NAME",'%20s'%"INCHARGE")
   print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
   for i in data:
      print('%5s'%i[0],'%20s'%i[1])
   print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
   club = input("ENTER NEW CLUB NAME : ")
   incharg = input("ENTER CLUB INCHARGE : ")
   print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
   try:
      query = """INSERT INTO CLUB_DETAILS VALUES
      ('{}', '{}')""".format(club, incharg)
      cur = mycon.cursor()
      cur.execute(query)
      mycon.commit()
      print("SUCCESSFULLY ADDED NEW CLUB")
      ad_menu()
   except Exception:
      print("OUT OF RANGE INPUT")
      clubadd()

def clubdelete():
   query = "SELECT * FROM CLUB_DETAILS"
   cur = mycon.cursor()
   cur.execute(query)
   data = cur.fetchall()
   print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
   print('%5s'%"CLUB NAME",'%20s'%"INCHARGE")
   print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
   for i in data:
      print('%5s'%i[0],'%20s'%i[1])
   print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
   club = input("ENTER THE CLUB THAT IS TO BE DELETED : ")
   query = "SELECT CLUB_NAME FROM CLUB_DETAILS"
   cur = mycon.cursor()
   cur.execute(query)
   data = cur.fetchall()
   for row in data:
      if (club in row):
         try:
            query = """DELETE FROM CLUB_DETAILS WHERE
            CLUB_NAME = '{}'""".format(club)
            cur = mycon.cursor()
            cur.execute(query)
            mycon.commit()
            print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
            print("STUDENT CLUB DELETED")
            ad_menu()
         except Exception:
            print("ENTER A VALID CLUB NAME")
            clubdelete()
   print("STUDENT CLUB NOT FOUND")
   ad_menu()

def incharge():
   query = "SELECT * FROM CLUB_DETAILS"
   cur = mycon.cursor()
   cur.execute(query)
   data = cur.fetchall()
   print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
   print('%5s'%"CLUB NAME",'%20s'%"INCHARGE")
   print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
   for i in data:
      print('%5s'%i[0],'%20s'%i[1])
   print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
   club = input("ENTER THE CLUB NAME : ")
   incharg = input("ENTER NEW INCHARGE NAME : ")
   try:
      query = """UPDATE CLUB_DETAILS SET CLUB_INCHARGE =
      '{}' WHERE CLUB_NAME = '{}'""".format(incharg, club)
      cur = mycon.cursor()
      cur.execute(query)
      mycon.commit()
      print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
      print("NEW INCHARGE FOR ", club, " IS ", incharg)
      ad_menu()
   except Exception:
      print("OUT OF RANGE INPUT, PLEASE RE-ENTER")
      incharge()

def menu():
   print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
   print("OPTIONS LOADING ■ ■ ■")
   print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
   print("1. VIEW STUDENT DETAILS")
   print("2. ADD STUDENT DETAILS")
   print("3. UPDATE STUDENT DETAILS")
   print("4. DELETE STUDENT DETAILS")
   print("5. VIEW STUDENT CLUBS")
   print("6. JOIN STUDENT CLUB")
   print("7. BACK TO MAIN MENU")
   print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
   ch2 = input("ENTER THE ACTION : ")
   if ch2 == '1':
      view()
   if ch2 == '2':
      add()
   elif ch2 == '3':
      update()
   elif ch2 == '4':
      delete()
   elif ch2 == '5':
      clubs()
   elif ch2 == '6':
      join()
   elif ch2 == '7':
      mainmenu()
   else:
      print("INVALID ACTION")
      menu()

def view():
   global admin
   query = """SELECT * FROM STUDENT_DETAILS WHERE
   ADMIN_NO = '{}'""".format(admin)
   cur = mycon.cursor()
   cur.execute(query)
   data = cur.fetchall()
   print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
   print('%5s'%"ADMIN NO",'%10s'%"NAME",'%12s'%"CLASS",'%12s'%"ADDRESS",
   '%15s'%"PHONE NO",'%14s'%"GENDER",'%15s'%"STUDENT CLUB")
   print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
   for i in data:
      print('%5s'%i[0],'%15s'%i[1],'%8s'%i[2],'%14s'%i[3],
      '%16s'%i[4],'%12s'%i[5],'%15s'%i[6])
   print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
   menu()

def add():
   global admin
   print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
   query = """SELECT * FROM STUDENT_DETAILS WHERE
   ADMIN_NO = '{}'""".format(admin)
   cur = mycon.cursor()
   cur.execute(query)
   data = cur.fetchall()
   if not data:
      name = input("ENTER STUDENT NAME : ")
      clas = int(input("ENTER YOUR CLASS : "))
      address = input("ENTER YOUR ADDRESS : ")
      phone = int(input("ENTER YOUR PHONE NUMBER : "))
      gender = input("ENTER YOUR GENDER (M/F) : ")
      try:
         query = """INSERT INTO STUDENT_DETAILS VALUES('{}','{}',{},'{}'
         ,{},'{}',NULL)""".format(admin,name,clas,address,phone,gender)
         cur = mycon.cursor()
         cur.execute(query)
         mycon.commit()
         print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
         print("STUDENT DETAILS ADDED")
         menu()
      except Exception:
         print("INVALID INPUT, PLEASE RE-ENTER THE VALUES")
         add()
   else:
      print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
      print("STUDENT DETAILS ALREADY EXISTS")
      menu()

def update():
   global admin
   print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
   query = """SELECT * FROM STUDENT_DETAILS WHERE
   ADMIN_NO = '{}'""".format(admin)
   cur = mycon.cursor()
   cur.execute(query)
   data = cur.fetchall()
   if not data:
      print("CAN'T FIND STUDENT RECORDS TO UPDATE")
      menu()
   else:
      print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
      print("SELECT THE DETAILS THAT IS TO BE UPDATED ■ ■ ■")
      print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
      print("1. NAME")
      print("2. CLASS")
      print("3. ADDRESS")
      print("4. PHONE NO")
      print("5. GENDER")
      print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
      ch = int(input("ENTER ACTION : "))
      print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
      if ch == 1 :
         name = input("ENTER THE NEW NAME OF THE STUDENT : ")
         try:
            query = """UPDATE STUDENT_DETAILS SET NAME = '{}'
            WHERE ADMIN_NO = '{}'""".format(name, admin)
            cur = mycon.cursor()
            cur.execute(query)
            mycon.commit()
            print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
            print("NAME OF THE STUDENT IS UPDATED")
         except Exception:
            print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
            print("NAME IS OUT OF RANGE, PLEASE RE-ENTER")
            update()
      elif ch == 2:
         clas = input("ENTER THE NEW CLASS OF THE STUDENT : ")
         try:
            query = """UPDATE STUDENT_DETAILS SET CLASS = '{}'
            WHERE ADMIN_NO = '{}'""".format(clas, admin)
            cur = mycon.cursor()
            cur.execute(query)
            mycon.commit()
            print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
            print("CLASS OF THE STUDENT IS UPDATED")
         except Exception:
            print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
            print("CLASS IS INVALID, PLEASE RE-ENTER")
            update()
      elif ch == 3:
         address = input("ENTER THE NEW ADDRESS OF THE STUDENT : ")
         try:
            query = """UPDATE STUDENT_DETAILS SET ADDRESS =
            '{}' WHERE ADMIN_NO = '{}'""".format(address, admin)
            cur = mycon.cursor()
            cur.execute(query)
            mycon.commit()
            print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
            print("ADDRESS OF THE STUDENT IS UPDATED")
         except Exception:
            print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
            print("ADDRESS IS OUT OF RANGE, PLEASE RE-ENTER")
            update()
      elif ch == 4:
         phone = int(input("ENTER THE NEW PHONE NO OF THE STUDENT : "))
         try:
            query = """UPDATE STUDENT_DETAILS SET PHONE_NO = {}
            WHERE ADMIN_NO = '{}'""".format(phone, admin)
            cur = mycon.cursor()
            cur.execute(query)
            mycon.commit()
            print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
            print("PHONE NUMBER OF THE STUDENT IS UPDATED")
         except Exception:
            print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
            print("PHONE NUMBER IS INVALID, PLEASE RE-ENTER")
            update()
      elif ch == 5:
         gender = input("ENTER THE NEW GENDER FOR THE STUDENT (M/F) : ")
         try:
            query = """UPDATE STUDENT_DETAILS SET GENDER = '{}'
            WHERE ADMIN_NO = '{}'""".format(gender, admin)
            cur = mycon.cursor()
            cur.execute(query)
            mycon.commit()
            print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
            print("GENDER OF THE STUDENT IS UPDATED")
         except Exception:
            print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
            print("GENDER IS INVALID, PLEASE GIVE INPUT IN M/F")
            update()
      else:
         print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
         print("INVALID ACTION")
      menu()

def delete():
   global admin
   query = """DELETE FROM STUDENT_DETAILS WHERE
   ADMIN_NO = '{}'""".format(admin)
   cur = mycon.cursor()
   cur.execute(query)
   mycon.commit()
   print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
   print("RECORD DELETED")
   menu()

def clubs():
   query = "SELECT * FROM CLUB_DETAILS"
   cur = mycon.cursor()
   cur.execute(query)
   data = cur.fetchall()
   print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
   print('%5s'%"CLUB NAME",'%20s'%"INCHARGE")
   print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
   for i in data:
      print('%5s'%i[0],'%20s'%i[1])
   print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
   menu()

def join():
   global admin
   print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
   query = """SELECT * FROM STUDENT_DETAILS WHERE
   ADMIN_NO = '{}'""".format(admin)
   cur = mycon.cursor()
   cur.execute(query)
   data = cur.fetchall()
   if not data:
      print("CAN'T JOIN A CLUB, STUDENT RECORDS NOT FOUND")
      menu()
   else:
      query = "SELECT * FROM CLUB_DETAILS"
      cur = mycon.cursor()
      cur.execute(query)
      data = cur.fetchall()
      print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
      print('%5s'%"CLUB NAME",'%20s'%"INCHARGE")
      print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
      for i in data:
         print('%5s'%i[0],'%20s'%i[1])
      print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")

      student_club = input("ENTER THE CLUB NAME : ")
      try:
         for row in data:
            if(student_club in row):
               print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
               print("STUDENT CLUB FOUND")
               query = """UPDATE STUDENT_DETAILS SET STUDENT_CLUB =
               '{}' WHERE ADMIN_NO='{}'""".format(student_club, admin)
               cur = mycon.cursor()
               cur.execute(query)
               mycon.commit()
               print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
               print("SUCCESSFULLY ADDED CLUB TO THE STUDENT DETAILS")
               menu()
      except Exception:
         print("STUDENT CLUB NOT FOUND")
         mainmenu()

def pexit():
   print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
   print("EXITING THE PORTAL ■ ■ ■")
   print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
   sys.exit()

def mainmenu():
   print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
   print("MAIN MENU LOADING ■ ■ ■")
   print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
   print("1. ADMINISTRATOR LOGIN")
   print("2. ADMINISTRATOR SIGN UP")
   print("3. CHANGE ADMINISTRATOR PASSWORD")
   print("4. STUDENT LOGIN")
   print("5. STUDENT SIGN UP")
   print("6. CHANGE STUDENT PASSWORD")
   print("7. PRESS ANY KEY TO EXIT THE PORTAL")
   print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
   while True:
      ch = ''
      ch = input("ENTER THE ACTION : ")
      if ch == '1':
         ad_login()
      if ch == '2':
         ad_signup()
      if ch == '3':
         ad_password()
      if ch == '4':
         login()
      if ch == '5':
         signup()
      if ch == '6':
         password()
      else:
         pexit()
admin = ''
mainmenu()