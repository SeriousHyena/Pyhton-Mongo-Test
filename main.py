# initial date: 3/16/2020
# Python code to illustrate 
# inserting data in MongoDB 
# i don't get credit for this. I got this from: 
# https://www.geeksforgeeks.org/mongodb-python-insert-update-data/
# and it works great!
# make sure the mongo db server is running
# use mongo compass to view the database

import pymongo
from pymongo import MongoClient 

try: 
    conn = MongoClient() 
    print("Connected successfully!!!") 
except:   
    print("Could not connect to MongoDB") 

# database 
db = conn.EM_mongo 
  
# Created or Switched to collection names: my_gfg_collection 
# this is a standard python dictionary that i can populate in any number
# of ways in python
collection = db.test_data 
  
emp_rec1 = { 
        "name":"Mrs. Peanut", 
        "eid":24, 
        "location":"Elmo"
        } 
emp_rec2 = { 
        "name":"Mrs. Bailey", 
        "eid":14, 
        "location":"Elmo"
        } 
  
# Insert Data 
rec_id1 = collection.insert_one(emp_rec1) 
rec_id2 = collection.insert_one(emp_rec2) 
  
print("Data inserted with record ids",rec_id1," ",rec_id2) 
  
# Printing the data inserted 
cursor = collection.find() 
for record in cursor: 
    print(record) 
    