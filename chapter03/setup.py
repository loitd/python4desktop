#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# Project Name: PythonImageViewer - Created Date: Wednesday September 23rd 2020
# Author: loitd - Email: loitranduc@gmail.com
# Description: This is a short project/file description
# Copyright (c) 2020 loitd. WWW: https://github.com/loitd
# -----
# Last Modified: Wednesday September 23rd 2020 9:49:10 pm By: loitd
# -----
# HISTORY:
# Date      	By    	Comments
# ----------	------	----------------------------------------------------------
# 2020-09-23	loitd	Initialized
###

# Official guide
# https://cx-freeze.readthedocs.io/en/latest/distutils.html
import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "packages": ["sys"], 
    "excludes": [""], 
    "include_files": ['py4de.png',],
    'include_msvcr': True,
    "optimize": 2
}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  
    name = "piv",
    version = "0.1",
    description = "My GUI application!",
    options = {
        "build_exe": build_exe_options,
        "install_exe": {},
        "bdist_msi": {}
    },
    executables = [Executable("example0303.py", base=base)]
)