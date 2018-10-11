#!/usr/bin/python
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
import repository as rp
import os

df_lp_blck_g = pd.DataFrame(columns = ['mtr_no','Real_time_Clock_Date_and_Time','Block_energy_kWhImport', 'Block_energykVAhImport','Block_energykvarh_Q2'])

class Loadprofile():
    mtr_no = '123mtr'
    Cumulative_energykWhImportInitial  = 2000
    def non_cum(self):
        mtr_no                        = self.mtr_no
        df_lp_blck                    = pd.DataFrame()
        Real_time_Clock_Date_and_Time = datetime.datetime.now()
        Battery_voltage               = round(np.random.uniform(2, 7),2)
        GSM_field_Strength            = round(np.random.uniform(2, 7),2)
        Telephone_No                  = '9848023221'
        Current_IR                    = round(np.random.uniform(5,20,size=None),2)
        Current_IY                    = Current_IR
        Current_IB                    = Current_IR
        Voltage_VRN                   = round(np.random.uniform(220,240),2)
        Voltage_VYN                   = Voltage_VRN
        Voltage_VBN                   = Voltage_VRN
        Block_energy_kWhImport         = round(np.random.uniform(0.12,0.22),2)
        Block_energy_kWhExpor         = 0
        PF                            = round(np.random.uniform(0.89,0.99),2)
        Block_energykVAhImport         = round(Block_energy_kWhImport/PF,2)
        Block_energykVAhExpor         = 0
        Block_energykvarh_Q2          = round(np.sqrt(np.power(Block_energykVAhImport,2)-np.power(Block_energy_kWhImport,2)),2)
        Block_energykvarh_Q1          = 0
        Block_energykvarh_Q3          = 0
        Block_energykvarh_Q4          = 0
        global df_lp_blck_g
        df_lp_blck_g =  df_lp_blck_g.append({'mtr_no' : mtr_no,
        'Real_time_Clock_Date_and_Time'           : Real_time_Clock_Date_and_Time,
        'Block_energy_kWhImport'                   : Block_energy_kWhImport,
        'Block_energykVAhImport'                   : Block_energykVAhImport,
        'Block_energykvarh_Q2'                    : Block_energykvarh_Q2}, ignore_index=True)


        df_lp_blck = df_lp_blck_g[(df_lp_blck_g.mtr_no == mtr_no)]

	Cumulative_energykWhImportInitial             = self.Cumulative_energykWhImportInitial
	Cumulative_energykWhImport                    = Cumulative_energykWhImportInitial+df_lp_blck.Block_energy_kWhImport.sum()
	Cumulative_energykWhExport                    = 0
	Cumulative_energykVAh_while_kW_Import_INITIAL = round(Cumulative_energykWhImportInitial/ np.random.uniform(0.89,0.99),2)
	Cumulative_energykVAh_while_kW_Import         = round(Cumulative_energykVAh_while_kW_Import_INITIAL + df_lp_blck.Block_energykVAhImport.sum(),2)
        Cumulative_energykVAh_while_kW_Export         = 0
        Cumulative_energykvarh_Quardrant_1  = 0
        Cumulative_energykvarh_Quardrant_2=round(np.sqrt(np.power(Cumulative_energykVAh_while_kW_Import,2)-np.power(Cumulative_energykWhImport,2)),2)
        Cumulative_energykvarh_Quardrant_3=0
        Cumulative_energykvarh_Quardrant_4=0
        Reactive_energy_high = 0
        Reactive_energy_low  = 0
        def prvar(__x):
            print traceback.extract_stack(limit=2)[0][3][6:][:-1],"=",__x
        #prvar(Cumulative_energykWhImport)
        l1=   [rp.pre_value_Real_time_Clock_Date_and_Time         + str(Real_time_Clock_Date_and_Time)         + rp.post_value, 
               rp.pre_value_Battery_voltage                       + str(Battery_voltage)                       + rp.post_value,
               rp.pre_value_GSM_field_Strenth                     + str(GSM_field_Strength)                    + rp.post_value, 
               rp.pre_value_Telephone_No                          + str(Telephone_No)                          + rp.post_value, 
               rp.pre_value_Current_IR                            + str(Current_IR)                            + rp.post_value, 
               rp.pre_value_Current_IY                            + str(Current_IY)                            + rp.post_value, 
               rp.pre_value_Current_IB                            + str(Current_IB)                            + rp.post_value, 
               rp.pre_value_Voltage_VRN                           + str(Voltage_VRN)                           + rp.post_value, 
               rp.pre_value_Voltage_VYN                           + str(Voltage_VYN)                           + rp.post_value, 
               rp.pre_value_Voltage_VBN                           + str(Voltage_VBN)                           + rp.post_value, 
               rp.pre_value_Block_energy_kWhImport                + str(Block_energy_kWhImport)                + rp.post_value, 
               rp.pre_value_Block_energy_kWhExpor                 + str(Block_energy_kWhExpor)                 + rp.post_value, 
               rp.pre_value_Block_energykVAhImport                + str(Block_energykVAhImport)                + rp.post_value, 
               rp.pre_value_Block_energykVAhExpor                 + str(Block_energykVAhExpor)                 + rp.post_value, 
               rp.pre_value_Block_energykvarh_Q2                  + str(Block_energykvarh_Q2)                  + rp.post_value, 
               rp.pre_value_Block_energykvarh_Q1                  + str(Block_energykvarh_Q1)                  + rp.post_value, 
               rp.pre_value_Block_energykvarh_Q3                  + str(Block_energykvarh_Q3)                  + rp.post_value, 
               rp.pre_value_Block_energykvarh_Q4                  + str(Block_energykvarh_Q4)                  + rp.post_value, 
               rp.pre_value_Cumulative_energykWhImport            + str(Cumulative_energykWhImport)            + rp.post_value, 
               rp.pre_value_Cumulative_energykWhExport            + str(Cumulative_energykWhExport)            + rp.post_value, 
               rp.pre_value_Cumulative_energykVAh_while_kW_Import + str(Cumulative_energykVAh_while_kW_Import) + rp.post_value, 
               rp.pre_value_Cumulative_energykVAh_while_kW_Export + str(Cumulative_energykVAh_while_kW_Export) + rp.post_value, 
               rp.pre_value_Cumulative_energykvarh_Quardrant_1    + str(Cumulative_energykvarh_Quardrant_1)    + rp.post_value, 
               rp.pre_value_Cumulative_energykvarh_Quardrant_2    + str(Cumulative_energykvarh_Quardrant_2)    + rp.post_value, 
               rp.pre_value_Cumulative_energykvarh_Quardrant_3    + str(Cumulative_energykvarh_Quardrant_3)    + rp.post_value, 
               rp.pre_value_Cumulative_energykvarh_Quardrant_4    + str(Cumulative_energykvarh_Quardrant_4)    + rp.post_value, 
               rp.pre_value_Reactive_energy_high                  + str(Reactive_energy_high)                  + rp.post_value, 
               rp.pre_value_Reactive_energy_low                   + str(Reactive_energy_low)                   + rp.post_value]
         
        output = '\n'.join(l1)
        return output
    def obj(self):
        def my_random_string(string_length=10):
            random = str(uuid.uuid4())
            random = random.upper()
            random = random.replace("-","")
            return random[0:string_length]
        mtr_no = self.mtr_no
        objid = my_random_string(10)
        objectid ='"'+'_id'+'"'+':'+ '"'+'ObjectId'+'"'+'('+objid+')'
        data ='"'+ 'data'+'"'+':'+'"'+'09.18.01.'+str(mtr_no)+'|'+'PASSWORD'+'|'+'28'+'|'+'1'+'|'+'1'      
        op = objectid +'\n'+ data
        return op
       
x = Loadprofile()
r = ['mtr1','mtr2','mtr3']
while True:
    for i in r:
        x.mtr_no = i
        result = x.non_cum()
        #print result
        r1 = x.obj()
        #print r1
        finalop = '{'+'\n'+r1+'\n'+result+'\n'+'}'
        #print finalop
        time_stamp = datetime.datetime.now()
        filepath = '/home/vishnu/Documents/meter_simulator/output/'
        fname = filepath+str(x.mtr_no)+'-'+str(time_stamp)+'.txt'
        fle =open(fname,"w")
        fle.write(finalop)
    #print df_lp_blck_g
    print '........Generating meter data ........'
    for i in os.listdir('/home/vishnu/Documents/meter_simulator/output/'):
        print i
    time.sleep(10)
#print rp.pre_value_Real_time_Clock_Date_and_Time 
