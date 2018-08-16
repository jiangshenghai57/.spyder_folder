# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 17:35:21 2018

@author: Shenghai
"""


from selenium import webdriver as wd
import time
import os
import sys
from misc_class_module import Miscellaneous
from datetime import date
from calendar import monthrange
import pandas as pd
import win32com.client

create_dbf = Miscellaneous.create_dbf
user_input = Miscellaneous.user_input
driver = wd.Chrome()
url = "https://fred.stlouisfed.org/series/USD1MTD156N"

ZERO = 0
ONE = 1
FOUR = 4
FIVE = 5
SEVEN = 7
ONEOFIVE = 1.5

###############################################################################

def libor_scraper():
    try:
        # open up the browser input the date and download the csv
        driver.get(url)
        year = str(date.today())[ZERO:FOUR]
        month = str(date.today())[FIVE:SEVEN]

        first_day = driver.find_element_by_id("input-cosd")
        last_day = driver.find_element_by_id("input-coed")
        first_day.clear()
        last_day.clear()

        if int(month) == ONE:
            first_day.send_keys("{}-01-01".format(int(year) - ONE))
            last_day.send_keys("{}-12-31".format(int(year) - ONE))
        else:
            first_day.send_keys("{}-01-01".format(year))
            last_day.send_keys("{}-{}-{}".format(year, int(month) - ONE, str(monthrange(int(year), int(month) - ONE)[ONE])))

        download = driver.find_element_by_xpath("//*[@id='download-button']/span")
        download.click()
        download_csv = driver.find_element_by_xpath("//*[@id='download-data-csv']")
        download_csv.click()

        time.sleep(ONEOFIVE)

        driver.close()

        # find the file in the download folder
        download_path = "C:\\users\\shenghai.etidomain\downloads\\"
        files = os.listdir(download_path)
        for file in files:
            if "USD1M" in str(file):
                libor_file = "{}{}".format(download_path, file)
                break
            else:
                libor_file = None

        if not libor_file:
            print("Did you download the file correctly???")
            input("Press Enter to Exit >>>")
            sys.exit()

        df = pd.read_csv(libor_file)

        os.remove(libor_file)

        return df

    except:
        print('Exception happened in libor_scraper function.')

###############################################################################

def send_dbf():
    try:
        outlook = win32com.client.Dispatch('Outlook.Application')
        msg = outlook.CreateItem(ZERO)
        msg.To = "shenghaijiang@e-t-i.com; "

        msg.Subject = "1-Month USD LIBOR"
        msg.Body = "Please see attached."
        attachment1 = "D:/deals/remictax/LIBOR_1MO.dbf"
        msg.Attachments.Add(Source=attachment1)
        msg.display()
        msg.Send()
        print("DBF file sent.")

    except:
        print('Exception happend in send_dbf function')

###############################################################################

if __name__ == '__main__':
    df = libor_scraper()
    create_dbf(df)
#    send_dbf()
    input("Press Enter to exit >>>")
    sys.exit()
