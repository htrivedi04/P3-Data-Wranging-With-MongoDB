"""
Your task in this exercise has two steps:
- audit the OSMFILE and change the variable 'mapping' to reflect the changes needed to fix 
    the unexpected street types to the appropriate ones in the expected list.
    You have to add mappings only for the actual problems you find in this OSMFILE,
    not a generalized solution, since that may and will depend on the particular area you are auditing.
- write the update_name function, to actually fix the street name.
    The function takes a string with street name as an argument and should return the fixed name
    We have provided a simple test so that you see what exactly is expected
"""
import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

OSMFILE = "map"
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)


expected = ["Road", "Marg", "Place", "Lane", "Kunj", "Colony", "Estate", "Nagar",
            "Lines", "Enclave", "Expressway", "Market", "Extension", "Area", "Chowk", "Complex"]

# UPDATE THIS VARIABLE
mapping = { 'road' : "Road",
            'Rd' : "Road",
            'lane' : "Lane",
            'nagar' : "Nagar",
            'marg' : "Marg",
            'lane' : "Lane",
            'area' : "Area",
            'vihar' : "Vihar",
            'up' : "U.P",
            'UP' : "U.P",
            'UP)' : "U.P",
            'U.P)' : "U.P",
            '(UP)' : "(U.P)",
            'colony' : "Colony"
            }
           
def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)


def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")


def audit(osmfile):
    osm_file = open(osmfile, "r")
    street_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])
    elem.clear()    # Clear from memory
    return street_types


def process_match(m):
    if mapping.get(m.group()) != None:
        return mapping.get(m.group())
    else:
        return m.group()
    return 


def update_name(name, mapping, regex): 
    m = regex.search(name)
    if m:
        match = m.group()

        if match in mapping:
            name = re.sub(regex, mapping[match], name)
    return name


def test():
    st_types = audit(OSMFILE)
    #pprint.pprint(dict(st_types))

    for st_type, ways in st_types.iteritems():
        if st_type in mapping:
            for name in ways:
                better_name = update_name(name, mapping, street_type_re)
                print name, "=>", better_name.title()
                
if __name__ == '__main__':
    test()
