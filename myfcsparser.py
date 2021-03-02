# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 16:59:24 2019

@author: ASALAS
HAMILTONLISTMODE.lmd
"""

import fcsparser
import numpy
import myfcsparsergui


def main():  
   
    stwosgui = myfcsparsergui.mytkgui()

    stwosgui.window.mainloop()
    
    

if __name__ == "__main__":
   main()     


#scatter(data['Time'], alpha=0.8, color='gray')
