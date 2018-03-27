# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 14:31:16 2018

@author: Shenghai
"""

import os

path = '//brian/d/deals/carrington/smac/'


deals = list(os.listdir(path))
brian_deals = []

for deal in deals:
    if len(deal) == 7:
        brian_deals.append(deal)
        
print(brian_deals)