# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 09:52:18 2017

@author: Shenghai
"""

import requests
from lxml import html
from selenium import webdriver as wd
import time
import zipfile
import os
import sys
# Using Chrome Browser as the driver, creating an driver object
driver = wd.Chrome()

# Wells Fargo login website
login_url = 'http://www.ctslink.com'

# Each link to individual deal's download webpage 
url = [
       # Brian's AHMIT and HomeBanc deal list
#       "https://www.ctslink.com/a/history.html?shelfId=AHMI&seriesId=20051&doc=AHMI_20051_RMT",
#       "https://www.ctslink.com/a/history.html?shelfId=AHMI&seriesId=20054&doc=AHMI_20054_RMT",
#       "https://www.ctslink.com/a/history.html?shelfId=AHMI&seriesId=20063&doc=AHMI_20063_RMT",
#       "https://www.ctslink.com/a/history.html?shelfId=AHMI&seriesId=20072&doc=AHMI_20072_RMT",
#       "https://www.ctslink.com/a/history.html?shelfId=HOMEBANC&seriesId=20041&doc=HOMEBANC_20041_RMT",
#       "https://www.ctslink.com/a/history.html?shelfId=HOMEBANC&seriesId=20042&doc=HOMEBANC_20042_RMT",
#       "https://www.ctslink.com/a/history.html?shelfId=HOMEBANC&seriesId=20051&doc=HOMEBANC_20051_RMT",
#       "https://www.ctslink.com/a/history.html?shelfId=HOMEBANC&seriesId=20052&doc=HOMEBANC_20052_RMT",
#       "https://www.ctslink.com/a/history.html?shelfId=HOMEBANC&seriesId=20053&doc=HOMEBANC_20053_RMT",
#       "https://www.ctslink.com/a/history.html?shelfId=HOMEBANC&seriesId=20054&doc=HOMEBANC_20054_RMT",
#       "https://www.ctslink.com/a/history.html?shelfId=HOMEBANC&seriesId=20055&doc=HOMEBANC_20055_RMT",
#       "https://www.ctslink.com/a/history.html?shelfId=HOMEBANC&seriesId=20062&doc=HOMEBANC_20062_RMT",
       
       # Brian's Carrington deal list
        "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=201320&doc=SMLT_201320_RMT", 
        "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=201320RT&doc=SMLT_201320RT_RMT",
        "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=201321&doc=SMLT_201321_RMT", 
        "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=201321RT&doc=SMLT_201321RT_RMT",
        "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20141&doc=SMLT_20141_RMT", 
        "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20141RT&doc=SMLT_20141RT_RMT",
        "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20144&doc=SMLT_20144_RMT", 
        "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20144RT&doc=SMLT_20144RT_RMT",
        "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20153&doc=SMLT_20153_RMT",
        "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20153RT&doc=SMLT_20153RT_RMT",
        "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20154&doc=SMLT_20154_RMT",
        "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20154RT&doc=SMLT_20154RT_RMT",
        "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20155&doc=SMLT_20155_RMT",
        "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20155RT&doc=SMLT_20155RT_RMT",
        "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20157&doc=SMLT_20157_RMT",
        "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20157RT&doc=SMLT_20157RT_RMT",
        "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20165&doc=SMLT_20165_RMT",
        "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20165RT&doc=SMLT_20165RT_RMT",
        "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20166&doc=SMLT_20166_RMT",
        "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20166RT&doc=SMLT_20166RT_RMT",
        "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20167&doc=SMLT_20167_RMT",
        "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20167RT&doc=SMLT_20167RT_RMT",
        "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20168&doc=SMLT_20168_RMT",
        "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20168RT&doc=SMLT_20168RT_RMT",
        "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20169&doc=SMLT_20169_RMT",
        "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20169RT&doc=SMLT_20169RT_RMT",
        "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=201610&doc=SMLT_201610_RMT",
        "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=201610RT&doc=SMLT_201610RT_RMT",
        "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=201611&doc=SMLT_201611_RMT",
        "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=201611RT&doc=SMLT_201611RT_RMT",
        "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=201612&doc=SMLT_201612_RMT",
        "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=201612RT&doc=SMLT_201612RT_RMT",
        "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20171&doc=SMLT_20171_RMT",
        "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20171RT&doc=SMLT_20171RT_RMT",
        "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20172&doc=SMLT_20172_RMT",
        "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20172RT&doc=SMLT_20172RT_RMT",
        "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20173&doc=SMLT_20173_RMT",
        "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20173RT&doc=SMLT_20173RT_RMT",
        "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20174&doc=SMLT_20174_RMT",
        "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20174RT&doc=SMLT_20174RT_RMT",
        "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20175&doc=SMLT_20175_RMT",
        "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20175RT&doc=SMLT_20175RT_RMT",
        "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20176&doc=SMLT_20176_RMT",
        "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20176RT&doc=SMLT_20176RT_RMT",
        "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=201721&doc=SMLT_201721_RMT",
        "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=201721RT&doc=SMLT_201721RT_RMT",
        "https://www.ctslink.com/a/history.html?shelfId=UMAC&seriesId=201731&doc=UMAC_201731_RMT",
        "https://www.ctslink.com/a/history.html?shelfId=UMAC&seriesId=201731RT&doc=UMAC_201731RT_RMT",
        "https://www.ctslink.com/a/history.html?shelfId=UMAC&seriesId=201732&doc=UMAC_201732_RMT",
        "https://www.ctslink.com/a/history.html?shelfId=UMAC&seriesId=201732RT&doc=UMAC_201732RT_RMT",
        "https://www.ctslink.com/a/history.html?shelfId=UMAC&seriesId=201733&doc=UMAC_201733_RMT",
        "https://www.ctslink.com/a/history.html?shelfId=UMAC&seriesId=201733RT&doc=UMAC_201733RT_RMT",
        "https://www.ctslink.com/a/history.html?shelfId=UMAC&seriesId=201734&doc=UMAC_201734_RMT",
        "https://www.ctslink.com/a/history.html?shelfId=UMAC&seriesId=201734RT&doc=UMAC_201734RT_RMT",
  
       # Shenghai's deal list
#       "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=201323&doc=SMLT_201323_RMT", 
#       "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=201323RT&doc=SMLT_201323RT_RMT",
#       "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20143&doc=SMLT_20143_RMT", 
#       "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20143RT&doc=SMLT_20143RT_RMT",
#       "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20145&doc=SMLT_20145_RMT", 
#       "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20145RT&doc=SMLT_20145RT_RMT",
#       "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20151&doc=SMLT_20151_RMT", 
#       "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20151RT&doc=SMLT_20151RT_RMT",
#       "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20158&doc=SMLT_20158_RMT", 
#       "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20158RT&doc=SMLT_20158RT_RMT",
#       "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20159&doc=SMLT_20159_RMT", 
#       "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20159RT&doc=SMLT_20159RT_RMT",
#       "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20161&doc=SMLT_20161_RMT", 
#       "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20161RT&doc=SMLT_20161RT_RMT",
#       "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20164&doc=SMLT_20164_RMT", 
#       "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20164RT&doc=SMLT_20164RT_RMT",
#       "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=201621&doc=SMLT_201621_RMT", 
#       "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=201621RT&doc=SMLT_201621RT_RMT",
#       "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=201623&doc=SMLT_201623_RMT", 
#       "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=201623RT&doc=SMLT_201623RT_RMT",
#       "https://www.ctslink.com/a/history.html?shelfId=UMAC&seriesId=201631&doc=UMAC_201631_RMT", 
#       "https://www.ctslink.com/a/history.html?shelfId=UMAC&seriesId=201631RT&doc=UMAC_201631RT_RMT",
#       "https://www.ctslink.com/a/history.html?shelfId=UMAC&seriesId=201632&doc=UMAC_201632_RMT", 
#       "https://www.ctslink.com/a/history.html?shelfId=UMAC&seriesId=201632RT&doc=UMAC_201632RT_RMT",
#       "https://www.ctslink.com/a/history.html?shelfId=UMAC&seriesId=201732&doc=UMAC_201732_RMT", 
#       "https://www.ctslink.com/a/history.html?shelfId=UMAC&seriesId=201732RT&doc=UMAC_201732RT_RMT",
#       "https://www.ctslink.com/a/history.html?shelfId=UMAC&seriesId=201733&doc=UMAC_201733_RMT", 
#       "https://www.ctslink.com/a/history.html?shelfId=UMAC&seriesId=201733RT&doc=UMAC_201733RT_RMT",
#       "https://www.ctslink.com/a/history.html?shelfId=NMLT&seriesId=20151&doc=NMLT_20151_RMT",
#       "https://www.ctslink.com/a/history.html?shelfId=NMLT&seriesId=20151RT&doc=NMLT_20151RT_RMT",
       ]

def user_input():
    # Asking user for month and year input
    # This chunck of codes will give the string info for what period of files to download
    # More features could be add in to ask users 
    print("If you want the entire year of PDF and XLS files, type in \"all17\" or \"all16\",")
    print("If you want a specific month and year,")
    dist_date = input("Please enter the distrituion month and year, (example 0117 for January 2017): ")
    
#    try:
    if ("all" in dist_date.lower()) and (len(dist_date) == 5):
        dist_date = dist_date[0:3].lower() + dist_date[-2:]
        # Retruning the dist_date as it is (all17 or all16 or all15)
        return dist_date
    
    elif ("all" not in dist_date.lower()):
        month = int(dist_date[0:2])
        year = int(dist_date[-2:]) + 2000
        
#        while (month > 12 or len(dist_date) != 4):
#            print("If you want the entire year of PDF and XLS files type in \"all17\" or \"all16\",")
#            print("If you want specific month and year,")
#            dist_date = input("Please enter the distrituion month and year, (example 0117 for January 2017): ")
#            month = int(dist_date[0:2])
#            year = int(dist_date[-2:]) + 2000
        
        if month < 10:
            month = "0" + str(month)
        else:
            month = str(month)
            
        dist_date = str(year) + "-" + month
        # return dist_date as a string like 2017-01
        return dist_date
        exit()
    
    else:
        print("You entered the wrong input!!!")
#    except:
#        pass
#        user_input()
    

def main():
# Most outter exception handling. Ensure the program runs
    try:
#     Prompt up Chrome webbroswer with login page
#     Only do this once
        driver.get(login_url)
        
    #     This block of the codes is actually doing the login
    # Once logged in all url's are good to download files
        username = driver.find_element_by_id("userId")
        password = driver.find_element_by_id("password")
        username.send_keys("brianfilips")
        password.send_keys("Suite82218%")
        login_attempt = driver.find_element_by_xpath("//*[@type='submit' and @name='btnSignon']")
        login_attempt.submit()
        
        # reference array to store the string for zipfile.ZipFile function to use
        # Other unzip function cannot access the dealname and folder directory within the try and except error handling
        zip_ref_list = []
        
        dist_date = user_input()
            
        for i in range(0, len(url)):
            try:  
                # Need to clean this up a bit
                session_object = requests.session()
                result = session_object.get(login_url)
                tree = html.fromstring(result.text)
                result = session_object.get(url[i], headers = dict(referer = url[i]))
                tree = html.fromstring(result.content)
                web_dealname = str(*tree.xpath("//*[@id=\"dochistory\"]/input[3]/@value"))
                file_name1 = str(*tree.xpath("//*[@id=\"dochistory\"]/input[2]/@value"))
                zip_file = file_name1 + "_" + web_dealname + "_reports.zip"
                
#                print("Web dealname is " + web_dealname)
#                print("Web file is " + file_name1)
        
                # Keeping the naming convention consistent. This will be used later for unzipping the files into correct folders
                if "AHMI" in file_name1:
                    # 20054 and 20072 deals file is going to mutiple places
                    if (int(web_dealname[-2:]) == 54) or (int(web_dealname[-2:]) == 72):                        
                        dealname = web_dealname[0:4] + "-" + web_dealname[4:]            
                    else:
                        dealname = "AHMIT" + web_dealname[-3:]
                
                # ALL HOMEBANC naming convention is HMB + LAST 2-DIGIT OF THE DEALNAME NAME
                elif "HOMEBANC" in file_name1:
                    dealname = "HMB" + web_dealname[-2:]
                    
                # For Carrington deals
                else:    
                    if web_dealname[-2:] == 'RT':
                        if len(web_dealname) == 8:
                            dealname = web_dealname[0:4] + "-" + web_dealname[4:6]
                        else:
                            dealname = web_dealname[0:4] + "-0" + web_dealname[4:5]
                    else:
                        if len(web_dealname) == 6:
                            dealname = web_dealname[0:4] + "-" + web_dealname[4:6]
                        else:
                            dealname = web_dealname[0:4] + "-0" + web_dealname[4:5]
                
#                print("New dealname is " + dealname)
                # Create a array. This will be put into zip_ref_list[] outside of the for loop
                lst = ["C:/Users/Shenghai.ETIDOMAIN/Downloads/" + zip_file, dealname]
                
                # Get each deal's web page
                driver.get(url[i])
                
                # searching for loop to find the user input dist_date and website dist_date

                for j in range(1, 30):
                    try:
                        day_el = driver.find_element_by_xpath("//*[@id='dochistory']/div/div/table/tbody/tr[" + str(j) + "]/td[2]")
                    except:
                        pass
                    else:
                        if ((day_el.text[0:2] == dist_date[-2:]) and (day_el.text[-4:] == dist_date[0:4])):
                            day = day_el.text
                
                # Distribution month and year can match up with user input,
                # but day could vary depends weekends and/or holidays
                
                
                # Only need pdf for homebanc and AHMIT deals
                if ("AHMI" in file_name1) or ("HOMEBANC" in file_name1):
                    dist_day = day[3:5]
                    checkbox1 = driver.find_element_by_xpath("//input[contains(@aria-label, 'Select cycle " + user_input().dist_date + "-" + dist_day + " and format PDF')]")
                    checkbox1.click()
                # To download the entire 2017 year
                elif "all" in dist_date:
                    checkbox1 = driver.find_element_by_xpath("//*[@id='" + "20" + dist_date[-2:] + "PDF']")
                    checkbox1.click()
                    checkbox2 = driver.find_element_by_xpath("//*[@id='" + "20" + dist_date[-2:] + "XLS']")
                    checkbox2.click()
                # Mostly for carrington SMLT deals
                else:  
                    dist_day = day[3:5]
                    checkbox1 = driver.find_element_by_xpath("//input[contains(@aria-label, 'Select cycle " + dist_date + "-" + dist_day + " and format PDF')]")
                    checkbox1.click()
                    checkbox2 = driver.find_element_by_xpath("//input[contains(@aria-label, 'Select cycle " + dist_date + "-" + dist_day + " and format XLS')]")
                    checkbox2.click()
        
                zip_download = driver.find_element_by_xpath("//*[@name='zip']")
                
                # if it is last file ensure download the file first before it closes out the browser
                if (i == (len(url) - 1)):
                    zip_download.click()
                    print("File " + zip_file + " downloaded")
                    time.sleep(1)
                    zip_ref_list.append(lst)
                elif((i == (len(url) - 1)) or ("all" in dist_date)):
                    zip_download.click()
                    print("File " + zip_file + " downloaded")
                    time.sleep(3)
                    print("Dowloading file(s) completed!!!")
                    zip_ref_list.append(lst)
                else:
                    zip_download.click()
                    print("File " + zip_file + " downloaded")
                    zip_ref_list.append(lst)

            
            except:
                print("SOMETHING WENT TERRIBLY WRONG IN FINDING THE LINK TO DOWNLOAD!!!")
                pass
            else:
                # If there is error, the correct list will useful for later when unzipping the files
                lst = ["C:/Users/Shenghai.ETIDOMAIN/Downloads/" + zip_file, dealname]
                driver.get(url[i])
                           
        # Only do this once. Close out the browser
        driver.close()
        
        # Unzip download files into prespective folders
        for k in range(0, len(zip_ref_list)):
            zip_ref = zipfile.ZipFile(str(zip_ref_list[k][0]), 'r')
            
            if ("AHMI" in zip_ref_list[k][1]) or ("2005-4" in zip_ref_list[k][1]) or ("2007-2" in zip_ref_list[k][1]):
                if "2005-4" in zip_ref_list[k][1]:
                    zip_ref.extractall("D:/deals/SMORI/AHMIT/" + str(zip_ref_list[k][1]) + "-I/stmts")
                    print("File is unzipped into " + "D:/deals/SMORI/AHMIT/" + str(zip_ref_list[k][1]) + "-I/stmts")
                    zip_ref.extractall("D:/deals/SMORI/AHMIT/" + str(zip_ref_list[k][1]) + "-II/stmts")
                    print("File is unzipped into " + "D:/deals/SMORI/AHMIT/" + str(zip_ref_list[k][1]) + "-II/stmts")
                    zip_ref.extractall("D:/deals/SMORI/AHMIT/" + str(zip_ref_list[k][1]) + "-III/stmts")
                    print("File is unzipped into " + "D:/deals/SMORI/AHMIT/" + str(zip_ref_list[k][1]) + "-III/stmts")
                    zip_ref.close()
                    os.remove(zip_ref_list[k][0])
                elif "2007-2" in zip_ref_list[k][1]:
                    zip_ref.extractall("D:/deals/SMORI/AHMIT/" + str(zip_ref_list[k][1]) + "/stmts")
                    print("File is unzipped into " + "D:/deals/SMORI/AHMIT/" + str(zip_ref_list[k][1]) + "/stmts")
                    zip_ref.extractall("D:/deals/SMORI/AHMIT/" + str(zip_ref_list[k][1]) + "-II/stmts")
                    print("File is unzipped into " + "D:/deals/SMORI/AHMIT/" + str(zip_ref_list[k][1]) + "-II/stmts")
                    zip_ref.close()  
                    os.remove(zip_ref_list[k][0])
                else:
                    zip_ref.extractall("D:/deals/SMORI/AHMIT/" + str(zip_ref_list[k][1]) + "/stmts")
                    print("File is unzipped into " + "D:/deals/SMORI/AHMIT/" + str(zip_ref_list[k][1]) + "/stmts")
                    zip_ref.close()
                    os.remove(zip_ref_list[k][0])
                    
            elif "HMB" in zip_ref_list[k][1]:
                zip_ref.extractall("D:/deals/HomeBanc_Mortgage_Trust/" + str(zip_ref_list[k][1]) + "/stmts")
                print("File is unzipped into " + "D:/deals/HomeBanc_Mortgage_Trust/" + str(zip_ref_list[k][1]) + "/stmts")
                zip_ref.close()
                os.remove(zip_ref_list[k][0])
                
            elif ("AHMI" not in zip_ref_list[k][1]) or ("HOMEBANC" not in zip_ref_list[k][1]):
                if "2015-01" in zip_ref_list[k][1]:
                    if "SMLT" in zip_ref_list[k][0]:
                        zip_ref.extractall("D:/deals/Carrington/SMAC/" + str(zip_ref_list[k][1]) + "-S" + "/stmts")
                        print("File is unzipped into " + "D:/deals/Carrington/SMAC/" + str(zip_ref_list[k][1]) + "-S" + "/stmts")
                        zip_ref.close()
                        os.remove(zip_ref_list[k][0])
                    elif "NMLT" in zip_ref_list[k][0]:
                        zip_ref.extractall("D:/deals/Carrington/SMAC/" + str(zip_ref_list[k][1]) + "-N" + "/stmts")
                        print("File is unzipped into " + "D:/deals/Carrington/SMAC/" + str(zip_ref_list[k][1]) + "-N" + "/stmts")
                        zip_ref.close()
                        os.remove(zip_ref_list[k][0])
                else:
                    zip_ref.extractall("D:/deals/Carrington/SMAC/" + str(zip_ref_list[k][1]) + "/stmts")
                    print("File is unzipped into " + "D:/deals/Carrington/SMAC/" + str(zip_ref_list[k][1]) + "/stmts")
                    zip_ref.close()
                    os.remove(zip_ref_list[k][0])

                               
    except:
        print("SOMETHING WENT TERRIBLY WRONG IN THE MOST OUTTER LAYER ERROR HANDLING!!!")
        pass
#    
if __name__ == '__main__':
    main()
    sys.exit()