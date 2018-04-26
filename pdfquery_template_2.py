# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 15:29:14 2018

@author: Shenghai
"""

"""
Load up the file first, find out the in_box location of the data, then cache it. It'll run faster
"""

from pdfquery.cache import FileCache
import pdfquery
import sys

def pdf_scrub():
    pdf = pdfquery.PDFQuery("D:\\deals\\Carrington\\SMAC\\2013-23\\Reports\\SMLT1323-16-Binder.pdf")
 
    pdf.load(2)    
    
    label2 = pdf.pq('LTTextLineHorizontal:contains(" see instructions for other forms the REMIC may have")')
    
    left_corner = float(label2.attr('x0'))
    bottom_corner = float(label2.attr('y0'))
    form = pdf.pq('LTTextLineHorizontal:in_bbox("%s, %s, %s, %s")' % (left_corner, bottom_corner-30, left_corner+150, bottom_corner)).text()
    
    print(left_corner)
    print(bottom_corner)
    print(left_corner)
    print(bottom_corner)
    
    print(form + "stop")
    
    print(type(form))
    
    label = pdf.pq('LTTextLineHorizontal:contains("cols. (a) through (f)")')
    
    left_corner = float(label.attr('x0'))
    bottom_corner = float(label.attr('y0'))
    cap_acct = pdf.pq('LTTextLineHorizontal:in_bbox("%s, %s, %s, %s")' % (left_corner, bottom_corner-30, left_corner+150, bottom_corner)).text()

    print(left_corner)
    print(bottom_corner-30)
    print(left_corner+150)
    print(bottom_corner)
    
    cap_acct = round(float(cap_acct.replace(",", "")), 2)
    
    print(cap_acct)
    
    print(type(cap_acct))
    
  

    pdf.extract(['Capital Acct: ', 'in_bbox("507.414, 33.03, 657.414, 63.03")'])

if __name__ == '__main__':
    pdf_scrub()
    sys.exit()