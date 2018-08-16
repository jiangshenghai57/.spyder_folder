# -*- coding: utf-8 -*-
"""
Created on Mon May  7 11:15:43 2018

@author: Shenghai
"""

import dbf
from shutil import copyfile
from numpy import nper
import os
import numpy as np
import xlrd
import math
import pandas as pd
from datetime import datetime
from misc_class_module import Miscellaneous
is_empty = Miscellaneous.is_empty
last_mon = Miscellaneous.last_mon


### CONSTANTS ###
FIFTEEN = 15
ONE = 1
## CONTANTS ###


    
    
###############################################################################
# Argument should be len 4 string yymm
def next_pay(dist_date):
    if int(dist_date[-2:]) == 12:
        next_mon = 1 
        cur_yr = int(dist_date[0:2])
        next_yr = cur_yr + 1 + 2000
        next_mon = "{}0{}".format(str(next_yr), str(next_mon))
    else:
        if int(dist_date[-2:]) < 10:
            cur_mon = int(dist_date[-2:])
            next_mon = cur_mon + 1
            cur_yr = int(dist_date[0:2])  + 2000
            next_mon = "{}0{}".format(str(cur_yr), str(next_mon))
        else:
            cur_mon = int(dist_date[-2:])
            next_mon = cur_mon + 1
            cur_yr = int(dist_date[0:2]) + 2000
            next_mon = "{}{}".format(str(cur_yr), str(next_mon))
            
    return next_mon


