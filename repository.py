#!/usr/bin/python

import datetime
import csv
import random
import math
from csv import DictReader
import pandas as pd
import numpy as np

import sys 
import fnmatch
def V(wildcard):
    variables = sys._getframe(1).f_locals
    rets = []
    for var in variables.keys():
        if fnmatch.fnmatch(var, wildcard):
            rets.append(variables[var])

    return rets


tep ='6'
n_t_e_p = str(random.randint(1,6))
ethpack =n_t_e_p+'-'+tep

tot_para = '28'
datatype = '25'
version = '0'
scalar = '0'
number_of_attributes='2'
attribute_list_pointer = '2'
sep = '|'
sp1 = '-'

post_value = sep+scalar+sep+number_of_attributes+sep+attribute_list_pointer

dty_ver =datatype+sep+version


pre_value_Real_time_Clock_Date_and_Time         = ethpack + sep + '1'  + sp1 + tot_para + sep + dty_ver + sep + '0.0.1.0.0.255'   + sep
pre_value_Battery_voltage                       = ethpack + sep + '2'  + sp1 + tot_para + sep + dty_ver + sep + '0.0.96.6.2.255'  + sep
pre_value_GSM_field_Strenth                     = ethpack + sep + '3'  + sp1 + tot_para + sep + dty_ver + sep + '0.b.96.12.5.255' + sep
pre_value_Telephone_No                          = ethpack + sep + '4'  + sp1 + tot_para + sep + dty_ver + sep + '0.b.96.12.6.255' + sep
pre_value_Current_IR                            = ethpack + sep + '5'  + sp1 + tot_para + sep + dty_ver + sep + '1.0.31.27.0.255' + sep
pre_value_Current_IY                            = ethpack + sep + '6'  + sp1 + tot_para + sep + dty_ver + sep + '1.0.51.27.0.255' + sep
pre_value_Current_IB                            = ethpack + sep + '7'  + sp1 + tot_para + sep + dty_ver + sep + '1.0.71.27.0.255' + sep
pre_value_Voltage_VRN                           = ethpack + sep + '8'  + sp1 + tot_para + sep + dty_ver + sep + '1.0.32.27.0.255' + sep
pre_value_Voltage_VYN                           = ethpack + sep + '9'  + sp1 + tot_para + sep + dty_ver + sep + '1.0.52.27.0.255' + sep
pre_value_Voltage_VBN                           = ethpack + sep + '10' + sp1 + tot_para + sep + dty_ver + sep + '1.0.72.27.0.255' + sep
pre_value_Block_energy_kWhImport                = ethpack + sep + '11' + sp1 + tot_para + sep + dty_ver + sep + '1.0.1.29.0.255'  + sep
pre_value_Block_energy_kWhExpor                 = ethpack + sep + '12' + sp1 + tot_para + sep + dty_ver + sep + '1.0.2.29.0.255'  + sep
pre_value_Block_energykVAhImport                = ethpack + sep + '13' + sp1 + tot_para + sep + dty_ver + sep + '1.0.9.29.0.255'  + sep
pre_value_Block_energykVAhExpor                 = ethpack + sep + '14' + sp1 + tot_para + sep + dty_ver + sep + '1.0.10.29.0.255' + sep
pre_value_Block_energykvarh_Q2                  = ethpack + sep + '15' + sp1 + tot_para + sep + dty_ver + sep + '1.0.6.29.0.255'  + sep
pre_value_Block_energykvarh_Q1                  = ethpack + sep + '16' + sp1 + tot_para + sep + dty_ver + sep + '1.0.5.29.0.255'  + sep
pre_value_Block_energykvarh_Q3                  = ethpack + sep + '17' + sp1 + tot_para + sep + dty_ver + sep + '1.0.7.29.0.255'  + sep
pre_value_Block_energykvarh_Q4                  = ethpack + sep + '18' + sp1 + tot_para + sep + dty_ver + sep + '1.0.8.29.0.255'  + sep
pre_value_Cumulative_energykWhImport            = ethpack + sep + '19' + sp1 + tot_para + sep + dty_ver + sep + '1.0.1.8.0.255'  + sep
pre_value_Cumulative_energykWhExport            = ethpack + sep + '20' + sp1 + tot_para + sep + dty_ver + sep + '1.0.2.8.0.255'  + sep
pre_value_Cumulative_energykVAh_while_kW_Import = ethpack + sep + '21' + sp1 + tot_para + sep + dty_ver + sep + '1.0.9.8.0.255'  + sep
pre_value_Cumulative_energykVAh_while_kW_Export = ethpack + sep + '22' + sp1 + tot_para + sep + dty_ver + sep + '1.0.10.8.0.255'  + sep
pre_value_Cumulative_energykvarh_Quardrant_1    = ethpack + sep + '23' + sp1 + tot_para + sep + dty_ver + sep + '1.0.5.8.0.255'  + sep
pre_value_Cumulative_energykvarh_Quardrant_2    = ethpack + sep + '24' + sp1 + tot_para + sep + dty_ver + sep + '1.0.6.8.0.255'  + sep
pre_value_Cumulative_energykvarh_Quardrant_3    = ethpack + sep + '25' + sp1 + tot_para + sep + dty_ver + sep + '1.0.7.8.0.255'  + sep
pre_value_Cumulative_energykvarh_Quardrant_4    = ethpack + sep + '26' + sp1 + tot_para + sep + dty_ver + sep + '1.0.8.8.0.255'  + sep
pre_value_Reactive_energy_high                  = ethpack + sep + '27' + sp1 + tot_para + sep + dty_ver + sep + '1.0.94.91.1.255'  + sep
pre_value_Reactive_energy_low                   = ethpack + sep + '28' + sp1 + tot_para + sep + dty_ver + sep + '1.0.94.91.2.255'  + sep

x=V('pre*')
print x


