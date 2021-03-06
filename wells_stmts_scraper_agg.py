import requests
from lxml import html
from selenium import webdriver as wd
import time
import zipfile
import os
import sys

# Using latest chromedriver.exe to avoid exception errors,
# Also be careful where to place the .exe file, script may not know where the chromedriver.exe is
driver = wd.Chrome()

login_url = "http://www.ctslink.com"

# Each link to individual deal's download webpage
# Carrington deals have to links, one is RT stmts, the other is non-RT
url = [
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
        "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20179&doc=SMLT_20179_RMT",
        "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20179RT&doc=SMLT_20179RT_RMT",
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
        "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20181&doc=SMLT_20181_RMT",
        "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20181RT&doc=SMLT_20181RT_RMT",
        "https://www.ctslink.com/a/history.html?shelfId=UMAC&seriesId=201831&doc=UMAC_201831_RMT",
        "https://www.ctslink.com/a/history.html?shelfId=UMAC&seriesId=201831RT&doc=UMAC_201831RT_RMT",
        "https://www.ctslink.com/a/history.html?shelfId=UMAC&seriesId=201832&doc=UMAC_201832_RMT",
        "https://www.ctslink.com/a/history.html?shelfId=UMAC&seriesId=201832RT&doc=UMAC_201832RT_RMT",
        "https://www.ctslink.com/a/history.html?shelfId=UMAC&seriesId=201833&doc=UMAC_201833_RMT",
        "https://www.ctslink.com/a/history.html?shelfId=UMAC&seriesId=201833RT&doc=UMAC_201833RT_RMT",
        "https://www.ctslink.com/a/history.html?shelfId=UMAC&seriesId=201834&doc=UMAC_201834_RMT",
        "https://www.ctslink.com/a/history.html?shelfId=UMAC&seriesId=201834RT&doc=UMAC_201834RT_RMT",

       # Shenghai's deal list
       "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20143&doc=SMLT_20143_RMT",
       "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20143RT&doc=SMLT_20143RT_RMT",
       "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20145&doc=SMLT_20145_RMT",
       "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20145RT&doc=SMLT_20145RT_RMT",
       "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20151&doc=SMLT_20151_RMT",
       "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20151RT&doc=SMLT_20151RT_RMT",
       "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20158&doc=SMLT_20158_RMT",
       "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20158RT&doc=SMLT_20158RT_RMT",
       "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20159&doc=SMLT_20159_RMT",
       "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20159RT&doc=SMLT_20159RT_RMT",
       "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20161&doc=SMLT_20161_RMT",
       "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20161RT&doc=SMLT_20161RT_RMT",
       "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20164&doc=SMLT_20164_RMT",
       "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20164RT&doc=SMLT_20164RT_RMT",
       "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=201621&doc=SMLT_201621_RMT",
       "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=201621RT&doc=SMLT_201621RT_RMT",
       "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=201623&doc=SMLT_201623_RMT",
       "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=201623RT&doc=SMLT_201623RT_RMT",
       "https://www.ctslink.com/a/history.html?shelfId=UMAC&seriesId=201631&doc=UMAC_201631_RMT",
       "https://www.ctslink.com/a/history.html?shelfId=UMAC&seriesId=201631RT&doc=UMAC_201631RT_RMT",
       "https://www.ctslink.com/a/history.html?shelfId=UMAC&seriesId=201632&doc=UMAC_201632_RMT",
       "https://www.ctslink.com/a/history.html?shelfId=UMAC&seriesId=201632RT&doc=UMAC_201632RT_RMT",
    ]

###############################################################################

def user_input():
	# Asking user for month and year input
    # This chunck of codes will give the string info for what period of files to download
    # More features could be add in to ask users

    while True:
        print("If you want the entire year of PDF and XLS files, type in \"all17\" or \"all16\", for year 2017 and 2016 respectively")
        print("If you want a specific month and year,")
        dist_date = input("Please enter the distrituion month and year, (example 0117 for January 2017): ")
        try:
            if ('all' in dist_date.lower()) and ('all' in dist_date[0:3]) and (len(dist_date) == 5):
                dist_date = "{}{}".format(dist_date[0:3].lower(), dist_date[-2:])
                break
            elif ('all' not in dist_date.lower()) and (len(dist_date) == 4) and (int(dist_date[0:2]) >= 1 or int(dist_date[0:2]) <= 12):
                month = dist_date[0:2]
                year = int(dist_date[-2:]) + 2000
                dist_date = "{}-{}".format(str(year), month)
                break
            else:
                print("You done messed up A-A-RON!!!")
                continue
        except:
            print("Let's try this again.")
            pass

    return dist_date

###############################################################################


def wells_scraper():
    # Very first outter exception handling. Ensure if script cannot find the link to download, go to the link