###############################################################################
# This function produce Myymm.CLD file
def create_mod(path, dist_date, mod, ws):
#    try:
        table = dbf.Table("{}M{}000".format(path, dist_date), 'coll_type C(1)')
        table.open()
        table.add_fields("loan_id C(15)")
        table.add_fields("delay_flag C(1)")
        table.add_fields("next_pdate D")
        table.add_fields("c_term_1 N(4, 0)")
        table.add_fields("c_term_2 N(4, 0)")
        table.add_fields("c_rate_1 N(13, 11)") 
        table.add_fields("c_net_rt1 N(13, 11)")
        table.add_fields("c_net_rt2 N(13, 11)")
        table.add_fields("c_wac_rt N(13, 11)")
        table.add_fields("max_svgfee N(15, 11)")
        table.add_fields("c_bal N(11, 2)")
        table.add_fields("rein_dys_1 N(4, 0)")
        table.add_fields("rein_dys_2 N(4, 0)")
        table.add_fields("orig_trm N(4, 0)")
        table.add_fields("curr_trm_1 N(4, 0)")
        table.add_fields("curr_trm_2 N(4, 0)")
        table.add_fields("c_curr_bal N(11, 2)")
        table.add_fields("c_orig_bal N(11, 2)")
        table.add_fields("psa_speed N(13, 11)")
        table.add_fields("max_bv_pct N(13, 11)")
        table.add_fields("p_and_i N(8, 2)")
        table.add_fields("strip_flag C(1)")
        table.add_fields("istrip_pct N(13, 11)")
        table.add_fields("pstrip_pct N(13, 11)")
        table.add_fields("actual_bv N(13, 11)")
        table.add_fields("special N(13, 11)")
        table.add_fields("delay_mths N(4, 0)")
        table.add_fields("balln_term N(4, 0)")
        table.add_fields("spare_int1 N(4, 0)")
        table.add_fields("spare_int2 N(4, 0)")
        table.add_fields("spare_rt1 N(13, 11)")
        table.add_fields("spare_rt2 N(13, 11)")
        table.add_fields("fixvarloan C(1)")
        table.add_fields("net_chgflg C(1)")
        table.add_fields("net_mrgn_1 N(13, 11)")
        table.add_fields("net_mrgn_2 N(13, 11)")
        table.add_fields("max_net_1 N(13, 11)")
        table.add_fields("max_net_2 N(13, 11)")
        table.add_fields("arms_index N(10, 8)")
        table.add_fields("sprd_to_ix N(13, 11)")
        table.add_fields("perchg_amt N(13, 11)")
        table.add_fields("prdchg_flg C(1)")
        table.add_fields("pmtchg_cap N(10, 8)")
        table.add_fields("pmtchg_flg C(1)")
        table.add_fields("life_cap N(10, 8)")
        table.add_fields("life_floor N(10, 8)")
        table.add_fields("ms_to_int N(4, 0)")
        table.add_fields("ms_to_prin N(4, 0)")
        table.add_fields("m_btw_ichg N(4, 0)")
        table.add_fields("m_btw_pchg N(4, 0)")
        table.add_fields("grad_rate N(10, 8)")
        table.add_fields("num_grads N(4, 0)")
        table.add_fields("grad_imths N(4, 0)")
        table.add_fields("tpm_stdbps N(11, 9)")
        table.add_fields("tpm_ecnbps N(11, 9)")
        table.add_fields("tpm_pi_pct N(11, 9)")
        table.add_fields("tpm_smtchg N(4, 0)")
        table.add_fields("tpm_emtchg N(4, 0)")
        table.add_fields("tpm_mbtwcg N(4, 0)")
        table.add_fields("prefundprd N(4, 0)")
        table.add_fields("io_dlymths N(4, 0)")
        table.add_fields("clsg_delay N(4, 0)")
        table.add_fields("draw_rate N(11, 9)")
        table.add_fields("draw_term N(4, 0)")
        table.add_fields("creditlimt N(8, 2)")
        table.add_fields("orig_gross N(13, 11)")
        table.add_fields("pp_type N(4, 0)")
        table.add_fields("pp_term N(4, 0)")
        table.add_fields("bal_wtd N(10, 8)")
        table.add_fields("forbear N(10, 2)")
        table.add_fields("act_prin N(8, 2)")
        table.add_fields("act_int N(8, 2)")
        table.add_fields("act_loss N(8, 2)")
        table.add_fields("outs_gain N(8, 2)")
        table.add_fields("amort_gain N(8, 2)")
        table.add_fields("mod_gain N(8, 2)")
        table.add_fields("mod_date D")
        table.add_fields("prevmod_dt D")
        table.add_fields("retire_dt D")
        table.add_fields("price N(11, 2)")
        table.add_fields("borr_age N(8, 5)")
        table.add_fields("creditline N(8, 2)")
        table.add_fields("amt_sched C(1)")
        table.add_fields("strip_pct1 N(10, 8)")
        table.add_fields("strip_pct2 N(10, 8)")
        table.add_fields("strip_pct3 N(10, 8)")
        table.add_fields("strip_pct4 N(10, 8)")
        table.add_fields("forbear2 N(8, 2)")
    
        next_dist_date = next_pay(dist_date)
        
    #    print(nper(mod.loc[i, "Newrate"], mod.loc[i, "New PI"], -mod.loc[i, "upb"]) - 1)
        
        last_dist = last_mon(dist_date)
        ws = ws
        ws_col = list(ws.columns)
        ws = ws = ws.set_index(ws_col[0])
        ws_ind = list(ws.index)
             
        def diff_month(d1, d2):
            return (d1.year - d2.year) * 12 + d1.month - d2.month
                  
        for i in range(0, len(mod)):
            df = mod[['Loan Number', 'Modified UPB', 'Newrate', 'New PI']]
            
            # Checking if the mod tab balance, newrate and new pi match with the remit tab loan information, else do nothing
            # find the forbearance amount for the mod loans
            if mod.loc[i, 'Loan Number'] in list(ws_ind):
                forbear = ws.loc[mod.loc[i, 'Loan Number'], ws_col[29]]
            else:
                forbear = 0.0
                
            # if the loan number in mod tab is found in remit tab then compare balance, newrate, and new p&i
            if mod.loc[i, 'Loan Number'] in list(ws_ind):
                if mod.loc[i, 'Modified UPB'] == ws.loc[mod.loc[i, 'Loan Number'], ws_col[7]]:
                    pass
                else:
                    df.loc[i, 'Modified UPB'] = ws.loc[mod.loc[i, 'Loan Number'], ws_col[7]]
                    print('Found a mismatch balance in loan #{}!'.format(mod.loc[i, 'Loan Number']))
            
            if mod.loc[i, 'Loan Number'] in list(ws_ind):
                if mod.loc[i, 'Newrate'] == ws.loc[mod.loc[i, 'Loan Number'], ws_col[9]]:
                    pass
                else:
                    df.loc[i, 'Newrate'] = ws.loc[mod.loc[i, 'Loan Number'], ws_col[9]]
                    print('Found a mismatch intereste rate in loan #{}!'.format(mod.loc[i, 'Loan Number']))
        
            if mod.loc[i, 'Loan Number'] in list(ws_ind):
                if mod.loc[i, 'New PI'] == ws.loc[mod.loc[i, 'Loan Number'], ws_col[8]]:
                    pass
                else:
                    df.loc[i, 'New PI'] = ws.loc[mod.loc[i, 'Loan Number'], ws_col[8]]
                    print('Found a mismatch P&I in loan #{}!'.format(mod.loc[i, 'Loan Number']))
            
            if pd.isnull(mod.loc[i, 'Post Mod Ball Pmt Date']) == False:
                d1 = str(mod.loc[i, 'Post Mod Ball Pmt Date'])[0:10]
                d1 = datetime(int(d1[0:4]), int(d1[5:7]), int(d1[8:10]))                      
                d2 = last_dist
                d2 = datetime(2000 + int(d2[0:2]), int(d2[-2:]), 1)

            else:
                d1 = "2001/01/01"
                d1 = datetime(int(d1[0:4]), int(d1[5:7]), int(d1[8:10]))
                d2 = "2001/01/01"
                d2 = datetime(int(d2[0:4]), int(d2[5:7]), int(d2[8:10]))
            
            if mod.loc[i, "Bal Principal"] == 0.0:
                print("Skipping the loan with a 0.00 balance!!")
                continue
            
            if mod.loc[i, 'Loan Number'] in list(ws_ind):
                if mod.loc[i, 'Modified UPB'] == ws.loc[mod.loc[i, 'Loan Number'], ws_col[7]]:
                    pass
                else:
                    mod.loc[i, 'Modified UPB'] = ws.loc[mod.loc[i, 'Loan Number'], ws_col[7]]
                    print('Found a mismatch balance in loan #{} in the modification tab!'.format(mod.loc[i, 'Loan Number']))
                
            term = math.floor(nper(df.loc[i, "Newrate"] / 100.0 / 12.0, df.loc[i, "New PI"], -mod.loc[i, 'Modified UPB'], 0))    
                
            for datum in (
                    ("", 
                     str(mod.loc[i, "Loan Number"]),
                     "N", 
                     dbf.Date(int(next_dist_date[0:4]), int(next_dist_date[-2:]), ONE), 
                     term,
                     term,
                     mod.loc[i, "Newrate"] / 100,
                     mod.loc[i, "Newrate"] / 100 - 0.006, # 0.6% svcg_fee 
                     0,
                     mod.loc[i, "Newrate"] / 100.0,
                     0.006, # max_svgfee
                     mod.loc[i, "Modified UPB"],
                     0, 0,
                     term,
                     term,
                     term,
                     mod.loc[i, "Modified UPB"],
                     mod.loc[i, "Modified UPB"],
                     1.00000, 1.00000,
                     mod.loc[i, "New PI"],
                     "N",
                     0.0, 0.0, # INT STRIP % # PRIN STRIP %
                     0.0, 0.0, 
                     0, 
                     diff_month(d1, d2), # ballon term 
                     0, 0,
                     0.0, 0.0,
                     "M","B", 
                     0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
                     "B",
                     9.99,
                     "B",
                     0.0, 0.0,
                     998, 999, 999, 999,
                     0.0,
                     0, 0,
                     0.0, 0.0, 0.0,       
                     0, 0, 0, 0, 0, 0,
                     0.0,
                     0, 
                     0.0, 0.0,
                     0, 0,
                     0.0,
                     forbear, 
                     0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                     dbf.Date(int("20{}".format(dist_date[0:2])), int(dist_date[-2:]), ONE),
                     dbf.Date(),
                     dbf.Date(),
                     df.loc[i, "Modified UPB"] + forbear,
                     0.0, 0.0, "",
                     0.0, 0.0, 0.0, 0.0, 0.0
                     ),
                    ):
                table.append(datum)
            
    
        table.close()
        
        mod_file = "{}M{}000.dbf".format(path, dist_date)
        
        copyfile(mod_file, "{}.CLD".format(mod_file[0:len(mod_file) - 4]))
        
        os.remove(mod_file)
        
        print("MOD CLD created!")
        
        
