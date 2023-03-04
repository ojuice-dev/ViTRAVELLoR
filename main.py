import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  port=3006,
  user="root",
  password="root")

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE if not exists mydatabase")
mycursor.execute("USE mydatabase")
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
        st = 'SELECT * from USERS'
        mycursor.execute(st)
        allrec = mycursor.fetchall()
        c=0
        for i in allrec:
            if i[0] == user:
                c=1
            if i[2] ==  password:
                c=c+1
                records = i

        if c==0:
            print("The username doesn't exist")
        if c==1:
            print('Invalid password')
            print('Try again')
        if c==2:
            #the user exists
            if records[2] == password:
                #the password entered is correct
                print('Welcome',records[1],'!')
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
                        st1 = 'SELECT from_date, destination, transport, details FROM travel WHERE regnumber = "{}"'.format(user)
                        groups = mycursor.fetchall()
                        for rec in groups:
                            print(rec)
                        else:
                            print("No groups found")
                    elif choice == 2:
                        print('Please fill the following questions:')
                        fdate = input('Enter the date of departure in YYYY-MM-DD format:')
                        start = input('Enter the place of departure:')
                        dest = input('Enter the destination:')
                        trans = input('Enter the mode of transport(PL for airplane, TR for train, CA for car):')
                        name = input('Enter the name of airlines/train/...:')
                        st2 = "INSERT INTO travel VALUES ('{}', '{}', '{}', '{}', '{}', '{}','{}')".format(user,user_name,start,fdate, dest, trans, name)
                        mycursor.execute(st2)
                        mydb.commit()
                        

                        print('Thank you for your patience!...')
                        print('Successful')
                        print("The following users share the same transport and name of the airline/train...")
                        rd = "select User_name, destination, transport, details FROM travel WHERE(from_date = '{}' AND start = '{}' AND transport = '{}' AND details = '{}')".format(fdate, start, trans, name)
                        mycursor.execute(rd)
                        group1 = mycursor.fetchall()
                        for rec in group1:
                            print(rec)
                        print("The following users share the same destination as well...")
                        rd2 = "select User_name, destination, transport, details FROM travel WHERE(from_date = '{}' AND start = '{}' AND transport = '{}' AND details = '{}' AND destination = '{}')".format(fdate,start,trans, name, dest)
                        mycursor.execute(rd2)
                        group2 = mycursor.fetchall()
                        print(group2)
                        for rec in group2:
                            print(rec)
                    else:
                        print("Enter a valid choice!")
                
            
    elif ch == 1:####################FOR SIGN UP
        temp = 0
        while temp == 0:
            reg_num = input("Enter your registration number(will be your username):")
            strp = 'SELECT regnu from USERS where regnu="{}"'.format(reg_num)
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
                    strf = 'INSERT INTO USERS VALUES("{}","{}","{}")'.format(reg_num, Name, passw)
                    print("Successful!")
                    mycursor.execute(strf)
                    mydb.commit()
                    temp=1
                else:
                    print("Passwords do not match")
                
    else:
        print('Enter a valid choice!')
            
        
