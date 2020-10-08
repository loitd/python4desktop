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

import os, time
# os.environ['KIVY_AUDIO'] = 'sdl2' # Please remind that seek() and get_pos() are not implement in sdl2 audio
os.environ['KIVY_AUDIO'] = 'gstplayer'
os.environ['KIVY_WINDOW'] = 'sdl2'
os.environ['KIVY_IMAGE'] = 'sdl2'
os.environ['KIVY_VIDEO'] = 'null'
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.gridlayout import GridLayout
from kivy.core.audio import SoundLoader
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivy.logger import Logger
from kivy.uix.filechooser import FileChooserListView, FileChooser
from kivy.lang import Builder

# kivy.require('1.9.0') #restrict kivy version

def init():
    Window.size = (650,150)
    # Window.borderless = True
    Window.clearcolor = (1, 0, 1, 1)
    Window.clear()
    kv = ''''''
    Builder.load_string(kv)

class FileChooserPopup(Popup):
    def __init__(self, **kwargs):
        super(FileChooserPopup, self).__init__(**kwargs)
        Logger.info("[FileChooserPopup] initialized")

    def build(self):
        # self.title='P4D File Chooser'
        # layout = BoxLayout(padding=1, orientation='vertical')
        return FileChooserListView()
        # layout.add_widget(fclv)
        # return layout

class FileChooserWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(FileChooserWidget, self).__init__(**kwargs)
        Logger.info("[FileChooserWidget] initialized")
        self.fcpopup = FileChooserPopup()
        self.fcpopup.open()
    
    def close(self):
        self.fcpopup.dismiss()

class MusicPlayerApp(App):
    def __init__(self, **kwargs):
        super(MusicPlayerApp, self).__init__(**kwargs)
        self.playingfile = 'python4desktop.mp3'
        self.sound = SoundLoader.load(self.playingfile)
        self.sound.on_play = self.onplaying
        self.sound.on_stop = self.onstopping
        self.lbl1 = None
        self.stopbtn = None
        self.playbtn = None
        self.clock = Clock.schedule_interval(self.onstatus, 2)

    def __del__(self):
        try:
            self.clock.cancel() # unschedule using cancel
            self.sound.stop()
            self.sound.unload()
        except Exception as e:
            Logger.error("[__del__] Exception: {0}".format(e))

    def build(self):
        self.icon = 'py4de.png'
        self.title = 'Python4Desktop Music Player'
        layout = BoxLayout(padding=1, orientation='vertical')
        
        hbox = BoxLayout(orientation='vertical', size_hint=(1, None), height=32)
        self.lbl1 = Label(text="Press Play to play {0}".format(self.playingfile))
        hbox.add_widget(self.lbl1)
        layout.add_widget(hbox)
        
        buttons = [['Open', 'Play', 'Stop', 'Exit']]
        for row in buttons:
            hbox = BoxLayout(orientation='horizontal', size_hint=(1, None), height=48)
            for b in row:
                if b == 'Stop':
                    self.stopbtn = Button(text=b, background_color=(1,0,0,0.5))
                    self.stopbtn.bind(on_press=self.on_press_button)
                    hbox.add_widget(self.stopbtn)
                elif b == 'Play':
                    self.playbtn = Button(text=b, background_color=(0,1,0,0.5))
                    self.playbtn.bind(on_press=self.on_press_button)
                    hbox.add_widget(self.playbtn)
                else:
                    button = Button(text=b)
                    button.bind(on_press=self.on_press_button)
                    hbox.add_widget(button)
            layout.add_widget(hbox)
        return layout

    def on_newfileopen(self, *args):
        try:
            self.fcwidget.close()
            filepath = args[1][0]
            filename, fileext = os.path.splitext(filepath)
            if fileext in ['.mp3', '.wav']:
                self.playingfile = filepath
                self.playmusic()
            else:
                self.lbl1.text = "File extension not match. Keep playing {0}".format(self.playingfile)
        except Exception as e:
            Logger.error("[on_newfileopen] Exception: {0}".format(e))
        
    
    def on_press_button(self, instance):
        try:
            Logger.info("[on_press_button] Button is pressed: {0}".format(instance.text))
            if instance.text == 'Exit':
                Window.close()
            elif instance.text == 'Open':
                self.fcwidget = FileChooserWidget()
            elif instance.text == 'Play':
                # instance.disabled = 1
                self.playmusic()
            elif instance.text == 'Stop':
                self.stopmusic()
        except Exception as e:
            Logger.error("[on_press_button] Exception: {0}".format(e))
        
    def playmusic(self):
        try:
            if self.sound: 
                if self.sound.source != self.playingfile: # different source
                    if self.sound.state == 'play':
                        self.sound.stop()
                        self.sound.unload()
                    self.sound = SoundLoader.load(self.playingfile)
                    self.sound.play()
                else: # same source
                    if self.sound.state == 'stop':
                        self.sound.play()
            else:
                self.sound = SoundLoader.load(self.playingfile)
                self.sound.play()
        except Exception as e:
            self.lbl1.text = "Error while playing {0}".format(self.playingfile)
            Logger.error("[playmusic] Exception: {0}".format(e))

    def stopmusic(self):
        try:
            if self.sound:
                self.sound.stop()
                # self.sound.unload()
        except Exception as e:
            self.lbl1.text = "Error while stoping {0}".format(self.playingfile)
            Logger.error("[stopmusic] Exeption: {0}".format(e))
    
    def onplaying(self):
        pass

    def onstopping(self):
        pass

    def onstatus(self, dt):
        '''check status periodically'''
        # dt means delta-time
        if self.sound.state == 'play':
            percent = self.sound.get_pos()*100//self.sound.length
            self.lbl1.text = "Source : {0}\nPlaying : {1:.2f}/{2:.2f} (seconds) - Percentage: {4}%\nVolume: {3}\n\n".format(self.sound.source, self.sound.get_pos(), self.sound.length, self.sound.volume, percent)
        else:
            self.lbl1.text = "Source : {0}\nStopped\n\n".format(self.sound.source)

if __name__ == '__main__':
    init()
    app = MusicPlayerApp()
    app.run()