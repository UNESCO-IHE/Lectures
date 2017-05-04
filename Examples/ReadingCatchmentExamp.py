# -*- coding: utf-8 -*-
"""
Created on Thu Oct 02 13:47:44 2014

@author: gco
"""
from pandas import *
import pandas
import re
import numpy as np
import linecache
#import MySQLdb


def skiplines(f,n):
    for i in range (1,n):
        f.next();

#==============================================================================
f = open('doushan(73-91).txt', 'r');
myvec=[];
StationNames=[];
count=1;
pos=1;
entro=0;
for line in f:
     line = line.strip();
     columns = line.split();
     if len(columns)>0:
         if columns[0]=='STATION':
             StationNames.append(columns[1])
         # print "Column zero is"+repr(columns[0])
         #if columns[0]=='1':
         #if any("TEMPERATURE" in s for s in columns):  
         if re.search('TEMPERATURE',line) and columns[0]=='HOURLY':
             #print "entro"+repr(columns)   
             entro=1
             pos=1
             #print "entro - "+repr(columns)   
             #cmpa=int(columns[-1])
             #if cmpa==1:
         if entro==1:
             pos=pos+1;             
             if columns[0]=='1':
                 myvec.append(count);         
                 entro=0
                 pos=1

#==============================================================================
     count=count+1
f.close   
mylist=[];
StationTemp=[];
ColumnH=[];

for i in range(1,32):
    mylist.append(str(i));
    
for i in range(1,23):
    ColumnH.append('H'+str(i));    
    
count=0;
f = open('doushan(73-91).txt', 'r')

df=DataFrame(columns=ColumnH); 
for k in range(1,len(myvec)+1):
    if k==1:
        for i in range(1,myvec[k-1]+1):
            line = f.readline()
    else:
        while i<myvec[k-1]:
            line = f.readline()
            i=i+1
            
    #fw= open('Temperature'+str(k)+'.txt','w');
    
    #df      
    line = line.strip()
    columns = line.split()
    while any(columns[0] in s for s in mylist):
        print "entro - "+repr(columns) 
        df.loc[count]=columns        
     #   for item in columns: 
     #       fw.write("%s," % item)        
     #   fw.write("\n")    
        line = f.readline()
        line = line.strip()
        columns = line.split()
        StationTemp.append(columns)
        count=count+1
      #  fw.close
        i=i+1
    

f.close
df.to_csv('TemperatureAll.txt', sep='\t')   
  
#==============================================================================
# count=1;
# for k in range(1,len(myvec)+1):
#      line=linecache.getline('abali(92-2010).txt',myvec[k-1]+count) 
#      line = line.strip()
#      columns = line.split()
#      print "Mas facil"+repr(columns)
#      while any(columns[0] in s for s in mylist):
#          line=linecache.getline('abali(92-2010).txt',myvec[k-1]+count)       
#          line = line.strip()
#          columns = line.split()
#          print "Mas facil"+repr(columns)
#          count=count+1;    
#==============================================================================
#==============================================================================
#      count=1
#==============================================================================
