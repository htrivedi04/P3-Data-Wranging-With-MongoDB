import xml.etree.ElementTree as ET
import pprint
from collections import defaultdict

import os
#Set the proper current working directory
#os.getcwd()
#os.chdir('C:\Users\Trivedi\Desktop\Data Analytics\P3')

def count_tags(filename):
    '''Iterate through each element in the file and add the relevant node name to a dictionary
    the first time with a value of 1 and then increment by 1 each time that node appears again.'''
    #initialize defaultdict to avoid KeyError and allow new keys not found in dictionary yet
    tags = defaultdict(int)
    #iterate through each node element and increment the dictionary value for that node.tag key
    for event, node in ET.iterparse(filename):
        if event == 'end': 
            tags[node.tag]+=1
        # discard the element is needed to clear from memory and speed up processing
        node.clear()             
    return tags

tags = count_tags('map')
pprint.pprint(tags)
