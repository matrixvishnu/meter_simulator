import time
import numpy as np
import pandas as pd
meterid=['123h','345i','567j','678k','234l']
for k in range(len(meterid)):
    name=meterid[k]
    randomid=str(np.random.randint(1000000,800000000))
    pwd="HELLO"
    numofparameters="28"
    ethernetpktsize='1'
    numofretries=str(np.random.randint(1,10))
    #nth_packet_of_total_packets='1-1'
    nth_parameter_of_total_parameter =list(range(1,28,1))
    datatype = "25"
    version="0"
    obiscode=['0.0.1.0.0.255',
              '0.0.96.6.2.255',
              '0.b.96.12.5.255',
              '0.b.96.12.6.255',
              '1.0.31.27.0.255',
              '1.0.51.27.0.255',
              '1.0.71.27.0.255',
              '1.0.32.27.0.255',
              '1.0.52.27.0.255',
              '1.0.72.27.0.255',
              '1.0.1.29.0.255',
              '1.0.2.29.0.255',
              '1.0.5.29.0.255',
              '1.0.6.29.0.255',
              '1.0.7.29.0.255',
              '1.0.8.29.0.255',
              '1.0.9.29.0.255',
              '1.0.10.29.0.255',
              '1.0.1.8.0.255',
              '1.0.2.8.0.255',
              '1.0.9.8.0.255',
              '1.0.10.8.0.255',
              '1.0.94.91.1.255',
              '1.0.94.91.2.255',
              '1.0.5.8.0.255',
              '1.0.6.8.0.255',
              '1.0.7.8.0.255',
              '1.0.8.8.0.255']
    value="value"
    scalar="0"
    numofattributes="2"
    attributelistpointer="2"
    fh=open(name,"w")
    data =input("Which data(live or historical) to be generated:")
    cme=input("Enter a value for Cumulative energy,kWh(Import)INItial:")
    print("Live data is being generated....")
    for j in range(1):
        fh.write("_id:"+"ObjectId("+ randomid+ ')'+"\n")
        fh.write("Data:"+"09.18.01."+name+'|'+pwd+'|'+numofparameters+'|'+ethernetpktsize+'|'+numofretries+'\n')
        for i in range(28):
            for l in obiscode:
                for m in v:
                    fh.write( "1-1"+'|'+str(i)+"-28"+'|'+datatype+'|'+version+'|'+str(l)+'|'+value+'|'+str(m.encode("utf-8"))+'|'+scalar+'|'+numofattributes+'|'+attributelistpointer+'|'+'\n')
        fh.write(time.ctime()+"\n")
        time.sleep(.01)
    fh.close()
    print("live data has been generated for 30secs")


