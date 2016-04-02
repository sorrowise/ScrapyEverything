# -*- coding: utf-8 -*-

"""
Script Name: net.py
Author:      LURUI
Created		: 31 March 2016
Version		: 1.0
Description	: This simple script is created in order to pack the functions I commonly use to write the web program.

"""

import urllib2 as ul
from urllib2 import HTTPError
from bs4 import BeautifulSoup
from algo import findAll
import os

def getBS(url):
    try:
        html = ul.urlopen(url)
    except HTTPError as e:
        print e
    else:
        bs = BeautifulSoup(html,'lxml')
    return bs

def makeFolder(path):
    if os.path.exists(path) == False:
        os.makedirs(path)

def download(link,path):
    try:
        html = ul.urlopen(link)
    except HTTPError as e:
        print e
    else:
        content = html.read()
        fileNameLoc = findAll(link,'/')[-1]
        with open(path+link[fileNameLoc+1:],'wb') as code:
            code.write(content)
