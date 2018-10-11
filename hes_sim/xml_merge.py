#!/usr/bin/python

import glob
import xml.etree.cElementTree as ET

ip_dir = '/home/vishnu/Documents/meter_simulator/hes_sim/opxml/'
ip_file_ext = '*.xml'
ip_file = ip_dir+ip_file_ext
ip_files = glob.glob(ip_file)

root = ET.Element("LPSUBGROUPDATA")
doc = ET.SubElement(root, "LIST_G_METERDATA")

op_file = 'load_profile.xml'
for ifl in ip_files:
    e=ET.parse(ifl).getroot()
    doc.append(e)
tree = ET.ElementTree(root)
tree.write(op_file)




#root = ET.Element("LPSUBGROUPDATA")
#doc = ET.SubElement(root, "LIST_G_METERDATA")
#ET.SubElement(doc, "field1", name="blah").text = "some value1"
#ET.SubElement(doc, "field2", name="asdfasd").text = "some vlaue2"
#tree = ET.ElementTree(root)
#print tree
#tree.write("filename.xml")

#print ip_files


