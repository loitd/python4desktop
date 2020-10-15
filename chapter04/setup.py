#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# -------------------------------------
# File: chapter04\setup.py
# Description: This is a short description
# Author: loitd - WWW: https://github.com/loitd
# ----------
# HISTORY:
# Date      	By    	Comments
# ----------	------	---------------
# 2020-10-09	loitd	Initialized
# -------------------------------------

# Official guide
# https://cx-freeze.readthedocs.io/en/latest/distutils.html
import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "packages": ["sys"], 
    "excludes": ["tkinter"], 
    "include_files": ['py4de.ico',],
    'include_msvcr': True,
    "optimize": 2
}

bdist_msi_options = {
    'add_to_path': True
}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  
    name = "example0401",
    version = "0.1",
    description = "Py4De Chapter 04 example",
    options = {
        "build_exe": build_exe_options,
        "install_exe": {},
        "bdist_msi": bdist_msi_options
    },
    executables = [Executable("example0401.py", base=base)]
)