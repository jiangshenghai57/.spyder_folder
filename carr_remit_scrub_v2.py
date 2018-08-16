# -*- coding: utf-8 -*-
"""
Created on Tue May  1 12:38:25 2018

@author: Shenghai
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 14:41:28 2018

@author: Shenghai
"""

#########################################################################################################
# This py script will scrub the monthly remit files for all CMS deals                                   #
# It will produce dat file and calculate the total net interest in the remit_scrub file
# User will only open up the remit file and copy and paste the row into the hist-job and other adj. if  #
# neccessary        
# Old method with load_workbook function
#########################################################################################################
# Script has been modified and with more source dependent modules to make the __main__ script look neater

import sys
import os
from shutil import copyfile
#import xlwings as xw
#from openpyxl import load_workbook
import numpy as np
import pandas as pd
import math
from create_mod import create_adj
from create_mod import create_dat
from create_mod import create_mod2
#from create_mod import create_mod
from misc_class_module import Miscellaneous
is_empty = Miscellaneous.is_empty
find_stop_row = Miscellaneous.find_stop_row
user_input = Miscellaneous.user_input

global dist_date

###############################################################################

# Dictionary of my carrington deals (Brian's deals)
# So the for loop can go through each deal's remit files
# additional value associated with key
my_deals = {
            # My deals
#            '2014-03': ('D:/deals/Carrington/SMAC/2014-03/', 'SMLT1403', 'A' , 'remit_check_3'),
#            '2014-05': ('D:/deals/Carrington/SMAC/2014-05/', 'SMLT1405', 'A' , 'remit_check_3'),
#            '2015-01': ('D:/deals/Carrington/SMAC/2015-01/', 'SMLT1501', 'A' , 'remit_check_3'),
#            '2015-08': ('D:/deals/Carrington/SMAC/2015-08/', 'SMLT1508', 'PO', 'remit_check_1'),
#            '2015-09': ('D:/deals/Carrington/SMAC/2015-09/', 'SMLT1509', 'PO', 'remit_check_1'),
#            '2016-01': ('D:/deals/Carrington/SMAC/2016-01/', 'SMLT1601', 'PO', 'remit_check_4'),
#            '2016-04': ('D:/deals/Carrington/SMAC/2016-04/', 'SMLT1604', 'PO', 'remit_check_1'),
#            '2016-21': ('D:/deals/Carrington/SMAC/2016-21/', 'SMLT1621', 'A' , 'remit_check_4'),
#            '2016-23': ('D:/deals/Carrington/SMAC/2016-23/', 'SMLT1623', 'A' , 'remit_check_3'),
#            '2016-31': ('D:/deals/Carrington/SMAC/2016-31/', 'SMLT1631', 'A' , 'remit_check_1'),
#            '2016-32': ('D:/deals/Carrington/SMAC/2016-32/', 'SMLT1632', 'A' , 'remit_check_1'),
           
            # Brian's deals
#            '2013-20': ('D:/deals/Carrington/SMAC/2013-20/', 'SMLT1320', 'A' , 'remit_check_2'),
#            '2013-21': ('D:/deals/Carrington/SMAC/2013-21/', 'SMLT1321', 'A' , 'remit_check_2'),
#            '2014-01': ('D:/deals/Carrington/SMAC/2014-01/', 'SMLT1401', 'A' , 'remit_check_2'),
#            '2014-04': ('D:/deals/Carrington/SMAC/2014-04/', 'SMLT1404', 'A' , 'remit_check_2'),
#            '2015-03': ('D:/deals/Carrington/SMAC/2015-03/', 'SMLT1503', 'PO', 'remit_check_2'),
#            '2015-04': ('D:/deals/Carrington/SMAC/2015-04/', 'SMLT1504', 'PO', 'remit_check_2'),
#            '2015-05': ('D:/deals/Carrington/SMAC/2015-05/', 'SMLT1505', 'PO', 'remit_check_2'),
#            '2015-07': ('D:/deals/Carrington/SMAC/2015-07/', 'SMLT1507', 'PO', 'remit_check_2'),
#            '2016-05': ('D:/deals/Carrington/SMAC/2016-05/', 'SMLT1605', 'PO', 'remit_check_2'),
#            '2016-06': ('D:/deals/Carrington/SMAC/2016-06/', 'SMLT1606', 'PO', 'remit_check_2'),
#            '2016-07': ('D:/deals/Carrington/SMAC/2016-07/', 'SMLT1607', 'PO', 'remit_check_2'),
#            '2016-08': ('D:/deals/Carrington/SMAC/2016-08/', 'SMLT1608', 'PO', 'remit_check_2'),
#            '2016-09': ('D:/deals/Carrington/SMAC/2016-09/', 'SMLT1609', 'PO', 'remit_check_2'),
#            '2016-10': ('D:/deals/Carrington/SMAC/2016-10/', 'SMLT1610', 'PO', 'remit_check_2'),
#            '2016-11': ('D:/deals/Carrington/SMAC/2016-11/', 'SMLT1611', 'PO', 'remit_check_2'),
#            '2016-12': ('D:/deals/Carrington/SMAC/2016-12/', 'SMLT1612', 'PO', 'remit_check_2'),
#            '2017-01': ('D:/deals/Carrington/SMAC/2017-01/', 'SMLT1701', 'PO', 'remit_check_2'),
#            '2017-02': ('D:/deals/Carrington/SMAC/2017-02/', 'SMLT1702', 'PO', 'remit_check_2'),
#            '2017-03': ('D:/deals/Carrington/SMAC/2017-03/', 'SMLT1703', 'PO', 'remit_check_2'),
#            '2017-04': ('D:/deals/Carrington/SMAC/2017-04/', 'SMLT1704', 'PO', 'remit_check_2'),
            '2017-05': ('D:/deals/Carrington/SMAC/2017-05/', 'SMLT1705', 'PO', 'remit_check_2'),
#            '2017-06': ('D:/deals/Carrington/SMAC/2017-06/', 'SMLT1706', 'PO', 'remit_check_2'),
#            '2017-09': ('D:/deals/Carrington/SMAC/2017-09/', 'SMLT1709', 'PO', 'remit_check_2'),
#            '2017-21': ('D:/deals/Carrington/SMAC/2017-21/', 'SMLT1721', 'A' , 'remit_check_2'),
#            '2017-31': ('D:/deals/Carrington/SMAC/2017-31/', 'UMLT1731', 'A' , 'remit_check_2'),
#            '2017-32': ('D:/deals/Carrington/SMAC/2017-32/', 'UMLT1732', 'A' , 'remit_check_2'),
#            '2017-33': ('D:/deals/Carrington/SMAC/2017-33/', 'UMLT1733', 'A' , 'remit_check_2'),
#            '2017-34': ('D:/deals/Carrington/SMAC/2017-34/', 'UMLT1734', 'A' , 'remit_check_2'),
#            '2018-01': ('D:/deals/Carrington/SMAC/2018-01/', 'SMLT1801', 'PO', 'remit_check_2'),
#            '2018-31': ('D:/deals/Carrington/SMAC/2018-31/', 'UMAC1831', 'A' , 'remit_check_2'),
#            '2018-32': ('D:/deals/Carrington/SMAC/2018-32/', 'UMAC1832', 'A' , 'remit_check_2'),
#            '2018-33': ('D:/deals/Carrington/SMAC/2018-33/', 'UMAC1833', 'A' , 'remit_check_2'),
#            '2018-34': ('D:/deals/Carrington/SMAC/2018-34/', 'UMAC1834', 'A' , 'remit_check_2'),
            }