#    except:
#        print('Exception happened in create_mod module create_mod function')


###############################################################################
# this function will read in the modification tab and grab the neccessary fields and kick out a csv mod file
# A substitute for create_mod function
def create_mod2(deal, agg_remit_path, dist_date, mod, deal_full_name, ws):
    try: 
        ws = ws
        ws_col = list(ws.columns)
        ws = ws.set_index(ws_col[0])
        ws_ind = list(ws.index)
        balloon = [] 
        forbear = []
        last_dist = last_mon(dist_date) 
        
        def diff_month(d1, d2): return (d1.year - d2.year) * 12 + d1.month - d2.month
        
        for i in range(0, len(mod)):
            if pd.isnull(mod.loc[i, 'Post Mod Ball Pmt Date']) == False:
                d1 = str(mod.loc[i, 'Post Mod Ball Pmt Date'])[0:10]
                d1 = datetime(int(d1[0:4]), int(d1[5:7]), int(d1[8:10]))                      
                d2 = last_dist
                d2 = datetime(2000 + int(d2[0:2]), int(d2[-2:]), 1)
                balloon.append(diff_month(d1, d2))
            else:
                balloon.append(0)
            
        if i in mod[['Modified UPB']] == 0: print('Modification with $0.00 balance in deal {}'.format(deal))
        
        df = mod[['Loan Number', 'Modified UPB', 'Newrate', 'New PI']]
        
        # Checking if the mod tab balance, newrate and new pi match with the remit tab loan information, else do nothing
        for i in range(0, len(df)):
            # find the forbearance amount for the mod loans
            if mod.loc[i, 'Loan Number'] in list(ws_ind):
                forbear.append(ws.loc[mod.loc[i, 'Loan Number'], ws_col[29]])
                          
            # if the loan number in mod tab is found in remit tab then compare balance, newrate, and new p&i
            if mod.loc[i, 'Loan Number'] in list(ws_ind):
                if mod.loc[i, 'Modified UPB'] == ws.loc[mod.loc[i, 'Loan Number'], ws_col[7]]:
                    pass
                else:
                    df.loc[i, 'Modified UPB'] = ws.loc[mod.loc[i, 'Loan Number'], ws_col[7]]
                    print('Found a mismatch balance in remit tab and mod tab, loan #{}!'.format(mod.loc[i, 'Loan Number']))
            
            if mod.loc[i, 'Loan Number'] in list(ws_ind):
                if mod.loc[i, 'Newrate'] == ws.loc[mod.loc[i, 'Loan Number'], ws_col[9]]:
                    pass
                else:
                    df.loc[i, 'Newrate'] = ws.loc[mod.loc[i, 'Loan Number'], ws_col[9]]
                    print('Found a mismatch intereste rate in remit tab and mod tab, loan #{}!'.format(mod.loc[i, 'Loan Number']))
        
            if mod.loc[i, 'Loan Number'] in list(ws_ind):
                if mod.loc[i, 'New PI'] == ws.loc[mod.loc[i, 'Loan Number'], ws_col[8]]:
                    pass
                else:
                    df.loc[i, 'New PI'] = ws.loc[mod.loc[i, 'Loan Number'], ws_col[8]]
                    print('Found a mismatch P&I in remit tab and mod tab, loan #{}!'.format(mod.loc[i, 'Loan Number']))
        
        df.loc[df.index, 'Forbearance Amount'] = pd.Series(forbear, index=df.index)
        df.loc[df.index, 'Ballon Term'] = pd.Series(balloon, index=df.index)
        
        full_name = []
        [i for i in range(0, len(mod)) if full_name.append(deal_full_name)]        
        mod_date = []
        [i for i in range(0, len(mod)) if mod_date.append("{}/01/20{}".format(last_dist[-2:], last_dist[0:2]))]    
        
        df.loc[df.index, 'Mod Date'] = pd.Series(mod_date, index=df.index)    
        df2 = pd.DataFrame(full_name, index=df.index)
        df = pd.concat([df2, df], axis=1)
        df.to_csv("d:/deals/carrington/aggdata/{}/mod_{}_{}.csv".format(dist_date, deal, dist_date), \
                  sep=",", header=False, index=False)
        
        print("Deal {} mod(s) file created.".format(deal))
        
    except (ValueError):
        print('Error handling happend in create_mod2 function in create_mod module!')
        print('Mod(s) csv did not create correctly')

            
        

