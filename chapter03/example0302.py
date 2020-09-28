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
from kivy.core.audio import SoundLoader
from kivy.config import Config

class Example0302App(App):
    def build(self):
        self.icon = 'py4de.png'
        self.title = 'Python4Desktop Music Player'
        layout = BoxLayout(padding=10)
        label = Label()
        button = Button()
        layout.add_widget(label)
        layout.add_widget(button)
        return layout
    
    def on_press_button(self):
        print("Button is pressed")
        sound = SoundLoader.load('python4desktop.mp3')
        if sound:
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)
            sound.play()

if __name__ == '__main__':
    app = Example0302App()
    app.run()