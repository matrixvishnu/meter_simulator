#!/usr/bin/python
from progressbar import ProgressBar
from dicttoxml import dicttoxml
import traceback
import time
import datetime
import csv
from random import *
import math
from csv import DictReader
import pandas as pd
import numpy as np
import threading
import uuid
import glob

import xml.etree.cElementTree as ET

class Hes():
    ip_dir_path = '/home/vishnu/Documents/meter_simulator/output/'
    ip_file_ext = '*.txt'
    ip_files = glob.glob(ip_dir_path+ip_file_ext)
   # print ip_files
    ip_file = 'mtr.txt'
    def xml_gen(self):
        f = open(self.ip_file, "r")
        lines = f.readlines()
        f.close()
        string1 = lines[2]
        st2 = string1.split("|")
        st3 = st2[0].split(".")
        mtr_no = st3[-1]
        l_ip_obis_para = lines[3:-1]
        obis_para={'0.0.1.0.0.255'  : 'REAL_TIME_CLOCK_DATE_AND_TIME',
                   '0.0.96.6.2.255' : 'BATTERY_VOLTAGE',
                   '0.b.96.12.5.255': 'GSM_FIELD_STRENTH',
                   '0.b.96.12.6.255': 'TELEPHONE_NO',
                   '1.0.31.27.0.255': 'CURRENT_IR',
                   '1.0.51.27.0.255': 'CURRENT_IY',
                   '1.0.71.27.0.255': 'CURRENT_IB',
                   '1.0.32.27.0.255': 'VOLTAGE_VRN',
                   '1.0.52.27.0.255': 'VOLTAGE_VYN',
                   '1.0.72.27.0.255': 'VOLTAGE_VBN',
                   '1.0.1.29.0.255' : 'BLOCK_ENERGY_KWHIMPORT',
                   '1.0.2.29.0.255' : 'BLOCK_ENERGY_KWHEXPOR',
                   '1.0.9.29.0.255' : 'BLOCK_ENERGYKVAHIMPORT',
                   '1.0.10.29.0.255': 'BLOCK_ENERGYKVAHEXPOR',
                   '1.0.6.29.0.255' : 'BLOCK_ENERGYKVARH_Q2',
                   '1.0.5.29.0.255' : 'BLOCK_ENERGYKVARH_Q1',
                   '1.0.7.29.0.255' : 'BLOCK_ENERGYKVARH_Q3',
                   '1.0.8.29.0.255' : 'BLOCK_ENERGYKVARH_Q4',
                   '1.0.1.8.0.255'  : 'CUMULATIVE_ENERGYKWHIMPORT',
                   '1.0.2.8.0.255'  : 'CUMULATIVE_ENERGYKWHEXPORT',
                   '1.0.9.8.0.255'  : 'CUMULATIVE_ENERGYKVAH_WHILE_KW_IMPORT',
                   '1.0.10.8.0.255' : 'CUMULATIVE_ENERGYKVAH_WHILE_KW_EXPORT',
                   '1.0.5.8.0.255'  : 'CUMULATIVE_ENERGYKVARH_QUARDRANT_1',
                   '1.0.6.8.0.255'  : 'CUMULATIVE_ENERGYKVARH_QUARDRANT_2',
                   '1.0.7.8.0.255'  : 'CUMULATIVE_ENERGYKVARH_QUARDRANT_3',
                   '1.0.8.8.0.255'  : 'CUMULATIVE_ENERGYKVARH_QUARDRANT_4',
                   '1.0.94.91.1.255': 'REACTIVE_ENERGY_HIGH',
                   '1.0.94.91.2.255': 'REACTIVE_ENERGY_LOW'}
        obis_val = {}
        for i in l_ip_obis_para:
            l = i.split("|")
            obiscode = l[4]
            value    = l[5]
            obis_val[obiscode] = value
            #print 'obis code --' +obiscode + '  value --'+value 
        #print obis_val
        para_value = {}
        for i in obis_val:
            para = obis_para[i]
            val  = obis_val[i]
           # print para + '---'+val
            para_value[para] = val
        para_value['METER_NO'] = mtr_no
        time = para_value['REAL_TIME_CLOCK_DATE_AND_TIME']
        op_xml = dicttoxml(para_value, custom_root='G_MTR_ID', attr_type=False)
        op_dir = '/home/vishnu/Documents/meter_simulator/hes_sim/opxml/'
        f_o_xml = op_dir+mtr_no+time+'.xml'
        out_file = open(f_o_xml,'w')
        out_file.write(op_xml) 
       # print op_xml
       # print para_value
        #print l2
        #print '****************'
        #print lines
        #print string1
        #print st2
        #print st3
        #print st3[-1]

ip_dir_path = '/home/vishnu/Documents/meter_simulator/output/'
ip_file_ext = '*.txt'
ip_files = glob.glob(ip_dir_path+ip_file_ext)

x= Hes()
pbar = ProgressBar()
print 'Generating XML From Meter Data'
for j in pbar(ip_files):
    for i in ip_files:
        x.ip_file = i
        x.xml_gen()
        #print 'generating xml files from METER DATA'
   

xml_ip_dir = '/home/vishnu/Documents/meter_simulator/hes_sim/opxml/'
xml_ip_file_ext = '*.xml'
xml_ip_file = xml_ip_dir+xml_ip_file_ext
xml_ip_files = glob.glob(xml_ip_file)

root = ET.Element("LPSUBGROUPDATA")
doc = ET.SubElement(root, "LIST_G_METERDATA")

op_file = 'load_profile.xml'
pbar = ProgressBar()
print 'Consolidating xml files'
for j in pbar(ip_files):
    for ifl in xml_ip_files:
        e=ET.parse(ifl).getroot()
        doc.append(e)
tree = ET.ElementTree(root)
tree.write(op_file)