#########################################################################################################
# Scrubbing the remit file                                                                              #
#########################################################################################################
#@profile
def scrub_carr(deal):
    # deal key only such as '2017-34'
    # Outter lvl exception handling if one deal does not go well,
    # it will go to the next deal
    try:
        # First value reference to the deal key
        # path is the deal path
        # current monthly remit if there is more than a couple of files in the dir,
        # make user choose which file to use
        # To see how many files is in the directory
        path = my_deals[deal][0]
        stmts_path = 'D:/deals/Carrington/aggdata/stmts/{}/'.format(deal)
        agg_remit_path = 'D:/deals/Carrington/aggdata/remit/{}/{}/'.format(deal, dist_date)
        aggdata_path = "D:/deals/remictax/aggdata/" # for prototype eticms only
        cur_mon_remit = agg_remit_path
        remit_files = os.listdir(cur_mon_remit)
    
        # Assign the correct remit file to manipulate for the deal
        # If there is no remit in the remit/dist_date/ folder continue to the next deal
        # This condition should be the most common one after just copied over the remit files from Tom's share
        # If rerun, scrub will be overwritten
        # If there is more than two files and other than remit and remit scrub, then ask user to choose
        if not os.path.exists(cur_mon_remit):
            print('Unfortunately this {} directory does not exist.'.format(cur_mon_remit))
            print("Make sure the remit file path name is correct.")
            return  
        elif len(remit_files) == 0:
            print("There is no file in {}".format(agg_remit_path))
            print("Going to the next deal")
            print('')
            return     
        
        elif (len(remit_files) == 1) and (dist_date[0:2] in remit_files[0]) and (".xlsx" in remit_files[0]):
            cur_mon_remit = "{}/{}".format(cur_mon_remit, remit_files[0])    
        elif len(remit_files) == 2 and "_scrub" not in remit_files[0] and '_scrub' in remit_files[1]:
            cur_mon_remit = "{}/{}".format(cur_mon_remit, remit_files[0])
        elif len(remit_files) == 3:
            for file in remit_files:
                if "_scrub" not in file and ".csv" not in file:
                    cur_mon_remit = "{}/{}".format(cur_mon_remit, file)
        else:
            for file in remit_files: print("{}. {}".format(str(remit_files.index(file)), file))
            print("Which file would you like to be your {} monthly remit file ".format(dist_date))
            while True:
                file_num = input('Please Choose a File number: ')
                try:
                    if int(file_num) < 0 and int(file_num) >= len(remit_files): pass
                    else:
                        cur_mon_remit = '{}/{}'.format(cur_mon_remit,remit_files[int(file_num)])
                        print("This file '{}' is going to be your {} remit file".format(remit_files[int(file_num)], dist_date))
                        print('Processing...')
                        break
                except: break
 
        # Copy the current month file and rename, and keep the original remit
        # Most likely it will never hit this condition. All remit files are in the current excel format xlsx
        if '.xlsx' in cur_mon_remit[-5:]: 
            remit_scrub = list(cur_mon_remit)
            remit_scrub = ''.join(remit_scrub[0: (len(remit_scrub) - 5)]) + '_scrub.xlsx'
            copyfile(cur_mon_remit, remit_scrub)
        elif '.xls' in cur_mon_remit[-4:]:
            print('Seems like the program cannot process the old excel format. Save as xlsx and retry.')
            return
        else:
            print('File cannot be found!!!')
            print('')
            return
        
        # Find out the remit files worksheet names
        # load_workbook will take a bit of time, since it's processing the entire remit file
        # pandas' read_excel function works faster, older version has the load_workbook function
        ws = pd.ExcelFile(remit_scrub)
        ws_sht_nm = ws.sheet_names
        remit_rprt = [nm for nm in ws_sht_nm if "remittance report" in nm.lower()]
        mod_nm = [nm for nm in ws_sht_nm if "modification" in nm.lower()]
        ws = pd.read_excel(remit_scrub, sheetname = remit_rprt[0])
        ws_col = list(ws.columns)
    
        # Additional checking
        if ws.empty: 
            print('Not sure which worksheet you want to look at.')
            print('You might want to check out the remit file or change the Worksheet\'s name to Remittance Report.')
            print('Going to the next deal.')
            return

        # reading the modification tab
        mod = pd.read_excel(remit_scrub, sheetname = mod_nm[0])
    
        # If mod tab/worksheet is empty not action
        # else use the create_mod function to create Mod CLD file
        # Need more thoughts about how to do this and get the correct calaculations
        # (months count, balloon term, forbear amount)
        if mod.empty: print("There is No mod for {} ".format(deal))
        else: 
            print("There is/are {} modification(s)".format(len(mod)))
            create_mod2(deal, agg_remit_path, dist_date, mod, my_deals[deal][1], ws)
