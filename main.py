# Brett you might find this useful
# initial date: 3/16/2020
# Python code to illustrate 
# inserting data in MongoDB 
# i don't get credit for this. I got this from: 
# https://www.geeksforgeeks.org/mongodb-python-insert-update-data/
# local repo location: C:\Users\emack\python-mongo
# and it works great!
# make sure the mongo db server is running
# use mongo compass to view the database

# i can either write a function or class to call the database writing code or 
# just leave it inline. i would write the python code that generates the data (i.e.)
# from a websraping junket or some other data


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
        "location":"Elmo",
        'Comments':'Peanut is a great dog and I love her very much'
        } 
emp_rec2 = { 
        "name":"Mrs. Bailey", 
        "eid":14, 
        "location":"Elmo",
        'Comments':'Bailey is a great dog and I miss her very much'
        } 
dog_1 = {
        'name':'Oliver',
        'dog_id':3,
        'location':'doghouse_1',
        'Comments':'Oliver is a crazy dog and I think he needs therapy'
        }

dog_2 = {
        'name':'Tigger',
        'dog_id':4,
        'location':'doghouse_2',
        'Comments':'Tigger is a big teddy bear'
        }
  
# Insert Data 
rec_id1 = collection.insert_one(emp_rec1) 
rec_id2 = collection.insert_one(emp_rec2) 
rec_id3 = collection.insert_one(dog_1)
rec_id4 = collection.insert_one(dog_2)

print("Data inserted with record ids",rec_id1," ",rec_id2, ' ', rec_id3, ' ', rec_id4) 
  
# Printing the data inserted 
cursor = collection.find() 
for record in cursor: 
    print(record) 
    