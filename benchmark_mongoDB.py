from pymongo import MongoClient
import numpy as np
import os
import time

URI1 = "mongodb://10.155.254.37:27017"
size = int(1000)
client = MongoClient(URI1);
print(client)
mydb = client["mydatabase"]
mycol = mydb["test"]

mylist = []
keylist = []
valuelist = []

for i in range(size):
    key = np.random.bytes(10)
    value = np.random.bytes(90)
    keylist.append(str(key))
    valuelist.append(str(value))
    mylist.append({str(key):str(value)})


st = time.time()
x = mycol.insert_many(mylist)
et = time.time()

t21 = et-st
print("Insertion:",t21)

t3=time.time()
for i in range(size):
    result = mycol.find({keylist[i]:valuelist[i]})


t4=time.time()
t34 = t4-t3
print("Searching:",t34)
t5 = time.time()
for j in range(size):
    dd = mycol.delete_many({keylist[j]:valuelist[j]})

mycol.delete_many({})
t6=time.time()
t56 = t6 - t5
print("Deletion:",t56)
execution_time = t56+t34+t21
throughput = 3000/(execution_time*1000000);
print('throughput :',throughput,'MOPS')
print('execution time :', execution_time/1000, 's')

client.close();
