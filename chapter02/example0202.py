#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# Project Name: python4desktop - Created Date: Thursday September 17th 2020
# Author: loitd - Email: loitranduc@gmail.com
# Description: A downloader without GUI
# Copyright (c) 2020 loitd. WWW: https://github.com/loitd
# -----
# Last Modified: Thursday September 17th 2020 10:14:57 pm By: loitd
# -----
# HISTORY:
# Date      	By    	Comments
# ----------	------	----------------------------------------------------------
# 2020-09-17	loitd	Initialized
###
import requests, shutil, threading, os, time
from lutils.utils import printlog, printwait

url = "https://file-examples-com.github.io/uploads/2017/11/file_example_MP3_1MG.mp3"
filename = "file_example_MP3_1MG.mp3"
lk = threading.Lock()

def download(url, filename):
    lk.acquire()
    filename = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        filesize = r.headers['Content-length'].encode("utf8")
        printlog("Start download {0} kilobytes".format(filesize))
        with open(filename+".tmp", 'wb') as fh:
            fh.write(filesize)
        with open(filename, 'wb') as f:
            lk.release()
            shutil.copyfileobj(r.raw, f)
    return filename, filesize

def percentage(filename):
    lk.acquire()
    with open(filename+".tmp", "rb") as fh:
        filesize = fh.read()
        filesize = int(filesize)
        printlog("Got filesize = {0}".format(filesize))
    os.remove(filename+".tmp")
    while 1:
        thesize = os.stat(filename).st_size
        if thesize == filesize:
            printlog("Download finished")
            lk.release()
            break 
        else:
            printwait("{0}/{1} - Percentage: {2:.2f}%".format(thesize, filesize, (thesize * 100 / filesize)), 1)

if __name__ == "__main__":
    dld = threading.Thread(name="Dlder", target=download, daemon=True, args=(url, filename))
    dld.start()
    percentage(filename)
    # Join the downloader thread
    dld.join()