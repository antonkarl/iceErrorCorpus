from pathlib import Path
import xml.etree.ElementTree as ET

basedir = 'data/wikipedia'
file_list = list(Path(basedir).rglob('*.xml'))

correct_codes = set()
f = open('correctCodes.txt', 'r')
lines = f.readlines()
for line in lines:
    line = line.rstrip()
    correct_codes.add(line)

all_codes = set()

for file in file_list:
    tree = ET.parse(file)
    root = tree.getroot()
    for child in root:
        if child.tag == '{http://www.tei-c.org/ns/1.0}text':
            for x in child[0][0][0]:
                if x.tag == '{http://www.tei-c.org/ns/1.0}revision':
                    for key, value in x[2][0].attrib.items():
                        if key == 'xtype':
                            all_codes.add(value)
                            #print(key, value)
                        #print(key, value)
                    #print(x[2][0].attrib)
                        #print(y[0])

diff = all_codes - correct_codes
print(diff)

for file in file_list:
    tree = ET.parse(file)
    root = tree.getroot()
    for child in root:
        if child.tag == '{http://www.tei-c.org/ns/1.0}text':
            for x in child[0][0][0]:
                if x.tag == '{http://www.tei-c.org/ns/1.0}revision':
                    for key, value in x[2][0].attrib.items():
                        if value in diff:
                            print(value)
                            print(file)
                            #print(key, value)
                        #print(key, value)
                    #print(x[2][0].attrib)
                        #print(y[0])