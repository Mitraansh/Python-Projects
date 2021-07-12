import mysql.connector
Mydb=mysql.connector.connect(host="localhost",user="root",passwd="root")
mycursor=Mydb.cursor()
def database():
     mycursor.execute("CREATE DATABASE IF NOT EXISTS RESTAURANT")


