# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 11:37:33 2018

@author: Shenghai
"""

"""
Potential template py script for scraping and reading PDF
GitHub example website: https://github.com/mstamy2/PyPDF2/blob/master/Sample_Code/basic_features.py
This template script contains PdfFileWriter megePage function
"""
import sys
from PyPDF2 import PdfFileReader as pdfr
from PyPDF2 import PdfFileWriter as pdfw

def scrape_pdf():
    output = pdfw()
    input1 = pdfr(open("D:\\deals\\Carrington\\SMAC\\2013-23\\Reports\\SMLT1323-16-Binder.pdf", 'rb'))
    
    print("SMLT1323-16-Binder.pdf has %d pages." % input1.getNumPages())
    
    output.addPage(input1.getPage(0))
    
    output.addPage(input1.getPage(1).rotateClockwise(90))
    
    output.addPage(input1.getPage(2).rotateCounterClockwise(90))
    
    merger_file = input1.getPage(4)
    merger_file.mergePage(input1.getPage(1))
    
    output.addPage(merger_file)
    
    outputStream = open('D:\\deals\\Carrington\\SMAC\\2013-23\\Reports\\PyPDF2-output.pdf', 'wb')
    output.write(outputStream)

if __name__ == '__main__':
    scrape_pdf()
    sys.exit()