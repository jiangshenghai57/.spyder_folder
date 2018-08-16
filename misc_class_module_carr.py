# -*- coding: utf-8 -*-
"""
Created on Thu May 17 16:51:03 2018

@author: Shenghai

This class module has miscellaneous functions such as 
user_input() to ask user to prompt in distribution month and year 
and is_empty() function and etc.
"""

import numpy as np

class Miscellaneous:
       
###############################################################################
# Take yymm as an argument such 1804 (2018 April)
# return yymm of last month
    def last_mon(dist_date):
        if int(dist_date[-2:]) == 1:
            last_mon = 12
            cur_yr = int(dist_date[0:2])
            last_yr = cur_yr - 1
            last_mon = str(last_yr) + str(last_mon)
        else:
            if (int(dist_date[-2:]) - 1) < 10:
                cur_mon = int(dist_date[-2:])
                last_mon = cur_mon - 1
                cur_yr = int(dist_date[0:2])
                last_mon = str(cur_yr) + "0" + str(last_mon)
            else:
                cur_mon = int(dist_date[-2:])
                last_mon = cur_mon - 1
                cur_yr = int(dist_date[0:2])
                last_mon = str(cur_yr) + str(last_mon)
                 
        return last_mon
    
###############################################################################
# Prompt console for usper input. Follow print func below                      
###############################################################################
    def user_input():
        # Asking user for month and year input
        # Retun the date as a 4-digit output as yymm
        # Input can be reversed to ask for yymm
    
        while True:
            dist_date = input("Please enter the distrituion month and year, (example 0117 for January 2017): ")
            try:
                if int(dist_date[0:2]) >= 1 and int(dist_date[0:2]) <= 12 and len(dist_date) == 4:
                    month = int(dist_date[0:2])
                    year = int(dist_date[-2:])
                    if month < 10:
                        month = "0{}".format(str(month))
                    else:
                        month = str(month)
                        
                    dist_date = "{}{}".format(str(year), str(month))
                    break
                else: continue
            except: pass
    
        # return dist_date as a string like 1801 for Jan. 2018
        return dist_date
    
    
###############################################################################
# If variable empty return true else false                                     
###############################################################################
    def is_empty(any_structure):
        # empty structure is False by default
        if any_structure: return False
        else: return True
        
        
