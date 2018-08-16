# -*- coding: utf-8 -*-
"""
Created on Thu May 17 16:51:03 2018

@author: Shenghai
"""
import dbf
from datetime import date
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
                else:
                    continue
            except:
                pass
    
        # return dist_date as a string like 1801 for Jan. 2018
        return dist_date
    
    
###############################################################################
# If variable empty return true else false                                     
###############################################################################
    def is_empty(any_structure):
        # empty structure is False by default
        if any_structure:
            return False
        else:
            return True
        
###############################################################################
    # This function produce Myymm.CLD file
    def create_dbf(df):
        try:
            path = "d:/deals/remictax/"
            table = dbf.Table("{}LIBOR_1MO".format(path), 'Month D')
            table.open()
            table.add_fields("day_1  N(9, 7)")
            table.add_fields("day_2  N(9, 7)")
            table.add_fields("day_3  N(9, 7)")
            table.add_fields("day_4  N(9, 7)")
            table.add_fields("day_5  N(9, 7)")
            table.add_fields("day_6  N(9, 7)")
            table.add_fields("day_7  N(9, 7)")
            table.add_fields("day_8  N(9, 7)")
            table.add_fields("day_9  N(9, 7)")
            table.add_fields("day_10 N(9, 7)")
            table.add_fields("day_11 N(9, 7)")
            table.add_fields("day_12 N(9, 7)")
            table.add_fields("day_13 N(9, 7)")
            table.add_fields("day_14 N(9, 7)")
            table.add_fields("day_15 N(9, 7)")
            table.add_fields("day_16 N(9, 7)")
            table.add_fields("day_17 N(9, 7)")
            table.add_fields("day_18 N(9, 7)")
            table.add_fields("day_19 N(9, 7)")
            table.add_fields("day_20 N(9, 7)")
            table.add_fields("day_21 N(9, 7)")
            table.add_fields("day_22 N(9, 7)")
            table.add_fields("day_23 N(9, 7)")
            table.add_fields("day_24 N(9, 7)")
            table.add_fields("day_25 N(9, 7)")
            table.add_fields("day_26 N(9, 7)")
            table.add_fields("day_27 N(9, 7)")
            table.add_fields("day_28 N(9, 7)")
            table.add_fields("day_29 N(9, 7)")
            table.add_fields("day_30 N(9, 7)")
            table.add_fields("day_31 N(9, 7)")
    
            year = str(date.today())[0:4]
            month = str(date.today())[5:7]
    
            for i in range(1, int(month)):
                
                
                for j in range(0, len(df)):
                    day_x = df.loc[j, "DATE"]
                    if int(day_x[5:7]) == i:
                                    
                        if int(day_x[-2:]) == 1 and df.loc[j, "USD1MTD156N"] != "." and \
                        float(df.loc[j, "USD1MTD156N"]):
                            day_1 = float(df.loc[j, "USD1MTD156N"]) / 100
                            break
                        else:
                            day_1 = None
                            
                for j in range(0, len(df)):
                    day_x = df.loc[j, "DATE"]
                    if int(day_x[5:7]) == i:
                        if int(day_x[-2:]) == 2 and df.loc[j, "USD1MTD156N"] != "." and \
                        float(df.loc[j, "USD1MTD156N"]):
                            day_2 = float(df.loc[j, "USD1MTD156N"]) / 100
                            break
                        else:
                            day_2 = None
                
                for j in range(0, len(df)):
                    day_x = df.loc[j, "DATE"]
                    if int(day_x[5:7]) == i:            
                        if int(day_x[-2:]) == 3 and df.loc[j, "USD1MTD156N"] != "." and \
                        float(df.loc[j, "USD1MTD156N"]):
                            day_3 = float(df.loc[j, "USD1MTD156N"]) / 100
                            break
                        else:
                            day_3 = None
               
                for j in range(0, len(df)):
                    day_x = df.loc[j, "DATE"]
                    if int(day_x[5:7]) == i:             
                        if int(day_x[-2:]) == 4 and df.loc[j, "USD1MTD156N"] != "." and \
                        float(df.loc[j, "USD1MTD156N"]):
                            day_4 = float(df.loc[j, "USD1MTD156N"]) / 100
                            break
                        else:
                            day_4 = None
               
                for j in range(0, len(df)):
                    day_x = df.loc[j, "DATE"]
                    if int(day_x[5:7]) == i:             
                        if int(day_x[-2:]) == 5 and df.loc[j, "USD1MTD156N"] != "." and \
                        float(df.loc[j, "USD1MTD156N"]):
                            day_5 = float(df.loc[j, "USD1MTD156N"]) / 100
                            break
                        else:
                            day_5 = None
             
                for j in range(0, len(df)):
                    day_x = df.loc[j, "DATE"]
                    if int(day_x[5:7]) == i:             
                        if int(day_x[-2:]) == 6 and df.loc[j, "USD1MTD156N"] != "." and \
                        float(df.loc[j, "USD1MTD156N"]):
                            day_6 = float(df.loc[j, "USD1MTD156N"]) / 100
                            break
                        else:
                            day_6 = None
                            
                for j in range(0, len(df)):
                    day_x = df.loc[j, "DATE"]
                    if int(day_x[5:7]) == i:             
                        if int(day_x[-2:]) == 7 and df.loc[j, "USD1MTD156N"] != "." and \
                        float(df.loc[j, "USD1MTD156N"]):
                            day_7 = float(df.loc[j, "USD1MTD156N"]) / 100
                            break
                        else:
                            day_7 = None
                            
                for j in range(0, len(df)):
                    day_x = df.loc[j, "DATE"]
                    if int(day_x[5:7]) == i:             
                        if int(day_x[-2:]) == 8 and df.loc[j, "USD1MTD156N"] != "." and \
                        float(df.loc[j, "USD1MTD156N"]):
                            day_8 = float(df.loc[j, "USD1MTD156N"]) / 100
                            break
                        else:
                            day_8 = None
                
                for j in range(0, len(df)):
                    day_x = df.loc[j, "DATE"]
                    if int(day_x[5:7]) == i:             
                        if int(day_x[-2:]) == 9 and df.loc[j, "USD1MTD156N"] != "." and \
                        float(df.loc[j, "USD1MTD156N"]):
                            day_9 = float(df.loc[j, "USD1MTD156N"]) / 100
                            break
                        else:
                            day_9 = None
                            
                for j in range(0, len(df)):
                    day_x = df.loc[j, "DATE"]
                    if int(day_x[5:7]) == i:             
                        if int(day_x[-2:]) == 10 and df.loc[j, "USD1MTD156N"] != "." and \
                        float(df.loc[j, "USD1MTD156N"]):
                            day_10 = float(df.loc[j, "USD1MTD156N"]) / 100
                            break
                        else:
                            day_10 = None
                            
                for j in range(0, len(df)):
                    day_x = df.loc[j, "DATE"]
                    if int(day_x[5:7]) == i:             
                        if int(day_x[-2:]) == 11 and df.loc[j, "USD1MTD156N"] != "." and \
                        float(df.loc[j, "USD1MTD156N"]):
                            day_11 = float(df.loc[j, "USD1MTD156N"]) / 100
                            break
                        else:
                            day_11 = None
                            
                for j in range(0, len(df)):
                    day_x = df.loc[j, "DATE"]
                    if int(day_x[5:7]) == i:             
                        if int(day_x[-2:]) == 12 and df.loc[j, "USD1MTD156N"] != "." and \
                        float(df.loc[j, "USD1MTD156N"]):
                            day_12 = float(df.loc[j, "USD1MTD156N"]) / 100
                            break
                        else:
                            day_12 = None
                            
                for j in range(0, len(df)):
                    day_x = df.loc[j, "DATE"]
                    if int(day_x[5:7]) == i:             
                        if int(day_x[-2:]) == 13 and df.loc[j, "USD1MTD156N"] != "." and \
                        float(df.loc[j, "USD1MTD156N"]):
                            day_13 = float(df.loc[j, "USD1MTD156N"]) / 100
                            break
                        else:
                            day_13 = None
                 
                for j in range(0, len(df)):
                    day_x = df.loc[j, "DATE"]
                    if int(day_x[5:7]) == i:             
                        if int(day_x[-2:]) == 14 and df.loc[j, "USD1MTD156N"] != "." and \
                        float(df.loc[j, "USD1MTD156N"]):
                            day_14 = float(df.loc[j, "USD1MTD156N"]) / 100
                            break
                        else:
                            day_14 = None
                            
                for j in range(0, len(df)):
                    day_x = df.loc[j, "DATE"]
                    if int(day_x[5:7]) == i:             
                        if int(day_x[-2:]) == 15 and df.loc[j, "USD1MTD156N"] != "." and \
                        float(df.loc[j, "USD1MTD156N"]):
                            day_15 = float(df.loc[j, "USD1MTD156N"]) / 100
                            break
                        else:
                            day_15 = None
                            
                for j in range(0, len(df)):
                    day_x = df.loc[j, "DATE"]
                    if int(day_x[5:7]) == i:             
                        if int(day_x[-2:]) == 16 and df.loc[j, "USD1MTD156N"] != "." and \
                        float(df.loc[j, "USD1MTD156N"]):
                            day_16 = float(df.loc[j, "USD1MTD156N"]) / 100
                            break
                        else:
                            day_16 = None
                            
                for j in range(0, len(df)):
                    day_x = df.loc[j, "DATE"]
                    if int(day_x[5:7]) == i:             
                        if int(day_x[-2:]) == 17 and df.loc[j, "USD1MTD156N"] != "." and \
                        float(df.loc[j, "USD1MTD156N"]):
                            day_17 = float(df.loc[j, "USD1MTD156N"]) / 100
                            break
                        else:
                            day_17 = None
              
                for j in range(0, len(df)):
                    day_x = df.loc[j, "DATE"]
                    if int(day_x[5:7]) == i:             
                        if int(day_x[-2:]) == 18 and df.loc[j, "USD1MTD156N"] != "." and \
                        float(df.loc[j, "USD1MTD156N"]):
                            day_18 = float(df.loc[j, "USD1MTD156N"]) / 100
                            break
                        else:
                            day_18 = None
                            
                for j in range(0, len(df)):
                    day_x = df.loc[j, "DATE"]
                    if int(day_x[5:7]) == i:             
                        if int(day_x[-2:]) == 19 and df.loc[j, "USD1MTD156N"] != "." and \
                        float(df.loc[j, "USD1MTD156N"]):
                            day_19 = float(df.loc[j, "USD1MTD156N"]) / 100
                            break
                        else:
                            day_19 = None
                 
                for j in range(0, len(df)):
                    day_x = df.loc[j, "DATE"]
                    if int(day_x[5:7]) == i:             
                        if int(day_x[-2:]) == 20 and df.loc[j, "USD1MTD156N"] != "." and \
                        float(df.loc[j, "USD1MTD156N"]):
                            day_20 = float(df.loc[j, "USD1MTD156N"]) / 100
                            break
                        else:
                            day_20 = None
                 
                for j in range(0, len(df)):
                    day_x = df.loc[j, "DATE"]
                    if int(day_x[5:7]) == i:             
                        if int(day_x[-2:]) == 21 and df.loc[j, "USD1MTD156N"] != "." and \
                        float(df.loc[j, "USD1MTD156N"]):
                            day_21 = float(df.loc[j, "USD1MTD156N"]) / 100
                            break
                        else:
                            day_21 = None
                            
                for j in range(0, len(df)):
                    day_x = df.loc[j, "DATE"]
                    if int(day_x[5:7]) == i:             
                        if int(day_x[-2:]) == 22 and df.loc[j, "USD1MTD156N"] != "." and \
                        float(df.loc[j, "USD1MTD156N"]):
                            day_22 = float(df.loc[j, "USD1MTD156N"]) / 100
                            break
                        else:
                            day_22 = None
                
                for j in range(0, len(df)):
                    day_x = df.loc[j, "DATE"]
                    if int(day_x[5:7]) == i:             
                        if int(day_x[-2:]) == 23 and df.loc[j, "USD1MTD156N"] != "." and \
                        float(df.loc[j, "USD1MTD156N"]):
                            day_23 = float(df.loc[j, "USD1MTD156N"]) / 100
                            break
                        else:
                            day_23 = None
                            
                for j in range(0, len(df)):
                    day_x = df.loc[j, "DATE"]
                    if int(day_x[5:7]) == i:             
                        if int(day_x[-2:]) == 24 and df.loc[j, "USD1MTD156N"] != "." and \
                        float(df.loc[j, "USD1MTD156N"]):
                            day_24 = float(df.loc[j, "USD1MTD156N"]) / 100
                            break
                        else:
                            day_24 = None
                            
                for j in range(0, len(df)):
                    day_x = df.loc[j, "DATE"]
                    if int(day_x[5:7]) == i:             
                        if int(day_x[-2:]) == 25 and df.loc[j, "USD1MTD156N"] != "." and \
                        float(df.loc[j, "USD1MTD156N"]):
                            day_25 = float(df.loc[j, "USD1MTD156N"]) / 100
                            break
                        else:
                            day_25 = None
                            
                for j in range(0, len(df)):
                    day_x = df.loc[j, "DATE"]
                    if int(day_x[5:7]) == i:             
                        if int(day_x[-2:]) == 26 and df.loc[j, "USD1MTD156N"] != "." and \
                        float(df.loc[j, "USD1MTD156N"]):
                            day_26 = float(df.loc[j, "USD1MTD156N"]) / 100
                            break
                        else:
                            day_26 = None
                            
                for j in range(0, len(df)):
                    day_x = df.loc[j, "DATE"]
                    if int(day_x[5:7]) == i:             
                        if int(day_x[-2:]) == 27 and df.loc[j, "USD1MTD156N"] != "." and \
                        float(df.loc[j, "USD1MTD156N"]):
                            day_27 = float(df.loc[j, "USD1MTD156N"]) / 100
                            break
                        else:
                            day_27 = None
                            
                for j in range(0, len(df)):
                    day_x = df.loc[j, "DATE"]
                    if int(day_x[5:7]) == i:             
                        if int(day_x[-2:]) == 28 and df.loc[j, "USD1MTD156N"] != "." and \
                        float(df.loc[j, "USD1MTD156N"]):
                            day_28 = float(df.loc[j, "USD1MTD156N"]) / 100
                            break
                        else:
                            day_28 = None
                            
                for j in range(0, len(df)):
                    day_x = df.loc[j, "DATE"]
                    if int(day_x[5:7]) == i:             
                        if int(day_x[-2:]) == 29 and df.loc[j, "USD1MTD156N"] != "." and \
                        float(df.loc[j, "USD1MTD156N"]):
                            day_29 = float(df.loc[j, "USD1MTD156N"]) / 100
                            break
                        else:
                            day_29 = None
                            
                for j in range(0, len(df)):
                    day_x = df.loc[j, "DATE"]
                    if int(day_x[5:7]) == i:             
                        if int(day_x[-2:]) == 30 and df.loc[j, "USD1MTD156N"] != "." and \
                        float(df.loc[j, "USD1MTD156N"]):
                            day_30 = float(df.loc[j, "USD1MTD156N"]) / 100
                            break
                        else:
                            day_30 = None
                            
                for j in range(0, len(df)):
                    day_x = df.loc[j, "DATE"]
                    if int(day_x[5:7]) == i:             
                        if int(day_x[-2:]) == 31 and df.loc[j, "USD1MTD156N"] != "." and \
                        float(df.loc[j, "USD1MTD156N"]):
                            day_31 = float(df.loc[j, "USD1MTD156N"]) / 100
                            break
                        else:
                            day_31 = None
                                      
                if i < 10:
                    i = "0{}".format(i)
                       
                for datum in (
                        (
                        dbf.Date("{}-{}-01".format(year, i)),
                        day_1 ,
                        day_2 ,
                        day_3 ,
                        day_4 ,
                        day_5 ,
                        day_6 ,
                        day_7 ,
                        day_8 ,
                        day_9 ,
                        day_10,
                        day_11,
                        day_12,
                        day_13,
                        day_14,
                        day_15,
                        day_16,
                        day_17,
                        day_18,
                        day_19,
                        day_20,
                        day_21,
                        day_22,
                        day_23,
                        day_24,
                        day_25,
                        day_26,
                        day_27,
                        day_28,
                        day_29,
                        day_30,
                        day_31
                         ),
                        ):
                    table.append(datum)
     
            table.close()
          
            print("LIBOR_1MO.dbf created in dir 'D:\\deals\\remictax'")
            
        except:
            print('Exception happened in misc module create_dbf function')
