import xml.etree.cElementTree as ET
import pprint
import re
from collections import defaultdict
"""
Your task is to explore the data a bit more.
The first task is a fun one - find out how many unique users
have contributed to the map in this particular area!
The function process_map should return a set of unique user IDs ("uid")
"""

def get_user(element):
    return


def process_map(filename):
    users = defaultdict(int)
    for _, element in ET.iterparse(filename):
        uid = element.attrib.get('uid')
        if uid != None:
            users[uid] += 1

    return users


users = process_map('map')
print "No. Of Unique Users :"
pprint.pprint(len(users))

'''
if __name__ == "__main__":
    output()
'''
