


#the following python libraries has to be installed to run the scripts
redis==4.3.5
numpy==1.23.5
pymongo==3.12.0
cassandra-driver==3.25.0

#to install all
sudo pip install -r requirements.txt



#important: 
**the server IP address has to be set in the script**

##To run the python Cassandra script 

python benchmark_cassandra.py

##To run the python Redis script

python benchmark_redis.py

##To run the python MongoDB script

python benchmark_mongoDB.py


**The script was run in parallel across multiple nodes in cluster using pssh tool**

## the following command was used to run the scripts in pssh

parallel-ssh -i -h ~/.hosts-file python benchmark_script.py

##create the file ~/.hosts-file and enter the ip addresses of the nodes in which the command has to be run
