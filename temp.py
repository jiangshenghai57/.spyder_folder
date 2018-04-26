o# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
This py script will have the functionality to call vba script to clean up the CLUB
remit files and attempt to automate the entire process
Within the club macro it can create the 3-column dat file
"""

import sys
import os
import xlwings as xw

#########################################################################################################
# Prompt console for usper input. Follow print func below                                               #
#########################################################################################################
def user_input():
    # Asking user for year and month input
    # Retun the as a 4-digit output as year and month, 1701

    while True:
        dist_date = input("Please enter the distrituion month and year, (example 1701 for January 2017): ")

        try:
            if int(dist_date[-2:]) >= 1 and int(dist_date[-2:]) <= 12:
                month = int(dist_date[-2:])
                year = int(dist_date[0:2])

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


#########################################################################################################
# Calling scrub_sof()/SOFI button within the excel                                                      #
# pulling numbers that will be input in hist-job row                                                    #
# sofi_scrub() will call up the hist-job and paste the data                                             #
#########################################################################################################
def club_scrub():
    dist_date = user_input()
    # Wilmington Trust path sofi remit files path = 'd:/deals/wt/sofi_servicing_report/'
    svcr_path = 'd:/deals/wt/CLUB_servicing_report/'

    remit_files = os.listdir("{}{}/".format(svcr_path, dist_date))
    # FileNotFoundError will pop up if not such dir exist

    # Remove any misc files within the servicing report files
    for file in remit_files:
        if 'sofi' not in file.lower():
            remit_files.pop(remit_files.index(file))


    # Create a macro that python can call when it opens up the hist-job
    wb = xw.Book('d:/execs/ETI CLUB.xlam')
    sofi = wb.macro('club_scrub')

    # Does not show on the screeen
    for file in remit_files:
        wb1 = xw.Book("{}{}/{}".format(svcr_path, dist_date, file))
        sofi()
        wb1.save()
        wb1.close()

    wb.close()


#########################################################################################################
# main func                                                                                             #
#########################################################################################################
if __name__ == '__main__':
    sofi_scrub()
    sys.exit()
