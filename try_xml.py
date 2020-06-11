import xml.etree.ElementTree as ET
import glob

file_list = glob.glob('data/onlineNews/*')

for file in file_list:
    #content = 'verslo/*.xml'
    print(file)
    tree = ET.parse(file)
    root = tree.getroot()

#root = ET.fromstring('general/essays/uppfaert/tei1/verslo-JA4-t12.xml')
#root = ET.fromstring('general/onlineNews/tei1/visir-2014_07_125[1042]-t3.xml')
#fixed = original_response.replace(b'\x0c', b'')
#tree = ET.fromstring(fixed, ET.XMLParser(encoding='utf-8'))
#tree

# Fjarlægja fyrstu tvær línur í skjali:
# tail -n +3 prof.txt.txt > prof2.txt