# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import OpenOPC as op

#OPC_Server_Name_def='KEPware.KEPServerEx.V4'
Connect_Flag=False
config_filename='tosave.csv'
index=0
index_opc_name_in_file=0
index_item_in_file=1

item_name=''
item_group=''
item_location=''

item_name_data=[]
item_group_data=[]
item_location_data=[]

fr=open(config_filename,'r')
lines=fr.readlines()
for line in lines:
    items=line.strip().split(',')
    if index==index_opc_name_in_file:
        OPC_Server_Name_def=items[1]
    if index==index_item_in_file:
        item_name=items[0]
        item_group=items[1]
        item_location=items[2]
    if index>index_item_in_file:    
        item_name_data.append(items[0])
        item_group_data.append(items[1])
        item_location_data.append(items[2])
    index=index+1
    
#print(OPC_Server_Name_def)    
#print(item_location_data)
print(len(item_location_data))      

opc=op.client()

if OPC_Server_Name_def in opc.servers():
    opc.connect(OPC_Server_Name_def)
    print(OPC_Server_Name_def+" is running!")
    Connect_Flag=True  
else:
    print(OPC_Server_Name_def+" is not running!")
    
      
if Connect_Flag==True:
    for i in range(len(item_location_data)):
        Item_Value=opc.read(item_location_data[i])
        #print(Item_Value[0])
        for j in range(len(Item_Value)):
            print(Item_Value[j])
        
#print(opc.list())
opc.close()