# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 15:29:14 2018

@author: Shenghai
"""

from pdfquery.cache import FileCache
import pdfquery
import sys

def pdf_scrub():
    pdf = pdfquery.PDFQuery("D:\\deals\\Carrington\\SMAC\\2013-23\\Reports\\SMLT1323-16-Binder.pdf",
                            parse_tree_cacher=FileCache("/tmp/"))
 
    label = pdf.pq('LTTextLineHorizontal:contains("cols. (a) through (f)")')
    
    left_corner = float(label.attr('x0'))
    bottom_corner = float(label.attr('y0'))
    cap_acct = pdf.pq('LTTextLineHorizontal:in_bbox("%s, %s, %s, %s")' % (left_corner, bottom_corner-30, left_corner+150, bottom_corner)).text()

    print(cap_acct)
    
    cap_acct = round(float(cap_acct.replace(",", "")), 2)
    
    print(cap_acct)
    
    print(type(cap_acct))

if __name__ == '__main__':
    pdf_scrub()
    sys.exit()