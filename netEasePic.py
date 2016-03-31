# -*- coding: utf-8 -*-

"""
Script Name: netEasePic.py
Author:      LURUI
Created		: 31st March 2016
Version		: 1.0
Description	: This simple script to download the photos belong to my favourite photographers in netEase Photo.

"""

import urllib2 as ul
from urllib2 import HTTPError
from bs4 import BeautifulSoup
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

def download(link,path,fileNameLoc):
    try:
        html = ul.urlopen(link)
    except HTTPError as e:
        print e
    else:
        content = html.read()
        with open(path+link[fileNameLoc:],'wb') as code:
            code.write(content)

def downloadPhoto(bs,author,pageIndex,path):
    girl = bs.findAll('img',{"class":"z-tag data-lazyload-src"})
    for img in girl:
        link = img.get('data-lazyload-src')
        savePath = path+author+'/'+str(pageIndex)+'/'
        fileNameLoc = -15
        download(link,savePath,fileNameLoc)   

def getNextID(soup):
    content = soup.get_text()
    loc = content.find('window.NEXTID')
    end = loc+16
    num = 0
    while True:
        if content[end+num] == ';':
            break
        else:
            num = num + 1
    nextID = content[end:end+num]
    return nextID

def getAuthor(beginPage,path):
    bs = getBS(beginPage)
    title = bs.title.get_text()
    byLoc = title.find('by')
    author = unicode(title[byLoc+2:])
    savePath = path+author+'/'
    makeFolder(savePath)
    return author

def netEasePic(beginPage):
    pageIndex = 1
    page = beginPage
    ppLoc = page.find('pp/')
    author = getAuthor(page,path)
    while True:
        soup = getBS(page)
        savePath = path+author+'/'+str(pageIndex)+'/'
        makeFolder(savePath)
        downloadPhoto(soup,author,pageIndex,path)
        print 'the %s page is being downloaded!' %(pageIndex)
        pageIndex = pageIndex + 1
        nextID = getNextID(soup)
        if nextID == '0':
            print 'this is the last page, downloading completed!'
            break
        else:
            page = page[:ppLoc+3]+nextID+'.html'

if __name__ == "__main__":
    beginPage = input('please enter the first page:\n')
    path = input('please input the path your want to save your image:\n')
    netEasePic(beginPage)
    raw_input('press any key to exit!')