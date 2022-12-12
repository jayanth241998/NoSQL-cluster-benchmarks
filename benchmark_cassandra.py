from cassandra.cluster import Cluster
import random
import string
import time
import sys

#connecting to the cluster with the given IP address
cluster = Cluster(['10.155.254.238'])

#connecting to the keyspace of cassandra
session = cluster.connect('benchmark')
session.default_timeout = 200

#list to store values of generated keys
keylist = []

#setting the starting time for elapsed time and cpu execution time
wall_start = time.time()
cpu_start = time.process_time()


#inserting 1000 records
for x in range(1000):
    key = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for i in range(10))
    keylist.append(key)
    value = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for i in range(90))
    session.execute("Insert into benchmark_table(key,value) values (%s,%s)",[key,value])
    
#performing lookup of 1000 records
for key in keylist:
    result = session.execute("select * from benchmark_table where key=%s",[key])
    
#deleting 1000 records
for key in keylist:
    session.execute("delete from benchmark_table where key=%s",[key])

#setting end time
wall_end = time.time()
cpu_end = time.process_time()

#calculating program execution time and cpu execution time
execution_time = wall_end - wall_start
cpu_time = cpu_end - cpu_start

#calculating throughput of 3000 total operations performed
throughput = 3000/(execution_time*1000000)

print('execution time :', execution_time/1000, 's')
print('cpu execution time :', cpu_time/1000, 's')
print('throughput :',throughput,'MOPS')

