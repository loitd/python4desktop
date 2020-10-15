#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# -------------------------------------
# File: chapter01\example0101.py
# Description: This is a short description
# Author: loitd - WWW: https://github.com/loitd
# ----------
# HISTORY:
# Date      	By    	Comments
# ----------	------	---------------
# 2020-09-16	loitd	Initialized
# -------------------------------------

import datetime, os, sys, platform

def hello():
    print("Hello, this is Python version", sys.version, "\nRunning on", platform.system(), platform.release(), "\nNow is", datetime.datetime.now())

if __name__ == "__main__":
    hello()
    