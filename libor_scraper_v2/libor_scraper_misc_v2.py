# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 12:06:01 2018

@author: Shenghai
"""

import os
import sys
import time
import dbf
import pyximport; pyximport.install()

import pandas as pd
from datetime import date
from calendar import monthrange
from selenium import webdriver as wd


        
class UserInput:        
    def __init__(self):
        self.const = Constants()
        
    def user_input_yymm(self):
        # Asking user for year and month input as yymm
        # Retun the date as a 4-digit string as yymm
        try:
            while True:
                
                distribution_yymm = input("Please enter the distrituion month and year, " + \
                                               "(example 1701 for January 2017): ")
                try:
                    if (int(distribution_yymm[self.const.TWO:self.const.FOUR]) >= self.const.ONE) and \
                    (int(distribution_yymm[self.const.TWO:self.const.FOUR]) <= self.const.TWELVE) and \
                    (len(distribution_yymm) == self.const.FOUR):
                        
                        month = int(distribution_yymm[self.const.TWO:self.const.FOUR])
                        year = int(distribution_yymm[self.const.ZERO:self.const.TWO])
                        if month < self.const.TEN:
                            month = "0{}".format(str(month))
                        else:
                            month = str(month)
                           
                        distribution_yymm= "{}{}".format(str(year), str(month))
                        break
                    else: 
                        print("Let's try this again!")
                        continue
                    
                except: 
                    print("Let's try this again!")
                    pass
        
            # return dist_date as a string like 1801 for Jan. 2018
            return distribution_yymm
        
        except:
            print("Error handling happened in user_input_yymm function!!!")
            
          
class LiborScraper:
    
    # Initialize object url and frequently used constants
    def __init__(self):
        self.const = Constants()
        self.url = "https://fred.stlouisfed.org/series/USD1MTD156N"      
        self.df = None
        self.libor_file = None
   
    # main func to open the st. louis website and download
    def download_libor_csv(self):
        try:
            self.driver = wd.Chrome()
            self.driver.get(self.url)
            time.sleep(self.const.THREE)
            year = str(date.today())[self.const.ZERO:self.const.FOUR]
            month = str(date.today())[self.const.FIVE:self.const.SEVEN]
            
            first_day = self.driver.find_element_by_id("input-cosd")
            last_day = self.driver.find_element_by_id("input-coed")
            first_day.clear()
            last_day.clear()
            
            if int(month) == self.const.ONE:
                first_day.send_keys("{}-01-01".format(int(year) - self.const.ONE))
                last_day.clear()
                last_day.send_keys("{}-12-31".format(int(year) - self.const.ONE))
                time.sleep(self.const.ONE)
            else:
                first_day.send_keys("{}-01-01".format(year))
                last_day.clear()
                last_day.send_keys("{}-{}-{}".format(year, int(month) - self.const.ONE, \
                                    str(monthrange(int(year), int(month) - self.const.ONE)[self.const.ONE])))
                time.sleep(self.const.ONE)
                
            download = self.driver.find_element_by_xpath("//*[@id='download-button']/span")
            download.click()
            time.sleep(self.const.ONEOFIVE)
            download_csv = self.driver.find_element_by_xpath("//*[@id='download-data-csv']")
            download_csv.click()
            time.sleep(self.const.TWO)
            self.driver.close()
            
        except:
            print("Error handling happened in download_libor_csv function!!!")
     
    
    # Modulize finding the csv in download folder
    # If ever there is an issue in create_dbf function, there is no need to open
    # the chrome driver and downlaod again
    def find_libor_csv(self):
        try:
            home = os.path.expanduser("~")
            home = os.path.join(home, "Downloads\\")
            files = os.listdir(home)
            for file in files:
                if "USD1M" in str(file):
                    self.libor_file = "{}{}".format(home, file)
                    break
                else:
                    self.libor_file = None
            
            if self.libor_file is None:
                print("Did you download the file correctly???")
                input("Press Enter to exit --->>>")
                sys.exit()
                
            df = pd.read_csv(self.libor_file)
            
            self.df = df
            
        except:
            print("Error handling happened in find_libor_csv function")
            raise
            
            
    # func to create dbf from the downloaded csv
    def create_dbf(self):
        self.output_path = "d:/deals/remictax/"
        
        table = dbf.Table("{}LIBOR_1MO".format(self.output_path), 'Month D')
        table.open(mode=dbf.READ_WRITE)
        # Add fields day 1 through day 31
        for i in range(self.const.ONE, self.const.THIRTYTWO):
            table.add_fields("day_{} N(9, 7)".format(i))            

        year = str(date.today())[self.const.ZERO:self.const.FOUR]
        month = str(date.today())[self.const.FIVE:self.const.SEVEN]
        
        # If month is January month would be 12 and year would be previous year
        if month == "01":
            month = "13"
            year = str(int(year) - self.const.ONE)
        
        # This for loop determines how many rows are there
        # if we are at Nov. there would be 11 rows, if at Dec. there would be 12 rows

        for i in range(self.const.ONE, int(month)):   
            
            if i < self.const.TEN:
                month_str = "0{}".format(i)
            else:
                month_str = str(i)
            
            # reference dictionary would be put into dbf row
            # daily libor row for that month
            # will reset after each loop
            reference_dict = {}

            temp_df = self.df.loc[self.df["DATE"].str[self.const.FIVE:self.const.SEVEN] == month_str]
            
            # Looping through the libor csv from the download folder
            for j in range(int(temp_df.index[self.const.ZERO]), int(temp_df.index[-self.const.ONE]) + self.const.ONE):
                
                day_x = temp_df.loc[j, "DATE"]
                day_x = int(day_x[-self.const.TWO:])
                   
                if self.df.loc[j, "USD1MTD156N"] != "." and \
                float(self.df.loc[j, "USD1MTD156N"]):
                    reference_dict["day_{}".format(day_x)] = float(self.df.loc[j, "USD1MTD156N"]) / self.const.HUNDRED
                    
            # Clean up any day_x that does not have any value to None in dbf
            for j in range(self.const.ONE, self.const.THIRTYTWO):           
                # This if statement ensures values does not get over written by None
                if "day_{}".format(j) in reference_dict.keys():
                    continue
                else:
                    reference_dict["day_{}".format(j)] = None
                    continue     
                        
                    
            if i < self.const.TEN:
                i = "0{}".format(i)
             
            # For loop put daily libors into corresponding month row
            for datum in (
                    (
                    dbf.Date("{}-{}-01".format(year, i)),
                    reference_dict["day_1"],
                    reference_dict["day_2"],
                    reference_dict["day_3"],
                    reference_dict["day_4"],
                    reference_dict["day_5"],
                    reference_dict["day_6"],
                    reference_dict["day_7"],
                    reference_dict["day_8"],
                    reference_dict["day_9"],
                    reference_dict["day_10"],
                    reference_dict["day_11"],
                    reference_dict["day_12"],
                    reference_dict["day_13"],
                    reference_dict["day_14"],
                    reference_dict["day_15"],
                    reference_dict["day_16"],
                    reference_dict["day_17"],
                    reference_dict["day_18"],
                    reference_dict["day_19"],
                    reference_dict["day_20"],
                    reference_dict["day_21"],
                    reference_dict["day_22"],
                    reference_dict["day_23"],
                    reference_dict["day_24"],
                    reference_dict["day_25"],
                    reference_dict["day_26"],
                    reference_dict["day_27"],
                    reference_dict["day_28"],
                    reference_dict["day_29"],
                    reference_dict["day_30"],
                    reference_dict["day_31"]
                     ),
                    ): table.append(datum)
                    
                
        table.close()
        
        print("LIBOR_1MO.dbf created in dir 'D:\\deals\\remictax'")
        os.remove(self.libor_file)
    
class Constants:
    """
    Frequently used constants
    """
    def __init__(self):
        self.ZERO = 0
        self.ONE  = 1
        self.TWO  = 2
        self.THREE = 3
        self.FOUR = 4
        self.FIVE = 5
        self.SIX  = 6
        self.SEVEN = 7
        self.EIGHT = 8
        self.TEN  = 10
        self.TWELVE = 12
        self.EIGHTEEN = 18
        self.THIRTY = 30
        self.THIRTYTWO = 32
        self.THIRTYTHREE = 33
        self.HUNDRED = 100
        self.ONEOFIVE = 1.5