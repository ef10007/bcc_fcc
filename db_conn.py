from sshtunnel import SSHTunnelForwarder
from pymongo import MongoClient
import os
from bson import ObjectId
import json
from pprint import pprint

from bson.json_util import dumps

hostname = os.getenv('hpc_host')
username = os.getenv('hpc_user')
pwd = os.getenv('hpc_pw')
database = "epp_potential"
collection_name = "BCC"

server = SSHTunnelForwarder(
    hostname,
    ssh_username=username,
    ssh_password=pwd,
    remote_bind_address=('127.0.0.1', 27017)
)

server.start()

client = MongoClient('127.0.0.1', server.local_bind_port) # server.local_bind_port is assigned local port

db = client[database]
cursor = db.BCC.find({ }).limit(10)

for document in cursor:
    milier_indices = 
    print(document['hkl'], document['eV/atom'])

server.stop()
