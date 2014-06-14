# -*- coding: utf-8 -*-

''' Script to migrate a table from a MySQL database to a PostgreSQL database with the same format and the same fields.
    Itś neccesary to change the name of TABLE and write a JSON file (nogit_mytopost.json) which contents the variable data
    as user1 and user2, passwd1 and passwd2, host1 and host2, and dbname1 and dbname2 as 1 the origin and 2 the destination data '''
    
import json
import MySQLdb
import psycopg2
from os import path
# Import data from json file to connect with databases origin (MySQL) and destination (PostgreSQL)
path_file = path.join("../","nogit_mytopost.json")
json_data = open(path_file)
data = json.load(json_data)
json_data.close()
# Import data from MySQL database
db=MySQLdb.connect(host=(data["host1"]),user=(data["user1"]),passwd=(data["passwd1"]),db=(data["dbname1"]))
cursor=db.cursor()
sql='SELECT * FROM ¿TABLE?'
cursor.execute(sql)
resultado=cursor.fetchall()
db.close()
# Export data to PostgreSQL
conector=psycopg2.connect(dbname=data["dbname2"], host=data["host2"], port=5432, user=data["user2"], password=data["passwd2"])
print "connected...!"
cursor=conector.cursor()
query = "INSERT INTO ¿TABLE? (id_areas_salud_id, id_usuario_id) VALUES (%s, %s)"
for r in resultado:
	area = int(r[1])
	usuario = int(r[2])
	print r[0] , '|' , field1, '|',  field2
	cursor.execute(query, (field1, field2,))
conector.commit()
conector.close()
print "Bye"
