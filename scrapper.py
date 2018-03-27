# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 11:58:22 2017

@author: Shenghai
"""

# imported the requests library
import requests
image_url = "https://www.ctslink.com/a/welcome.html?TYPE=33554433&REALMOID=06-0001db9f-d296-135e-8965-8cd9a78f208d&GUID=&SMAUTHREASON=0&METHOD=GET&SMAGENTNAME=-SM-D4WL7bIJRrs9Tf9CX1FdyXStqgRzkMfLgle7ZhPTEhzWE7bQ%2bZ7b84aSMgXJqhLbNQbaLkXFeg%2f4hNNsNPKN%2fYYX0tuX1r4htCaBLtqswPijMbGOSqJKr5y9tm3IciXe&TARGET=-SM-HTTPS%3a%2f%2fwww%2ectslink%2ecom%2f"
 
# URL of the image to be downloaded is defined as image_url
r = requests.get(image_url) # create HTTP response object
 
# send a HTTP request to the server and save
# the HTTP response in a response object called r
with open("python_logo.png",'wb') as f:
 
    # Saving received content as a png file in
    # binary format
 
    # write the contents of the response (r.content)
    # to a new file in binary mode.
    f.write(r.content)