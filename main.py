import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE mydatabase")
print("Welcome to ViTraveller!")
i = 0
while i == 0:
    print('press 1 to sign up')
    print('press 2 to sign in')
    print('press 9 to exit')
    ch = int(input('Enter:'))
    if ch == 9:#termination of while loop 
        i = 1
    elif ch == 2:
        user = input("Enter your registration number(username):")
        password = input("Enter your password:")
        ###############CHECKING FOR THE USER
        st = 'SELECT regno, password from USERS'
        mycursor.execute(st)
        records = mycursor.fetchone()
        mydb.commit()
        if records[0] == user:
            #the user exists
            if records[2] == password:
                #the password entered is correct
                print('Welcome',user,'!')
                user_name = records[1]
                j = 0
                while j == 0:
                    print('Press 1 to view your existing groups')
                    print('Press 2 to find a group')
                    print('Press 9 to exit')
                    choice = int(input('Enter:'))
                    if choice == 9:
                        j = 1
                    elif choice == 1:
                        st1 = 'SELECT from_date, destination, transport, detail WHERE regnumber = {} FROM travel'.format(user)
                        mycursor.execute(st1)
                        mydb.commit()
                        groups = mycursor.fetchall()
                        for rec in groups:
                            print(rec)
                    elif choice == 2:
                        print('Please fill the following questions:')
                        fdate = input('Enter the date of departure in YYYY-MM-DD format:')
                        dest = input('Enter the destination:')
                        trans = input('Enter the mode of transport(PL for airplane, TR for train, CA for car):')
                        name = input('Enter the name of airlines/train/...:')
                        st2 = 'INSERT INTO travel VALUES ({}, {}, {},{},{},{})'.format(user,user_name,fdate, dest, trans, name)
                        mycursor.execute(st2)
                        mydb.commit()
                        print('Thank you for your patience!...')
                        print('Successful')
                        print("The following have the same transport and same name of the airline/train...")
                        rd = 'select regnumber, User_name, destination, transport, details WHERE(from_date = {} AND transport = {} AND details = {}) FROM travel'.format(fdate,trans, name)
                        mycursor.execute(rd)
                        mydb.commit()
                        print("The following have the same destination as well")
                        rd2 = 'select regnumber, User_name, destination, transport, details WHERE(from_date = {} AND transport = {} AND details = {} AND destination = {}) FROM travel'.format(fdate,trans, name, dest)
                        mycursor.execute(rd2)
                        mydb.commit()
                        
                    else:
                        print("Enter a valid choice!")
                
            else:
                print('Invalid password')
                print('Try again')
        else:
            print("The username doesn't exist")
    elif ch == 1:####################FOR SIGN UP
        temp = 0
        while temp == 0:
            reg_num = input("Enter your registration number(will be your username):")
            strp = 'SELECT regnu from USERS'
            mycursor.execute(strp)
            user_rec = mycursor.fetchall()
            if len(user_rec) > 0:
                print("The username already exists")
                temp = 1
            else:
                mydb.commit()
                Name = input("Enter your name:")
                passw = input("Enter your password:")
                cpassw = input("Re-enter your password:")
                if passw == cpassw:
                    strf = "INSERT INTO USERS VALUES ({},{},{})".format(reg_num, Name, passw)
                    print("Successful!")
                    mycursor.execute(strf)
                    mydb.commit()
                else:
                    print("Passwords do not match")
                
    else:
        print('Enter a valid choice!')
            
        
