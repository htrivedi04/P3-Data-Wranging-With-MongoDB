import signal
import os
import subprocess
from pymongo import MongoClient

# The os.setsid() is passed in the argument preexec_fn so
# it's run after the fork() and before exec() to run the shell.
pro = subprocess.Popen("mongod", preexec_fn = os.setsid)

db_name = "osmDelhi"

client = MongoClient('localhost:27017')
db = client[db_name]

# Build Mongo Import command
collection = filename[:filename.find(".")]
working_directory = "/Users/Trivedi/Desktop/Data Analytics/P3"
json_file = "map.json"

mongoimport_cmd = "mongoimport --db " + db_name + \
                  "--collection " + collection + \
                  "--file " + working_directory + json_file

# Before importing, drop collection if it exists
if collection in db.collection_names():
    print "Dropping collection"
    db[collection].drop()

# Executing the command
print "Executing : " + mongoimport_cmd
subprocess.call(mongoimport_cmd.split())
