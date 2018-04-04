# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
This py script has access_deallist_record function that can access the deallist record
It will return ETI deal name and directory for the deal.
It can gain full access of the deallist record
"""
import sys
from dbfread import DBF
from pandas import DataFrame

###############################################################################
# This function will have  acces to the d:\\deals\\remictax\deallist.dbf file
# The dbfread library can only read the deallist. It cannot modify  
# the record
def access_deallist_record():
    deallist = DBF("d:\\deals\\remictax\\deallist.dbf")
    deallist = DataFrame(iter(deallist))

    deal_range = range(0, len(deallist))
    deal_dict = {}
    
    print('Chosen deal(s) is/are: ')
    for deal in deal_range:
        if deallist['CHOSEN'][deal] == True:
            deal_dict.update({deallist['DEALNAME'][deal]:deallist['SUBDIR'][deal]})
            print(deallist['DEALNAME'][deal] + " " + deallist['SOURCE_NME'][deal] + " " + deallist['FULLNAME'][deal] + " " + deallist['SUBDIR'][deal])
    print('******************************************************************************')
        
    if not deal_dict:
        print('No deals are chosen!!!')
        print('Check out your deal list record!')
        sys.exit()
    else:
        print('Is/are the chosen deal(s) correct?')
        while True:
            user_input = input("Please choose [Y/N]: ")     
            try:
                if 'yes' in user_input.lower() or 'y' in user_input.lower():
                    print('Deal dictionary returned')
                    return deal_dict
                    break
                elif 'no' in user_input.lower() or 'n' in user_input.lower():
                    break
            except:
                continue