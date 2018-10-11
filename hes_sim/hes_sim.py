import texttoxml as t_xml
import xml_merge
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


ip_dir_path = '/home/vishnu/Documents/meter_simulator/output/'
ip_file_ext = '*.txt'
ip_files = glob.glob(ip_dir_path+ip_file_ext)

x= t_xml.Hes()
for i in ip_files:
    x.ip_file = i
    x.xml_gen()

