# -*- coding: utf-8 -*-


"""
Spyder Editor

This is a temporary script file.
"""
"""
Web Scrapper to grab the Remit Statements from Wells Fargo's website
Following Codes include login information and possibly matching the deal name and deal folder directories
"""

import requests
from lxml import html

USERNAME = "brianfilips"
PASSWORD = "Suite82218$"


LOGIN_URL = "https://www.ctslink.com/a/welcome.html"
URL = "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=201323&doc=SMLT_201323_RMT"

def main():
    session_requests = requests.session()
    
    # distribution date will be used later for userInput
    # distDate = input()

    # Get login form validation token 
    result = session_requests.get(LOGIN_URL)
    tree = html.fromstring(result.text)
    authenticity_token = list(set(tree.xpath("//input[@name='form.validation.token']/@value")))[0]

    # Create payload, this is the login info
    payload = {
        "username": USERNAME, 
        "password": PASSWORD, 
        "form.validation.token": authenticity_token
    }

    # Perform login
    result = session_requests.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))

    # Scrape url
    result = session_requests.get(URL, headers = dict(referer = URL))
    print(result.ok)
    print(result.status_code)
    tree = html.fromstring(result.content)
    dealname = str(*tree.xpath("//*[@id=\"dochistory\"]/input[3]/@value"))
    dealname = dealname[0:4] + "-" + dealname[-2:]
    print("Deal folder is " + dealname)
        
    bucket_names = tree.xpath("//*[@id=\"contentBody\"]/div[1]/span/text()")
    print(bucket_names)
    
    tab_name = tree.xpath("//*[@id=\"seriesTabs\"]/a[1]/text()")
    print(tab_name)
    
    test = tree.xpath("//a[@href = '/a/seriesdocs.html?shelfId=SMLT&seriesId=201323&tab=DEALDOCS']")
    print(test)
    
    test = tree.xpath("//*[contains(@type, 'submit')]")
    print(test)
    
    test = tree.xpath("//*[contains(text(), '11/15/2017')]")
    print(test)
    
    distDate = tree.xpath("//*[@id=\"dochistory\"]/div/div/table/tbody/tr[2]/td[1]/text()")
    print(distDate)
    
    
if __name__ == '__main__':
    main()