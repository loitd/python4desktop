#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# Project Name: python4desktop - Created Date: Wednesday September 16th 2020
# Author: loitd - Email: loitranduc@gmail.com
# Description: This is a short project/file description
# Copyright (c) 2020 loitd. WWW: https://github.com/loitd
# -----
# Last Modified: Wednesday September 16th 2020 10:20:27 am By: loitd
# -----
# HISTORY:
# Date      	By    	Comments
# ----------	------	----------------------------------------------------------
# 2020-09-16	loitd	Initialized
###
import datetime, os, sys, platform

def hello():
    print("Hello, this is Python version", sys.version, "\nRunning on", platform.system(), platform.release(), "\nNow is", datetime.datetime.now())

if __name__ == "__main__":
    hello()