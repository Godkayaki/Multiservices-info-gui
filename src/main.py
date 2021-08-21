#!/usr/bin/python3
#-*- coding: utf-8 -*-
#created on 21-08-2021
#Drg - main.py

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

import connections

PROJECT_PATH = os.path.dirname(os.path.dirname(__file__))

#main class
class MainApp(Frame):
    
    #init method
    def __init__(self, parent=None):
        self.builder = builder = pygubu.Builder()
        builder.add_from_file(GUI_FILE)
        self.mainwindow = builder.get_object('mainwindow')
        
        self.defineWidgets()
        self.setupButtons()

    #define pygubu widgets
    def defineWidgets(self):
        pass

    #setup bindings on startup
    def setupButtons(self):
        pass

    #run application
    def run(self):
        self.mainwindow.mainloop()

#run on main
if __name__ == '__main__':
    root = tk.Tk()
    root.title("Services Status")
    app = MainApp(root)
    app.run()