#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# Project Name: chapter03 - Created Date: Monday September 28th 2020
# Author: loitd - Email: loitranduc@gmail.com
# Description: This is a music player by Python
# Copyright (c) 2020 loitd. WWW: https://github.com/loitd
# -----
# Last Modified: Monday September 28th 2020 1:03:49 am By: loitd
# -----
# HISTORY:
# Date      	By    	Comments
# ----------	------	----------------------------------------------------------
# 2020-09-28	loitd	Initialized
###

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.core.audio import SoundLoader
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.popup import Popup
import os

kivy.require('1.10.0') #restrict kivy version

def init():
    # Config.set('graphics','borderless',1)
    # Config.set('graphics','resizable',0)
    Window.size = (450,350)
    # Window.borderless = True
    Window.clearcolor = (1, 0, 1, 1)
    Window.clear()

class FileChooserPopup(Popup):
    def __init__(self, **kwargs):
        super(FileChooserPopup, self).__init__(**kwargs)
        print("FileChooserPopup initialized")

    def selected(self, *args):
        print(args)
        self.dismiss()

class FileChooserWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(FileChooserWidget, self).__init__(**kwargs)
        print("FileChooserWidget initialized")
        self.fcpopup = FileChooserPopup()
        self.fcpopup.open()
    
    def close(self):
        self.fcpopup.dismiss()

class MusicPlayerApp(App):
    def build(self):
        self.icon = 'py4de.png'
        self.title = 'Python4Desktop Music Player'
        self.playingfile = 'python4desktop.mp3'
        self.sound = None
        layout = BoxLayout(padding=1, orientation='vertical')
        
        hbox = BoxLayout(orientation='vertical', size_hint=(1, None), height=32)
        self.lbl1 = Label(text="Press Play to play {0}".format(self.playingfile))
        hbox.add_widget(self.lbl1)
        layout.add_widget(hbox)
        
        buttons = [['Open', 'Play', 'Stop', 'Exit']]
        for row in buttons:
            hbox = BoxLayout(orientation='horizontal', size_hint=(1, None), height=48)
            for b in row:
                button = Button(text=b)
                button.bind(on_press=self.on_press_button)
                hbox.add_widget(button)
            layout.add_widget(hbox)
        return layout

    def on_newfileopen(self, *args):
        print(args)
        self.fcwidget.close()
        filepath = args[1][0]
        filename, fileext = os.path.splitext(filepath)
        if fileext in ['mp3', 'wav']:
            self.playingfile = filepath
            self.lbl1.text="Playing {0}".format(self.playingfile)
            print(self.playingfile)
            self.playmusic()
        else:
            self.lbl1.text = "File extension not match. Keep playing {0}".format(self.playingfile)
        
    
    def on_press_button(self, instance):
        print("Button is pressed", instance.text)
        if instance.text == 'Exit':
            Window.close()
        elif instance.text == 'Open':
            self.fcwidget = FileChooserWidget()
        elif instance.text == 'Play':
            # instance.disabled = 1
            self.playmusic()
        elif instance.text == 'Stop':
            self.stopmusic()
        
    def playmusic(self):
        try:
            if self.sound:
                self.sound.stop()
                self.sound.unload()
            self.sound = SoundLoader.load(self.playingfile)
            self.sound.play()
            self.lbl1.text = "Playing {0}".format(self.playingfile)
        except Exception as e:
            self.lbl1.text = "Error while playing {0}".format(self.playingfile)

    def stopmusic(self):
        try:
            if self.sound:
                self.sound.stop()
                # self.sound.unload()
                self.lbl1.text = "{0} stopped".format(self.playingfile)
        except Exception as e:
            self.lbl1.text = "Error while stoping {0}".format(self.playingfile)

if __name__ == '__main__':
    init()
    app = MusicPlayerApp()
    app.run()