#            create_mod(path, dist_date, mod, ws)
    
        # Searching for loan count row and find the hist job row(hist_row)
        """
        if KeyError comes up, then "Loan count" string is missing
        """
        for i in np.arange(1, 100000):
            if "loan count" in str(ws.loc[i, ws_col[0]]).lower():
                row = i
                break
            else: row = None
    
        # Skip the remit file, process the next one
        if is_empty(row) == True: 
            print('Cannot find loan count string or loan count row')
            print('Check out the remit file for deal {}'.format(deal)), print('')
            return
    
        # Detecting more than one empty row and put them into a list
        range1 = np.arange(0, int(row))
        empty_row = [i for i in range1 if math.isnan(ws.loc[i, ws_col[0]])]
    
        # First checker to ensure the CMS remit file format is correct
        # Beginning Balance should be in the G column, otherwise it would go to the next deal
        if ("beginning" not in str(ws_col[6]).lower()) or ('balance' not in str(ws_col[6]).lower()):
            print('Seems like the file format has changed for {} distribution file.'.format(dist_date))
            print('You might want to check it out.'), print('Going to the next deal.')
            return
    
        # Hist job row. Will be used for checking first, then changed to plus calc int and adjust prin write, etc.
        # from the beginning balance col to FMV Class B col
        hist_row = list(ws.iloc[row, 6:33])
    
        stop_row = find_stop_row(empty_row, row, ws, ws_col, hist_row, deal, dist_date)
        
        # check if AG is still fmv column
        # Additinal checker for CMS format
        if "fmv" in (ws_col[32]).lower(): 
            pass
        else: 
            print('Format has changed!!!')
            print('Check the new FMV column in {}'.format(remit_scrub))
            return
    
        # if there is a fmv, then erase def prin, prin write-off, new formula in hist_row
        # Sum up the transferred balance and beg_def_bal
        # Assign new formula into the hist row
        # This can be changed into for loops to input hard numbers onto the hist_row
        def_prin_w_off = 0.0
        prin_w_off = 0.0
        trans_bal = 0.0
        def_trans_bal = 0.0
        trans_bal_ac = 0.0
        
        # if there is fmv then calculate trans_bal, def_prin_w_off and other values
        loan_range = np.arange(0, int(stop_row))

        for num in loan_range:
            # if fmv column is not empty, add up the new Q & R columns
            if ws.loc[num, ws_col[32]] > 0:
                trans_bal += ws.loc[num, ws_col[6]]
                def_trans_bal += ws.loc[num, ws_col[28]]
    
            # if def prin w/off not empty and fmv > 0, zero out the cell
            if not math.isnan(ws.loc[num, ws_col[16]]) and ws.loc[num, ws_col[32]] > 0: ws.loc[num, ws_col[16]] = 0.0
    
            # if prin w/off not empty and fmv > 0, zero out the cell
            if not math.isnan(ws.loc[num, ws_col[17]]) and ws.loc[num, ws_col[32]] > 0: ws.loc[num, ws_col[17]] = 0.0
    
        # summing up the new q and r columns, deferred prin wirte-off and prin write-off
        def_prin_w_off = ws.loc[:stop_row, ws_col[16]].sum(skipna=True)
        prin_w_off = ws.loc[:stop_row, ws_col[17]].sum(skipna=True)
        trans_bal_ac = trans_bal + def_trans_bal
        
        # Create net calc int for each loan
        # Repalce total_upb cell with total net interest
        total_net_int = 0
        for num in loan_range:
            if ws.loc[num, ws_col[6]] > 0:
                total_net_int += ws.loc[num, ws_col[6]] * ws.loc[num, ws_col[9]] / 1200.0 - ws.loc[num, ws_col[11]] 
    
        #Do a loan by loan balance check.  Writes a message with any loans that have an error. Must be done BEFORE adjustments to FMV loans.
        # Beg_bal + beg_def_prin - prin_payment - prin_writeoff - end_def_prin - end_bal - fmv
        for num in loan_range:
            bal_check = ws.loc[num, ws_col[6]] + ws.loc[num, ws_col[28]] - ws.loc[num, ws_col[13]] \
                        - ws.loc[num, ws_col[17]] - ws.loc[num, ws_col[29]] - ws.loc[num, ws_col[7]] - ws.loc[num, ws_col[32]]
            if abs(bal_check) > 0.05:
                print('Loan level balance check fail for Loan # {0} by {1} check it out!'.format(ws.loc[num, ws_col[0]], bal_check))
                input('Press Enter to continue >>>')
            else: 
                pass
    
        # if there is fmv loans, column q and r will get modified
        # append net int and transferred bal to hist_row2
        # append the full name into the hist_row2
        hist_row2 = hist_row
        hist_row2[10] = def_prin_w_off
        hist_row2[11] = prin_w_off
        hist_row2.append(total_net_int)
    
        # Check hist_row if they are consistent with the sum of all loans' numbers
        beg_def_prin = ws.loc[:stop_row, ws_col[28]].sum(skipna=True)
        end_def_prin = ws.loc[:stop_row, ws_col[29]].sum(skipna=True)
        
        if beg_def_prin - hist_row2[22] > 0.05:
            print('There is inconsistency between hist_row Beg_Def_Prin and remit_file Beg_Def_Prin amount')
            print('Script is going to change the number in csv')
            print('Watch out for other inconsitency in the remit file')
            hist_row2[22] = beg_def_prin
        
        if end_def_prin - hist_row2[23] > 0.05:
            print('There is inconsistency between hist_row End_Def_Prin and Loan Total End_Def_Prin amount')
            print('Script is going to change the number in csv.')
            print('Watch out for other inconsitency in the remit file!')
            hist_row2[23] = end_def_prin
        
        # Create the dat file in the deal remit folder
        # 7-columns carrington dat
        # carrington #, beg_bal, end_bal, prin, gross int, prin w/r/loss, end def prin
        # Search for other dat and/or inp file to create deal name and date extention
        c_file = os.listdir(path)
        for file in c_file:
            if '.inp' in file:
                deal_name = str(file[0:5])
                break
            else:
                deal_name = None
    
        if is_empty(deal_name) == True: 
            print("Cannot find deal name")
            print('')
            return

        # Create deal 7-column dat file into deal directory
        create_dat(deal, deal_name, path, aggdata_path, dist_date, loan_range, ws)    

