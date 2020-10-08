#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# Project Name: chapter03 - Created Date: Saturday September 26th 2020
# Author: loitd - Email: loitranduc@gmail.com
# Description: This is a short project/file description
# Copyright (c) 2020 loitd. WWW: https://github.com/loitd
# -----
# Last Modified: Saturday September 26th 2020 9:32:29 pm By: loitd
# -----
# HISTORY:
# Date      	By    	Comments
# ----------	------	----------------------------------------------------------
# 2020-09-26	loitd	Initialized
# 2020-09-27    loitd   https://kivy.org/doc/stable/api-kivy.core.audio.html#kivy.core.audio.SoundLoader.load
###

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.core.audio import SoundLoader
from kivy.config import Config
from kivy.uix.widget import Widget

class RBoxWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(RBoxWidget, self).__init__(**kwargs)

class GUI0302(BoxLayout):
    def __init__(self, **kwargs):
        super(GUI0302, self).__init__(**kwargs)

class Example0302App(App):
    def build(self):
        self.icon = 'py4de.png'
        self.title = 'Python4Desktop Music Player Example 0302'
        return GUI0302()
    
    def on_press_button(self):
        print("Button is pressed")
        sound = SoundLoader.load('test.mp3')
        if sound:
            sound.play()
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)

if __name__ == '__main__':
    app = Example0302App()
    app.run()