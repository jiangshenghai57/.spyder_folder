# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

#Box
#########################################################################################################
#                                                                                                       #
#########################################################################################################
"""

import os
from shutil import copyfile
import sys

#########################################################################################################
# Taking distribution date as an argument and return last month in 4-digit                              #
#########################################################################################################
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

    # Return last month value as 1801 if cur mon is 1802
    return last_mon

#########################################################################################################
# Prompt console for usper input. Follow print func below                                               #
#########################################################################################################
def user_input():
    # Asking user for month and year input
    # This chunck of codes will give the string info for what period of files to download
    # More features could be add in to ask users
    print("If you want to copy remit files over for a specific month and year,")
    dist_date = input("please enter the distrituion month and year, (example 0117 for January 2017): ")

    month = int(dist_date[0:2])
    year = int(dist_date[-2:])

    if month < 10:
        month = "0" + str(month)
    else:
        month = str(month)

    dist_date = str(year) + month
    # return dist_date as a string like 1801 for Jan. 2018
    return dist_date
    exit()


#########################################################################################################
# Going to //etiserver/etishare to find carrington remit files                                          #
#########################################################################################################
def copy_remit():
    dist_date = user_input()
    lst_month = last_mon(dist_date)
    # deals dictionary with their associated deals investor code
    my_deals_dict = {'2013-23': '2173',
                     '2014-03': '2181',
                     '2014-05': '2191',
                     '2015-01': '2194',
                     '2015-08': '2209',
                     '2015-09': '2212',
                     '2016-01': '2215',
                     '2016-04': '2224',
                     '2016-21': '2218',
                     '2016-23': '2227',
                     '2016-31': '2237',
                     '2016-32': '2248'}

    my_deals = list(my_deals_dict.keys())
    my_deals_invnum = list(my_deals_dict.values())

    path = '//etiserver/etishare/tom/carrington/smlt/cms_servicer_files_download/new/'
    files = os.listdir(path)

    # make monthly remit directories
    for i in range(0,len(my_deals)):
        if not os.path.exists("d:/deals/carrington/smac/" + my_deals[i] + "/remit/" + dist_date + "/"):
            os.makedirs("d:/deals/carrington/smac/" + my_deals[i] + "/remit/" + dist_date + "/")
            # Searcing algo for current month and
            for file in files:
                if (lst_month[-2:] in file) and (my_deals_invnum[i] in file) :
                    copyfile(path + file, "d:/deals/carrington/smac/" + my_deals[i] + "/remit/" + dist_date + "/" + file)
                    print("This file: " + file + " just got moved into " + "d:/deals/carrington/smac/" + my_deals[i] + "/remit/" + dist_date + "/" + file)
        else:
            # Overwrite
            print("Directory already exists!!!")

if __name__ == '__main__':
    copy_remit()
    input("Press Enter to exit...")

