from sshtunnel import SSHTunnelForwarder
from pymongo import MongoClient
import os
from bson import ObjectId
import json
from pprint import pprint

from ase.build import surface
from ase.visualize import view


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

def get_data(limit=1):
    server.start()

    client = MongoClient('127.0.0.1', server.local_bind_port) # server.local_bind_port is assigned local port
    db = client[database]
    cursor = db.FCC.find({ }).limit(limit)

    for document in cursor:
        atom = document['atom']
        miller_indices = document['hkl'].split('_')
        miller_indices = tuple(int(m) for m in miller_indices)
        potential_energy = document['eV/atom']
        yield atom, miller_indices, potential_energy

    # server.stop()


# data = get_data(10)

# print([d for d in data])