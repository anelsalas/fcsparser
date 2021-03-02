# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 16:16:14 2019

@author: ASALAS
"""

import sys
sys.setrecursionlimit(15000) # 10000 is an example, try with different values


import tkinter as tkshitt 
from tkinter import Tk #as Tkk
#from tkinter import BooleanVar #,frame
from tkinter import ttk as ttk
from tkinter import scrolledtext
#from tkinter import Checkbutton
from tkinter import filedialog

import fcsparser # can put immediatly into a pandas dataframe
import numpy
#import myfcsparsergui

#import CommandsDict

import datetime

def timeStamped(fname, fmt='%Y-%m-%d-%H-%M-%S_{fname}'):
    return datetime.datetime.now().strftime(fmt).format(fname=fname)

class mytkgui:
    def __init__(self):
        self.window = Tk()  

        #echo button objects
        self.BtnBrowseFileText = tkshitt.StringVar()        
        self.BtnBrowseFile = ttk.Button(self.window,
                                 textvariable = self.BtnBrowseFileText,
                                 command = self.BtnBrowseFunction) 
        self.BtnConvertToCSVText = tkshitt.StringVar()        
        self.BtnConvertToCSV = ttk.Button(self.window,
                                 textvariable = self.BtnConvertToCSVText,
                                 command = self.BtnConvertToCSVTextFunction) 
        
        self.fcsFileName = ""
        self.logtxt = scrolledtext.ScrolledText(self.window,width=100,height=15)
        self.largeFileData = None
        self.metaDataDictionary = None
        
        self.InitWindow()

    def BtnConvertToCSVTextFunction(self):
        newcvsFile = filedialog.asksaveasfilename (initialdir = "./",
                                            title = "Save as CSV",
                                            filetypes = (
                                                    ("Comma Separated Values File","*.csv"),
                                                    ("all files","*.*")
                                            ))
        
        numpy.savetxt(newcvsFile,self.largeFileData,delimiter=",")
        
    def BtnBrowseFunction(self):
        self.fcsFileName = filedialog.askopenfilename(initialdir = "./",
                                            title = "Select file",
                                            filetypes = (
                                                    ("Aquios List Files","*.lmd"),
                                                    ("Flow Cytometry Standard files","*.fcs"), 
                                                    ("all files","*.*")
                                             ))
        path = self.fcsFileName 
        self.logtxt.insert(tkshitt.END,"File: " + path +"\r\n")
        
        # fcsparser.parse Returns:
        #    -------
        #    if meta_data_only is True:
        #        meta_data: dict
        #            Contains a dictionary with the meta data information
        #    Otherwise:
        #        a 2-tuple with
        #            the first element the meta_data (dictionary)
        #            the second element the data (in either DataFrame or numpy format)  
        try:
            
            self.metaDataDictionary, self.largeFileData= fcsparser.parse(path,
                                                                         meta_data_only=False,
                                                                         reformat_meta=True)#,
                                                                         #channel_naming=channel_naming)
        except (ValueError) as e: 
                
            self.logtxt.insert(tkshitt.END,str(e)+"\r\n")
            return
            
        self.logtxt.insert(tkshitt.END,self.metaDataDictionary)
        self.logtxt.insert(tkshitt.END,self.largeFileData)
        
        #numpy.savetxt("cytometerdata.csv",data,delimiter=",")
        #print  (meta)
        #print (data)
        
        #scatter(data['Time'], alpha=0.8, color='gray')        
        
    def InitWindow(self):
        self.window.title("Flow Cytometry Standard File Parser and Converter")
        self.BtnBrowseFileText.set("Select file")
        self.BtnConvertToCSVText.set("Convert To CSV File")
        self.window.geometry('900x400')
        #row 0
        self.BtnBrowseFile.grid(column=0, row=0)
        self.logtxt.grid(column=0,row=1)
        self.BtnConvertToCSV.grid(column=0,row=2)
        
        
        
        