###############################################################################
# return a stop_row var to show where the loans stop at, including the incative
# loans            
###############################################################################        
    def find_stop_row(empty_row_var, row, ws, ws_col, hist_row, deal, dist_date):
        is_empty = Miscellaneous.is_empty
        empty_row = []
        empty_row = empty_row_var
        # Checking if the total beg balnce matches with hist row's first value
        tot_beg_bal = 0.0
        
        # If it encounters multiple empty_row
        # or there is no empty rows at all
        # decides to select where to stop in order to produce the right dat file
        # including zero balance/inactive loans
        # It does not delete/manipulate the data in remit files, it just stops calculating at stop row
        # Additional features can be added in
    
        # If there is nothing in the empty row, the row before hist_job_row should be empty
        if is_empty(empty_row) == True and '70000' in str(ws.loc[row, ws_col[0]]): stop_row = str(int(row) - 1)
    
        # if threre is only one empty row
        elif len(empty_row) == 1 and empty_row[0] + 1 == int(row): stop_row = empty_row[0]
    
        # if there are only two empty rows, make sure empty_row[1] include all the inactive loans
        # if there are no beg bals in those inactive loans, use empty_row[1] as the stop row
        # other wise use empty_row[0]
        elif len(empty_row) == 2:
            range3 = np.arange(len(empty_row)-1, -1, -1)
            for i in range3:
                tot_beg_bal = ws.loc[:empty_row[i], ws_col[6]].sum(skipna=True)
                tot_end_bal = ws.loc[:empty_row[i], ws_col[7]].sum(skipna=True)
                # Check if all the loans add up to beg_bal and end_bal
                if tot_beg_bal == hist_row[0] and tot_end_bal == hist_row[1]: return int(empty_row[i])
                elif (tot_beg_bal - hist_row[0] < 0.001) and (tot_end_bal - hist_row[1] < 0.001): return int(empty_row[i])
                else: stop_row = None
    
        elif len(empty_row) == 3 and empty_row[-2] == int(row) - 2 and empty_row[-1] == int(row) - 1:
            # If the third empty row is second empty row are above the loan count row
            # use the second empty_row
            empty_row.pop()
            range5 = np.arange(len(empty_row)-1, -1, -1)
            for i in range5:
                tot_beg_bal = ws.loc[:empty_row[i], ws_col[6]].sum(skipna=True)

                # Check if all the loans add up to beg_bal
                if tot_beg_bal == hist_row[0]: return int(empty_row[i])
                elif (tot_beg_bal - hist_row[0] < 0.001): return int(empty_row[i])
                else: stop_row = None
    
        # two consecutive empty rows in empty_row 0 and 1 use emtpy_row[0]
        elif len(empty_row) == 3 and int(empty_row[0]) == int(empty_row[1]) - 1:
            empty_row.pop()
            range6 = np.arange(len(empty_row)-1, -1, -1)
            for i in range6:
                tot_beg_bal = ws.loc[:empty_row[i], ws_col[6]].sum(skipna=True)

                # Check if all the loans add up to beg_bal
                if tot_beg_bal == hist_row[0]: return int(empty_row[i])
                elif (tot_beg_bal - hist_row[0] < 0.001): return int(empty_row[i])
                else: stop_row = None
             
        # if last empty_row is right above the loan count row and last two empty rows are consecutive
        elif len(empty_row) == 3 and int(empty_row[-1]) + 1 == int(row) and \
            int(empty_row[-2]) + 1 == int(empty_row[-1]):
            empty_row.pop()
            range7 = np.arange(len(empty_row)-1, -1, -1)
            for i in range7:
                tot_beg_bal = ws.loc[:empty_row[i], ws_col[6]].sum(skipna=True)
    
                # Check if all the loans add up to beg_bal
                if tot_beg_bal == hist_row[0]: return int(empty_row[i])
                elif (tot_beg_bal - hist_row[0] < 0.001): return int(empty_row[i])
                else: stop_row = None
               
        # If it is just regular 3 blocks of loans
        elif len(empty_row) == 3:
            range7 = np.arange(len(empty_row)-1, -1, -1)
            for i in range7:
                tot_beg_bal = ws.loc[:empty_row[i], ws_col[6]].sum(skipna=True)
    
                # Check if all the loans add up to beg_bal
                if tot_beg_bal == hist_row[0]: return int(empty_row[i])
                elif (tot_beg_bal - hist_row[0] < 0.001): return int(empty_row[i])
                else: stop_row = None
                        
        # Two consective empty rows right above the loan count row
        elif len(empty_row) == 4 and empty_row[-2] == int(row) - 2:
            empty_row.pop()
            range5 = np.arange(len(empty_row)-1, -1, -1)
            for i in range5:
                tot_beg_bal = ws.loc[:empty_row[i], ws_col[6]].sum(skipna=True)
        
                # Check if all the loans add up to beg_bal including the inactive loans
                # Double check if the decimal does not match for some reason
                if tot_beg_bal == hist_row[0]: return int(empty_row[i])
                elif (tot_beg_bal - hist_row[0] < 0.001): return int(empty_row[i])
                else: stop_row = None
    
        # two consecutive empty rows in empty_row 0 and 1 use emtpy_row[0]
        elif len(empty_row) == 4 and int(empty_row[0]) == int(empty_row[1]) - 1:
            range6 = np.arange(len(empty_row)-1, -1, -1)
            for i in range6:
                tot_beg_bal = ws.loc[:empty_row[i], ws_col[6]].sum(skipna=True)

                # Check if all the loans add up to beg_bal
                if tot_beg_bal == hist_row[0]: return int(empty_row[i])
                elif (tot_beg_bal - hist_row[0] < 0.001): return int(empty_row[i])
                else: stop_row = None
                
        elif len(empty_row) == 4 and int(empty_row[-1]) + 1 == int(row):
            range7 = np.arange(len(empty_row)-1, -1, -1)
            for i in range7:
                tot_beg_bal = ws.loc[:empty_row[i], ws_col[6]].sum(skipna=True)
    
                # Check if all the loans add up to beg_bal
                if tot_beg_bal == hist_row[0]: return int(empty_row[i])
                elif (tot_beg_bal - hist_row[0] < 0.001): return int(empty_row[i])
                else: stop_row = None
        
        elif len(empty_row) == 4 and int(empty_row[-1]) == int(empty_row[-2]) + 1:
            range8 = np.arange(len(empty_row)-1, -1, -1)
            for i in range8:
                tot_beg_bal = ws.loc[:empty_row[i], ws_col[6]].sum(skipna=True)
    
                # Check if all the loans add up to beg_bal
                if tot_beg_bal == hist_row[0]: return int(empty_row[i])
                elif (tot_beg_bal - hist_row[0] < 0.001): return int(empty_row[i])
                else: stop_row = None
        
        else:
            print('Check out {} {} remit file!'.format(deal, dist_date))
            print('You might want to delete some extra empty rows.')
            return
        
        # check again with regular payment column and kick out warning message if there is inconsistency
        regular_pmt_amt = ws.loc[:stop_row, ws_col[8]].sum(skipna=True)
        if regular_pmt_amt == hist_row[2]:
            pass
        else:
            print("***************WARNING***************")
            print("Dat file might have included uneccessary loans!!!")
            print("Check out the remit file and/or dat file for this deal!!")
            print("***************WARNING***************")
    
        return stop_row