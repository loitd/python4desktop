#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# Project Name: python4desktop - Created Date: Wednesday September 16th 2020
# Author: loitd - Email: loitranduc@gmail.com
# Description: This is a short project/file description
# Copyright (c) 2020 loitd. WWW: https://github.com/loitd
# -----
# Last Modified: Wednesday September 16th 2020 4:07:58 pm By: loitd
# -----
# HISTORY:
# Date      	By    	Comments
# ----------	------	----------------------------------------------------------
# 2020-09-16	loitd	Initialized
###

class Person(object):
    '''Person class in Python'''
    _name = None
    _age = 0
    
    def __init__(self, name, age):
        '''Initialization'''
        self._name = name
        self._age = age
    
    def hello(self):
        '''Say hello to everyone'''
        print("Hello, my name is", self._name, ". I am", self._age, "years old.")

if __name__ == "__main__":
    loi = Person("Tran Duc Loi", 30)
    loi.hello()
    print("Yes, I am an instance of Person" if isinstance(loi, Person) else "No, I am NOT an instance of Person")
