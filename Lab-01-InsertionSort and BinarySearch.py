# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 21:58:06 2023

@author: User
"""

array=[]

while(1):
  cmd=int(input("\nEnter cmd number:"))
  value=int(input("Enter value number:"))
  
  if(cmd==0):
    if(value not in array):
          if(len(array)==0):
            array.append(value)
          elif(array[0]>value):
            array.insert(0,value)
          elif(array[len(array)-1]<value):
            array.insert(len(array),value)
          else:
              i=len(array)-1
              while(i>=0):
                if(array[i]<value):
                  array.insert(i+1,value)
                  break
                i = i-1                     
    print(array)
  if(cmd==1):
    result=-1
    s=0
    e=len(array)-1
    while(s<=e):
      m=int((s+e)/2)
      if(array[m]<=value):
        s=m+1
        result=array[m]
      else:
         e=m-1
    if(result==value): 
        print("Found:",result)
    else:
        result=-1
        print("Not Found:",result)