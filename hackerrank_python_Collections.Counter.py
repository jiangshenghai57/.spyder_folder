# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 17:57:55 2018

@author: Shenghai
"""

from collections import Counter

X = int(input())
shoe_size = list(input().split())
shoe_size = [int(i) for i in shoe_size if int(i)]

#print(X)
#print(shoe_size)

N = int(input())
cust_dict = {}
for i in range(0, N):
    cus = input().split()
    cus = [int(i) for i in cus if int(i)]
    if cus[0] not in cust_dict:
        cust_dict.update({cus[0]: [cus[1]]})
    else:
        cust_dict[cus[0]].append(cus[1])

c = Counter(shoe_size)

tot_money = 0
for key in c.keys():
    if key in cust_dict.keys():
        for i in range(0, c[key]):
            if i < len(cust_dict[key][:]):
                tot_money += cust_dict[key][i]

print(tot_money)