#        '''
        ws_col = list(ws_col[6:33])
        ws_col.append("tot_net_int")    
        hist_row2.insert(0, my_deals[deal][1])
    
        # Searching for remittance amount and add up all the fees (if any) in the ws DataFrame
        # it is usually under the ws.loc[:, "Next_Due_Date"] column
        # numbers are usually under the Beginning_Balance column
        for i in np.arange(1, 100000):
            if "hamp funds" in str(ws.loc[i, "Next_Due_Date"]).lower():
                fee_row = i + 1
                break
            else: fee_row = None
    
        for i in np.arange(1, 100000):
            if "remittance total" in str(ws.loc[i, "Next_Due_Date"]).lower() or \
            "total remittance" in str(ws.loc[i, "Next_Due_Date"]).lower():
                remit_stop_row = i
                break
            else: remit_stop_row = None
    
        if not fee_row: 
            print("Cannot find fees!!!")
            print("Going to the next deal.")
            print("")
            return
    
        if not remit_stop_row: 
            print("Cannot find total remittance amount!!!")
            print("Going to the next deal.")
            return
    
        loop_range = np.arange(fee_row, remit_stop_row)
    
        advan_fee = 0
    
        for i in loop_range:
            if "remittance total" not in str(ws.loc[i, "Next_Due_Date"]) or \
            "total remittance" not in str(ws.loc[i, "Next_Due_Date"]):
                if math.isnan(ws.loc[i, "Beginning_Balance"]): continue
                else: advan_fee += ws.loc[i, "Beginning_Balance"]
    
        opt_trf = ws.loc[remit_stop_row, "Ending_Balance"]
        opt_paf = ws.loc[remit_stop_row, "Current_Regular_Pmt_Amt"]
        
        if ws.loc[remit_stop_row, "Beginning_Balance"] > 0.0: carr_tot_remit = ws.loc[remit_stop_row, "Beginning_Balance"]
        elif ws.loc[remit_stop_row, "Beginning_Balance"] < 0.0: 
            carr_tot_remit = ws.loc[remit_stop_row, "Beginning_Balance"]
            advan_fee = -carr_tot_remit + advan_fee
            carr_tot_remit = 0.0
        elif ws.loc[remit_stop_row, "Beginning_Balance"] == 0.0: carr_tot_remit = 0.0
        elif ws.loc[remit_stop_row, "Beginning_Balance"] < 0.0 and deal == "2014-05":
            carr_tot_remit = ws.loc[remit_stop_row, "Beginning_Balance"]
            advan_fee += -ws.loc[remit_stop_row, "Beginning_Balance"]
            carr_tot_remit = 0.0
        
        # add advance fee and other numbers from the remit
        hist_row2.append(advan_fee), hist_row2.append(carr_tot_remit)
        hist_row2.append(trans_bal), hist_row2.append(trans_bal_ac)
        # Default to only one group
        # this could be added to my_deals dictionary
        hist_row.append(1)
        hist_row.append(opt_trf)
        hist_row.append(opt_paf)
    
        hist_row2 = [hist_row2]
    
        if os.path.exists("d:/deals/carrington/aggdata/{}".format(dist_date)): pass
        else: os.makedirs("d:/deals/carrington/aggdata/{}".format(dist_date))
    
        df = pd.DataFrame(hist_row2)
  
        df.to_csv("d:/deals/carrington/aggdata/{}/{}_{}.csv".format(dist_date, deal, dist_date), \
                  float_format='%.2f', sep=",", header=False, index=False)
        print("Deal {} agg file created.".format(deal))
    
        # for cash check and other checks
        adj_df = create_adj(deal, stmts_path, dist_date, deal_name, my_deals[deal][1])
        
        # Warning message if there is a difference in transferred balnces
        check_trans_bal_1 = df.iloc[0, 31]
        check_trans_bal_2 = df.iloc[0, 32]
        if abs(check_trans_bal_1 - check_trans_bal_2) > 0.05:
            print("************WARNING************")
            print("Transferred balance difference {0:.2f}".format(check_trans_bal_1 - check_trans_bal_2))
            print("************WARNING************")

        # first round of cash checks before ETICMS application
        # Some deals are set up completely different
        beg_bal = df.iloc[0, 1]
        end_bal = df.iloc[0, 2]
        sched_prin = df.iloc[0, 8]
        unsched_prin = df.iloc[0, 27]
        gross_int = df.iloc[0, 5] + df.iloc[0, 15] + df.iloc[0, 16] + \
                    df.iloc[0, 17] + df.iloc[0, 18] + df.iloc[0, 26] + df.iloc[0, 29]
        servicing = adj_df.iloc[0, 10]
        prin_writeoff = df.iloc[0, 12]
