import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="rootpass",
  database="testdatabase"
)

mycursor = db.cursor()

# create database below
# mycursor.execute("CREATE DATABASE testdatabase")