#    try:
        # Open the wells website with chrome driver
        driver.get(login_url)
        username = driver.find_element_by_id("user_id")
        password = driver.find_element_by_id("password")
        username.send_keys("brianfilips")
        password.send_keys("Suite82219^")
        login_attempt = driver.find_element_by_xpath("//*[@id='loginButton']")
        login_attempt.click()

        zip_ref_list = []

        dist_date = user_input()

        for link in url:
            try:
                # Need to clean this up a bit
                session_object = requests.session()
                result = session_object.get(login_url)
                tree = html.fromstring(result.text)
                result = session_object.get(link, headers = dict(referer = link))
                tree = html.fromstring(result.content)
                web_dealname = str(*tree.xpath("//*[@id=\"dochistory\"]/input[3]/@value"))
                file_name1 = str(*tree.xpath("//*[@id=\"dochistory\"]/input[2]/@value"))
                zip_file = file_name1 + "_" + web_dealname + "_reports.zip"

                # Keeping the naming convention consistent. This will be used later for unzipping the files into correct folders
                if "AHMI" in file_name1:
                    # 20054 and 20072 deals file is going to mutiple places
                    if (int(web_dealname[-2:]) == 54) or (int(web_dealname[-2:]) == 72):
                        dealname = "{}-{}".format(web_dealname[0:4], web_dealname[4:])
                    else:
                        dealname = "AHMIT{}".format(web_dealname[-3:])

                # ALL HOMEBANC naming convention is HMB + LAST 2-DIGIT OF THE DEALNAME NAME
                elif "HOMEBANC" in file_name1:
                    dealname = "HMB{}".format(web_dealname[-2:])

                # For Carrington deals
                else:
                    if web_dealname[-2:] == 'RT':
                        if len(web_dealname) == 8:
                            dealname = "{}-{}".format(web_dealname[0:4], web_dealname[4:6])
                        else:
                            dealname = "{}-0{}".format(web_dealname[0:4], web_dealname[4:5])
                    else:
                        if len(web_dealname) == 6:
                            dealname = web_dealname[0:4] + "-" + web_dealname[4:6]
                        else:
                            dealname = web_dealname[0:4] + "-0" + web_dealname[4:5]

                # Create a array. This will be put into zip_ref_list[] outside of the for loop
                lst = ["C:/Users/Shenghai.ETIDOMAIN/Downloads/" + zip_file, dealname]

                # Get each deal's web page
                driver.get(link)

                # searching for loop to find the user input dist_date and website dist_date
                # //*[@id="dochistory"]/div/div/table/tbody/tr[3]/td[2]
                for j in range(1, 30):
                    try:
                        day_el = driver.find_element_by_xpath("//*[@id='dochistory']/div/div/table/tbody/tr[" + str(j) + "]/td[2]")
                    except:
                        pass
                    else:
                        if ((day_el.text[0:2] == dist_date[-2:]) and (day_el.text[-4:] == dist_date[0:4])):
                            day = day_el.text
                            break

                # Distribution month and year can match up with user input,
                # but day could vary depends weekends and/or holidays
                # //*[@id="chk_2018PDF0"]

                # Only need pdf for homebanc and AHMIT deals
                if ("AHMI" in file_name1) or ("HOMEBANC" in file_name1):
                    dist_day = day[3:5]
                    checkbox1 = driver.find_element_by_xpath("//input[contains(@aria-label, 'Select cycle " + dist_date + "-" + dist_day + " and format PDF')]")
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
                if (url.index(link) == (len(url) - 1)):
                    zip_download.click()
                    print("File " + zip_file + " downloaded")
                    time.sleep(1)
                    zip_ref_list.append(lst)
                elif(url.index(link) == (len(url) - 1)):
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
                driver.get(link)

        # Only do this once. Close out the browser
        driver.close()

        # Unzip download files into prespective folders
        for k in range(0, len(zip_ref_list)):
            zip_ref = zipfile.ZipFile(str(zip_ref_list[k][0]), 'r')

            if ("AHMI" in zip_ref_list[k][1]) or ("2005-4" in zip_ref_list[k][1]) or ("2007-2" in zip_ref_list[k][1]):
                pass

            elif "HMB" in zip_ref_list[k][1]:
                pass

            elif ("AHMI" not in zip_ref_list[k][1]) or ("HOMEBANC" not in zip_ref_list[k][1]):
                zip_ref.extractall("D:/deals/Carrington/aggdata/stmts/" + str(zip_ref_list[k][1]))
                print("File is unzipped into " + "D:/deals/Carrington/aggdata/stmts/" + str(zip_ref_list[k][1]))
                zip_ref.close()
                os.remove(zip_ref_list[k][0])

#    except:
#        print("SOMETHING WENT WRONG IN THE FIRST OUTER LAYER ERROR HANDLING")
#        pass

###############################################################################

if __name__ == '__main__':
    wells_scraper()
    input("Press Enter to exit >>>")
    sys.exit()
