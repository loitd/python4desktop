#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# Project Name: chapter04 - Created Date: Tuesday October 6th 2020
# Author: loitd - Email: loitranduc@gmail.com
# Description: This is a example of Python For Desktop book
# Copyright (c) 2020 loitd. WWW: https://github.com/loitd
# -----
# Last Modified: Tuesday October 6th 2020 2:38:40 pm By: loitd
# -----
# HISTORY:
# Date      	By    	Comments
# ----------	------	----------------------------------------------------------
# 2020-10-06	loitd	Initialized
###

# First things, first. Import the wxPython package.
import wx

# Next, create an application object.
app = wx.App()

# Then a frame.
frm = wx.Frame(None, title="Hello World")

# Show it.
frm.Show()

# Start the event loop.
app.MainLoop()