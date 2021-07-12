import mysql.connector
Mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="RESTAURANT")
mycursor=Mydb.cursor()

mycursor.execute("CREATE TABLE  IF NOT EXISTS INCOME(ORDER_ID int(5) ,\
ORDER_TYPE  VARCHAR(3) ,ORDER_DATE DATETIME,ITEM_NAME VARCHAR(30),QTY int(5),\
TOTAL  int(6))")

mycursor.execute("CREATE TABLE  IF NOT EXISTS MANAGER(EMP_ID integer PRIMARY KEY,\
EMP_NAME VARCHAR(30),DESIGNATION VARCHAR(30),PHONE_NO BIGINT,\
SALARY BIGINT)")

