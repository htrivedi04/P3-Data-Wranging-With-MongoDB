import xml.etree.cElementTree as ET
import re
import pprint


OSMFILE = "map"

VALID_POSTAL = re.compile('\d\d\d\d\d\d')
# NON-BREAKING HYPHEN
INVALID_POSTAL_NON_BREAKING_HYPHEN = re.compile(u'\d\d\d\d\d\d')
INVALID_POSTAL_MISSING_HYPHEN = re.compile('\d\d\d\d')


def fixed_postal_code(code):
    if VALID_POSTAL.match(code):
        return (code, code)
    elif INVALID_POSTAL_NON_BREAKING_HYPHEN.match(code):
        fixed = code[0:2] + '-' + code[2:]
        return (code, fixed)
    elif INVALID_POSTAL_MISSING_HYPHEN.match(code):
        fixed = code[0:2] + '-' + code[2:]
        return (code, fixed)
    else:
        print code
        msg = u'Invalid postal code: {0}'.format(code)
        raise Exception(msg)


def find_postal_issues(osmfile):
    osm_file = open(osmfile, "r")
    valid = {}
    invalid = {}

    for event, elem in ET.iterparse(osm_file, events=("start",)):
        if elem.tag == 'node':
            for tag in elem.iter('tag'):
                k = tag.get('k')
                if k == "addr:postcode":
                    v = tag.get('v')
                    v, fixed = fixed_postal_code(v)
                    if v == fixed:
                        valid[v] = v
                    else:
                        invalid[v] = fixed
    return valid, invalid


def report_postal_issues():
    valid_postal, invalid_postal = find_postal_issues(OSMFILE)
    print '# of valid postal codes: ', len(valid_postal)
    print '# of invalid postal codes: ', len(invalid_postal)
    print
    print 'Invalid postal codes:'
    pprint.pprint(invalid_postal)


if __name__ == '__main__':
    report_postal_issues()
