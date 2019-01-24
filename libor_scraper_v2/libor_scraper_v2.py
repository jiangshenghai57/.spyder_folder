# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 12:02:29 2018

@author: Shenghai
cleaning up the previous libor scraper script

"""
import sys

from libor_scraper_misc_v2 import LiborScraper
        

if __name__ == '__main__':
    scraper = LiborScraper()
#    scraper.download_libor_csv()
    scraper.find_libor_csv()
    scraper.create_dbf()
    input("Press Enter to exit --->>>")
    sys.exit()