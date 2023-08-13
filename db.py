import mysql.connector
f = mysql.connector.connect(host = "localhost", user = "root", passwd = "")
mycur = f.cursor()
mycur.execute("create database healocode;")
f.commit()
mycur.execute("use healocode;")
print("database created")

que = "create table user_info(USERNAME varchar(20), PASSWORD varchar(20), PHONENO varchar(10) NOT NULL primary key, FLAT varchar(20), STATE varchar(30), CITY varchar(30));"
mycur.execute(que)
print("table user_info created")
f.commit()

que = "create table infected(PHONENO varchar(20), HEADACHE tinyint, COUGH tinyint, COLD tinyint, GENERAL_SICKNESS tinyint, FEVER tinyint, NAUSEOUS tinyint, FATIGUE tinyint);"
mycur.execute(que)
print("table infected created")
f.commit()

que = "create table food_info(ITEMNAME varchar(20), DESCRIPTION varchar(100), PHONENO varchar(10) NOT NULL primary key);"
mycur.execute(que)
print("table food_info created")
f.commit()

mycur.execute("insert into user_info(USERNAME, PASSWORD, PHONENO, FLAT, STATE, CITY)values('{}','{}','{}','{}','{}','{}')".format('a','a','a','a','a','a'))
mycur.execute("insert into user_info(USERNAME, PASSWORD, PHONENO, FLAT, STATE, CITY)values('{}','{}','{}','{}','{}','{}')".format('b','b','b','b','b','b'))
mycur.execute("insert into user_info(USERNAME, PASSWORD, PHONENO, FLAT, STATE, CITY)values('{}','{}','{}','{}','{}','{}')".format('c','c','c','c','c','c'))
mycur.execute("insert into user_info(USERNAME, PASSWORD, PHONENO, FLAT, STATE, CITY)values('{}','{}','{}','{}','{}','{}')".format('d','d','d','d','d','d'))
mycur.execute("insert into user_info(USERNAME, PASSWORD, PHONENO, FLAT, STATE, CITY)values('{}','{}','{}','{}','{}','{}')".format('e','e','e','e','e','e'))
f.commit()

mycur.execute("insert into infected(PHONENO, HEADACHE, COUGH, COLD, GENERAL_SICKNESS, FEVER, NAUSEOUS, FATIGUE)values('{}',{},{},{},{},{},{},{})".format('a',0,1,1,0,0,0,0))
mycur.execute("insert into infected(PHONENO, HEADACHE, COUGH, COLD, GENERAL_SICKNESS, FEVER, NAUSEOUS, FATIGUE)values('{}',{},{},{},{},{},{},{})".format('b',1,1,0,0,0,0,0))
mycur.execute("insert into infected(PHONENO, HEADACHE, COUGH, COLD, GENERAL_SICKNESS, FEVER, NAUSEOUS, FATIGUE)values('{}',{},{},{},{},{},{},{})".format('c',0,1,1,0,0,1,1))
mycur.execute("insert into infected(PHONENO, HEADACHE, COUGH, COLD, GENERAL_SICKNESS, FEVER, NAUSEOUS, FATIGUE)values('{}',{},{},{},{},{},{},{})".format('d',1,1,1,1,1,1,1))
mycur.execute("insert into infected(PHONENO, HEADACHE, COUGH, COLD, GENERAL_SICKNESS, FEVER, NAUSEOUS, FATIGUE)values('{}',{},{},{},{},{},{},{})".format('e',0,0,1,0,0,0,0))
f.commit()

mycur.execute("insert into food_info(ITEMNAME, DESCRIPTION, PHONENO)values('{}','{}','{}')".format('food','AAAAAAAA', 'a'))
mycur.execute("insert into food_info(ITEMNAME, DESCRIPTION, PHONENO)values('{}','{}','{}')".format('food','CCCCC', 'c'))
mycur.execute("insert into food_info(ITEMNAME, DESCRIPTION, PHONENO)values('{}','{}','{}')".format('food','EEEEEEEEEEE', 'e'))
f.commit()