import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

osm_file = open("map", "r")
address_count = 0

def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")

for event, elem in ET.iterparse(osm_file, events=("start",)):
    if elem.tag == "node" or elem.tag == "way":
        for tag in elem.iter("tag"):
            if is_street_name(tag):
                address_count += 1


print address_count

