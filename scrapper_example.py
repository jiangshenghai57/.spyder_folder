# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 14:45:36 2017

@author: Shenghai
"""

# this is a example from the internet

payload  = {
        "userID": "jiangshenghai57",
        "passwo
        #"csrfmiddlewaretoken": "COWzq1OIO5uTCkuBp4Ouu9yfxMubXCiy5cLpjVpooDhAQJgMG1OFNBBk6J1UaFed"
}

import requests 
from lxml import html

# create a session object
session_requests = requests.session()

login_url = "https://en.wikipedia.org/wiki/List_of_Olympic_medalists_in_judo"
result = session_requests.get(login_url)

tree = html.fromstring(result.text)
#authenticity_token = list(set(tree.xpath("//input[@name='csrfmiddlewaretoken']/@value")))[0]

# Perform the login phase
result = session_requests.post(
        login_url,
        data = payload,
        headers = dict(refereer=login_url)
)

url = 'https://en.wikipedia.org/wiki/List_of_Olympic_medalists_in_judo'
result = session_requests.get (
        url,
        headers = dict(referer = url)
)

tree = html.fromstring(result.content)
bucket_names = tree.xpath("//*[@id='Middleweight']/text()")
print(bucket_names)

result.ok
result.status_code