###############################################################################    
def create_adj(deal, stmts_path, dist_date, deal_name, deal_full_name):
    try:
        # Grabbing fees and blocker cash for po deals only in the stmts + dist_date path
        stmts_path = "{}R20{}/".format(stmts_path,dist_date)
        
        # List the files and fine the right file with distribution/fee numbers
        wells_files = os.listdir(stmts_path)
        if len(wells_files) == 4:
            for file in wells_files:
                if str(deal_name[-1:]) + "_RMT" in file and ".xls" in file: fee_non_rt = "{}{}".format(stmts_path, file)   
                if "RT_RMT" in file and ".xls" in file: rt_rmt = "{}{}".format(stmts_path, file)                 
        elif len(wells_files) > 4: print("There are more than 4 files in the directory, you might want to check it out!!!")
        else: print("Something is funky about the wells files, you might want to check it out!!!")
        
        fee_wb = xlrd.open_workbook(fee_non_rt, formatting_info=True)
        fee_ws = fee_wb.sheet_by_index(0)    
        blocker_cash = 0.0
        
        # Find paying agent fee, trustee fee, blocker cash. For some deals we need Trigger
        # amount, trigger adjustment amount, and trigger threshold
        for i in np.arange(120, 150):
            if "class a" in str(fee_ws.cell(i, 7)).lower() and "paying agent fee" in str(fee_ws.cell(i, 7)).lower():
                paf = fee_ws.cell_value(i, 11)
                break
            else: paf = None              
            
        for i in np.arange(120, 150):
            if "class a" in str(fee_ws.cell(i, 7)).lower() and "trustee fee" in str(fee_ws.cell(i, 7)).lower():
                trt_fee = fee_ws.cell_value(i, 11)
                break
            else: trt_fee = None
                
        for i in np.arange(120, 150):
            if "class a service fee" in str(fee_ws.cell(i, 7)).lower() or \
            "class a servicing fee" in str(fee_ws.cell(i, 7)).lower() or \
            "servicing fee a" in str(fee_ws.cell(i,7)).lower():
                actual_svcg_fee = fee_ws.cell_value(i, 11)
                break
            else: actual_svcg_fee = None
                
        for i in np.arange(220, 270):
            if ("class b" in str(fee_ws.cell_value(i, 2)).lower() and \
            "available funds" in str(fee_ws.cell_value(i, 2)).lower()) or \
            ("class b" in str(fee_ws.cell_value(i, 2)).lower() and \
            "available distribution amount" in str(fee_ws.cell_value(i, 2)).lower()):
                blocker_cash += float((fee_ws.cell_value(i, 7)).replace(',', ''))
                break
            else: blocker_cash = 0.0
            
        for i in np.arange(220, 270):
            if "class b" in str(fee_ws.cell_value(i, 2)).lower() and \
            "success service fee paid" in str(fee_ws.cell_value(i, 2)).lower():
                suc_svcg_paid = float((fee_ws.cell_value(i, 7)).replace(',', ''))
                blocker_cash += suc_svcg_paid
                break
            else: suc_svcg_paid = None
        
        for i in np.arange(235, 255):
            if "periodic trigger amount" in str(fee_ws.cell_value(i, 2)).lower():
                prd_trig_amt = float((fee_ws.cell_value(i, 7)).replace(',', ''))
                break
            else: prd_trig_amt = None
        
        for i in np.arange(235, 255):
            if "trigger adjustment amount" in str(fee_ws.cell_value(i, 2)).lower() or \
            ("trigger threshold" in str(fee_ws.cell_value(i, 2)).lower() and \
             "adjustment" in str(fee_ws.cell_value(i, 2)).lower() and \
             "amount" in str(fee_ws.cell_value(i, 2)).lower()):
                trig_adj_amt = float((fee_ws.cell_value(i, 7)).replace(',', ''))
                break
            else: trig_adj_amt = None
                
        for i in np.arange(235, 255):
            if str(fee_ws.cell_value(i, 2)) == "Trigger Threshold":
                trig_thr= float((fee_ws.cell_value(i, 7)).replace(',', ''))
                break
            else: trig_thr = None
         
        rt_wb = xlrd.open_workbook(rt_rmt, formatting_info=True)    
        rt_ws = rt_wb.sheet_by_index(0)
        
        for row in np.arange(15, 25):
            if 'A' in str(rt_ws.cell_value(row, 0)):
                class_a_row = row
                break
            else: class_a_row = None  
                
        for row in np.arange(15, 25):
            if 'PO' in str(rt_ws.cell_value(row, 0)):
                class_po_row = row
                break
            else: class_po_row = None
        
    #        print(rt_ws.cell_value(14, 9))
    #        print(rt_ws.cell_value(15, 9))
    #        print(rt_ws.cell_value(16, 9))
    #        print(rt_ws.cell_value(12, 9))
        
        if is_empty(class_po_row) == True:
            for row in np.arange(class_a_row - 3, 20):
                for col in np.arange(6, 10):
                    if col == 9:
                        class_a_int_dist = rt_ws.cell_value(class_a_row, col - 3)
                        class_a_prin_dist = rt_ws.cell_value(class_a_row, col - 2)
                        end_cert_bal_a = rt_ws.cell_value(class_a_row, col)
                        tot_dist = rt_ws.cell_value(class_a_row, col + 1)
                        break
                    else:
                        class_a_int_dist = None
                        class_a_prin_dist = None
                        end_cert_bal_a = None
                        tot_dist = None     
                    
                if end_cert_bal_a >= 0 and tot_dist >= 0: break
                        
            end_cert_bal_po = None
            tot_dist_po = None
            class_po_int_dist = None
            class_po_prin_dist = None
            deal_type = 'A'
            
        else:
            for row in np.arange(class_a_row - 3, 18):
                for col in np.arange(6, 10):
                    if "Ending" in str(rt_ws.cell_value(row, col)):
                        end_cert_bal_a = rt_ws.cell_value(class_a_row, col)
                        end_cert_bal_po = rt_ws.cell_value(class_po_row, col)
                        class_a_int_dist = rt_ws.cell_value(class_a_row, col - 3)
                        class_a_prin_dist = rt_ws.cell_value(class_a_row, col - 2)
                        class_po_int_dist = rt_ws.cell_value(class_po_row, col - 3)
                        class_po_prin_dist = rt_ws.cell_value(class_po_row, col - 2)
                        tot_dist_po = rt_ws.cell_value(class_po_row, col + 1)
                        tot_dist = rt_ws.cell_value(class_a_row, col + 1)                    
                        break
                    else:
                        end_cert_bal_a = None
                        end_cert_bal_po = None
                        class_a_int_dist = None
                        class_a_prin_dist = None
                        class_po_int_dist = None
                        class_po_prin_dist = None
                        tot_dist = None
                    
                if end_cert_bal_a >= 0 and end_cert_bal_po >= 0 and tot_dist >= 0 and tot_dist_po >= 0:
                    break               
            deal_type = 'PO'
        
