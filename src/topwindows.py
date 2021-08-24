#!/usr/bin/python3
#-*- coding: utf-8 -*-
#created on 24-08-2021
#Drg - topwindows.py

import os
import re
import sys
import lxml
import pygubu
import tkmacosx
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

PROJECT_PATH = os.path.dirname(os.path.dirname(__file__))

#add service top window
class w_addService(tk.Toplevel):

    #init method
    def __init__(self, parent=None):
        super().__init__(parent)

        self.geometry('300x100')
        self.title('Specify service')

        self.mainframe = tk.Frame(self)
        self.mainframe.pack(side="top", fill="both")

    def exit():
        pass