#        trans_bal_1 = df.iloc[0, 31]
        trans_bal_2 = df.iloc[0 ,32]
        fmv = df.iloc[0, 27]
        beg_def_bal = df.iloc[0, 23]
        end_def_bal = df.iloc[0, 24]
        carr_remit = df.iloc[0, 30]
        paf_trustee = adj_df.iloc[0, 9]
        class_a_tot_remit = adj_df.iloc[0, 5]
        class_po_tot_remit = adj_df.iloc[0, 8]
        
        gross_cash = gross_int + sched_prin + unsched_prin
        
        # balance, principal, loss, fmv check, should be all the same acrross all carrington deals
        check_1 = end_bal - (beg_bal - sched_prin - unsched_prin - prin_writeoff - trans_bal_2 + \
                    fmv + beg_def_bal - end_def_bal)
            
        
        
        if abs(check_1) > 0.05:
            print("Check 1 is off by {:2f}".format(abs(check_1)))
        
        if class_po_tot_remit == None and "remit_check_1" in my_deals[deal]:
            remit_check_1 = carr_remit - servicing - paf_trustee - class_a_tot_remit
            if abs(remit_check_1) > 0.05:
                print("Remit check 1 is off by {:2f}".format(abs(remit_check_1)))
                
        elif "remit_check_1" in my_deals[deal]:
            remit_check_1 = carr_remit - servicing - paf_trustee - class_a_tot_remit - class_po_tot_remit
            if abs(remit_check_1) > 0.05:
                print("Remit check 1 is off by {:2f}".format(abs(remit_check_1)))
                
        elif "remit_check_2" in my_deals[deal]:
            remit_check_2 = gross_cash - fmv - carr_remit
            if abs(remit_check_2) > 0.05:
                print("Remit check 2 is off by {:2f}".format(abs(remit_check_2)))
                
        elif class_po_tot_remit == None and "remit_check_3" in my_deals[deal]:
            remit_check_3 = gross_cash - fmv - paf_trustee - servicing - class_a_tot_remit
            if abs(remit_check_3) > 0.05:
                print("Remit check 3 is off by {:2f}".format(abs(remit_check_3)))
                
        elif "remit_check_3" in my_deals[deal]:
            remit_check_3 = gross_cash - fmv - paf_trustee - servicing - class_a_tot_remit - class_po_tot_remit
            if abs(remit_check_3) > 0.05:
                print("Remit check 3 is off by {:2f}".format(abs(remit_check_3)))
         
        elif class_po_tot_remit == None and "remit_check_4" in my_deals[deal]:
            remit_check_4 = gross_cash - fmv - carr_remit
            if abs(remit_check_4) > 0.05:
                print("Remit check 4 is off by {:2f}".format(abs(remit_check_4)))
                
        elif "remit_check_4" in my_deals[deal]:
            remit_check_4 = gross_cash - fmv - carr_remit
            if abs(remit_check_4) > 0.05:
                print("Remit check 4 is off by {:2f}".format(abs(remit_check_4)))
                
        else:
            print("You're shit out of luck!!!")
        
        
        print("")
#        '''
    
    except:
        print("Tried to process " + deal + " deal, but you might want to check it out.")
        input("Please press Enter to continue ...")
        print('')
        pass


if __name__ == '__main__':
    # Asking user to input a 4-digit year and month (e.g. 1812 for 2018 December)
    dist_date = user_input()
    # Looping through each deal(key)
    for deal in my_deals.keys():
        scrub_carr(deal)  
    input('Please press Enter to exit...')
    sys.exit()
