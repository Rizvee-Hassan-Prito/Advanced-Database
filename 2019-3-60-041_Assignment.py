# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 17:08:55 2023

@author: User
"""

with open('run1.txt', 'r') as f1:
    arr1 = list(map(int, f1.read().split()))

with open('run2.txt', 'r') as f2:
    arr2 = list(map(int, f2.read().split()))


#%%

sorted_list = []
i = 0
j = 0

while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
        sorted_list.append(arr1[i])
        i+=1
    else:
        sorted_list.append(arr2[j])
        j+=1

while i < len(arr1):
    sorted_list.append(arr1[i])
    i+=1
while j < len(arr2):
    sorted_list.append(arr2[j])
    j+=1

#%%

with open('sorted.txt', 'w') as f:
    f.write('\n'.join(map(str, sorted_list)))