#        print(dist_date[-2])
#        print(dist_date)
        
        data = [[   
                deal_full_name,
                end_cert_bal_a,
                end_cert_bal_po, # if any
                class_a_int_dist,
                class_a_prin_dist,
                tot_dist,
                class_po_int_dist,
                class_po_prin_dist,
                tot_dist_po,
                paf + trt_fee,
                actual_svcg_fee,
                blocker_cash,
                prd_trig_amt,
                trig_adj_amt,
                trig_thr,
                None,
                deal_type,
                1,               # Default only to 1 group of loans
                "{}/15/20{}".format(dist_date[-2:], dist_date[0:2])
                ]]
        
        df = pd.DataFrame(data)   
        
        df.to_csv("d:/deals/carrington/aggdata/{}/adj_{}_{}.csv".format(dist_date, deal, dist_date), sep=",", header=False, index=False)
        print("Deal {} adj file created.".format(deal))
        
        # this df will be used for cash check and other check 
        return df
        
    except:
        print('Exception happend in create_mod module create_adj function')
    
    
    
###############################################################################
def create_dat(deal, deal_name, path, aggdata_path, dist_date, loan_range, ws):
    try:
        if is_empty(deal_name) == False:
            dat = open('{}{}_{}.dat'.format(path, deal_name, dist_date), 'w+')
        else:
            dat = open('{}_{}.dat'.format(path, dist_date), 'w+')
            print('Make sure you rename the dat file')
    
        remit_path = "{}remit/".format(path)
        
        ws_col = list(ws.columns)
        # Create the monthly distribution dat file (Carrington 7-column)
        #  Wipe out the end_def_prin if there is a fmv
        # If fmv is greater than beg_bal, produce a negative write off in the dat file
        for loan in loan_range:
            # (1) Carrington Ln#
            if not math.isnan(ws.loc[loan, ws_col[0]]): dat.write("{} ".format(str(ws.loc[loan, ws_col[0]])))
            else: pass
    
            # (2) beg_bal, if not empty write beg bal
            if not math.isnan(ws.loc[loan, ws_col[6]]): dat.write('{0:.2f} '.format(ws.loc[loan, ws_col[6]]))
            else: dat.write("0.00 ")
    
            # (3) end bal, if not empty write end bal
            if not math.isnan(ws.loc[loan, ws_col[7]]): dat.write('{0:.2f} '.format(ws.loc[loan, ws_col[7]]))
            else: dat.write("0.00 ")
    
            # (4) prin payment, if not empty write n column
            #                   else if not empty in prin payment and there is a fmv, write prin_pmt + fmv
            #                   else if empty in prin_pmt and there is a fmv, write fmv
            #                   else write zero    
            if not math.isnan(ws.loc[loan, ws_col[13]]) and ws.loc[loan, ws_col[13]] != 0 and ws.loc[loan, ws_col[32]] > 0:
                dat.write('{0:.2f} '.format(ws.loc[loan, ws_col[13]] + ws.loc[loan, ws_col[32]]))
            elif ws.loc[loan, ws_col[13]] == 0 and ws.loc[loan, ws_col[32]] > 0:
                dat.write('{0:.2f} '.format(ws.loc[loan, ws_col[32]]))
            elif not math.isnan(ws.loc[loan, ws_col[13]]): dat.write('{0:.2f} '.format(ws.loc[loan, ws_col[13]]))
            else: dat.write("0.00 ")
    
            # (5) int, if not empty write interest
            if not math.isnan(ws.loc[loan, ws_col[10]]): dat.write('{0:.2f} '.format(ws.loc[loan, ws_col[10]]))
            else: dat.write("0.00 ")
    
            # (6) prin w/r/loss, if not empty write prin_w_off
            #                    else if beg_def_bal not empty and fmv not empty, beg_bal - fmv + beg_def_bal
            #                    else if
            if ws.loc[loan, ws_col[32]] == 0.0 and ws.loc[loan, ws_col[17]] == 0.0 and ws.loc[loan, ws_col[16]] == 0.0:
                dat.write('{0:.2f} '.format(ws.loc[loan, ws_col[17]]))
            elif not math.isnan(ws.loc[loan, ws_col[28]]) and ws.loc[loan, ws_col[32]] > 0:
                dat.write('{0:.2f} '.format(ws.loc[loan, ws_col[6]] - ws.loc[loan, ws_col[32]] + ws.loc[loan, ws_col[28]]))       
            elif not math.isnan(ws.loc[loan, ws_col[17]]) and ws.loc[loan, ws_col[17]] != 0:
                dat.write('{0:.2f} '.format(ws.loc[loan, ws_col[17]]))
            elif ws.loc[loan, ws_col[32]] > 0: dat.write('{0:.2f} '.format(ws.loc[loan, ws_col[6]] - ws.loc[loan, ws_col[32]]))
            else: dat.write("0.00 ")
    
            # (7) end def prin
            if not math.isnan(ws.loc[loan, ws_col[29]]): dat.write('{0:.2f}\n'.format(ws.loc[loan, ws_col[29]]))
            else: dat.write("0.00\n")
                
        dat.close()
        
        # Copy the dat file into remictax/aggdata
        # should be commented out later
        copyfile('{}{}_{}.dat'.format(path, deal_name, dist_date), \
                 "d:/deals/remictax/aggdata/{}_{}.dat".format(deal_name, dist_date))
        
        copyfile('{}{}_{}.dat'.format(path, deal_name, dist_date), \
                 "{}{}_{}.dat".format(remit_path, deal_name, dist_date))
        
        print("Deal {} dat file created in the deal folder.".format(deal))
    
    except:
        print('Exception happend in create_mod module create_dat function')
    
    
###############################################################################