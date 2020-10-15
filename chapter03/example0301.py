#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# -------------------------------------
# File: chapter03\example0301.py
# Description: This is a short description
# Author: loitd - WWW: https://github.com/loitd
# ----------
# HISTORY:
# Date      	By    	Comments
# ----------	------	---------------
# 2020-09-26	loitd	Initialized
# -------------------------------------

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MainApp(App):
    def build(self):
        layout = BoxLayout(padding=10)
        label = Label(
            text='[color=ff3333]Hello[/color] from Kivy with Python for Desktop by [b]Loitd[/b]', 
            size_hint=(1, .5), 
            pos_hint={'center_x': .5, 'center_y': .5},
            markup = True
        )
        button = Button(text='Press me. See the console')
        button.bind(on_press=self.on_press_button)
        layout.add_widget(label)
        layout.add_widget(button)
        return layout
    
    def on_press_button(self, instance):
        print("Button is pressed", instance)

if __name__ == '__main__':
    app = MainApp()
    app.run()