import os
import pymongo
from pymongo import MongoClient
import datetime
import json

##os.system("ping 8.8.8.8 -t")
##os.system("snmpget -v 1 -c demopublic test.net-snmp.org sysUpTime.0")
#client = MongoClient('localhost', 27017)
#db = client['test']
##cursor = db.players.find()
##for i in cursor:
##   print i

#coll = db.aa
#temp = {"a":8,"b":8}

##coll.insert_one(temp).inserted_id
##db.aa.drop()
#a = db.aa.find({"a":7})
#print a
#print list(a)
##for i in a:
##    print i

##result = db.aa.delete_one({'a': 7})

##b = db.aa.count({'a'})
##print b

a = os.system("snmpwalk -v 2c -c test 192.168.1.2 .1.3.6.1.2.1.4.20.1.1")
print a
print list(a)