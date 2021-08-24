#!/usr/bin/python3
#-*- coding: utf-8 -*-
#created on 24-08-2021
#Drg - topwindows.py

import os, re, sys, paramiko, json
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

PROJECT_PATH = os.path.dirname(os.path.dirname(__file__))

#add service top window
class w_addService(tk.Toplevel):

    service_str_c = "sudo systemctl is-active "

    #init method
    def __init__(self, parent=None):
        super().__init__(parent)

        #self.geometry('300x300')
        self.title('Specify service')

        self.mainframe = tk.Frame(self)
        self.mainframe.pack(side="top", fill="both")
        self.mainframe.pack_propagate(1)

        #frame title
        frame_title = tk.Frame(self.mainframe, pady=15)
        frame_title.pack(side="top", fill="both")

        hostname_lbl = tk.Label(frame_title, text="Set service values:")
        hostname_lbl.pack(side="top")
        hostname_lbl.config(font=("TkCaptionFont")) 

        #frame content
        frame_content = tk.Frame(self.mainframe, padx=20)
        frame_content.pack(side="top", fill="both")

        #service name frame
        frame_service = tk.Frame(frame_content, height=10)
        frame_service.pack(side="top", fill="x", pady=5)
        
        frame_service_lbl = tk.Frame(frame_service, height=20)
        frame_service_lbl.pack(side="left", expand=True, fill="x")
        frame_service_entry = tk.Frame(frame_service, height=30, width=20)
        frame_service_entry.pack(side="right", expand=True, fill="x")

        service_lbl = tk.Label(frame_service_lbl, text="service name: ", width=10)
        service_lbl.pack(side="right", expand=False)
        self.service_entry = tk.Entry(frame_service_entry)
        self.service_entry.pack(side="left")

        #hostname frame
        frame_hostname = tk.Frame(frame_content, height=10)
        frame_hostname.pack(side="top", fill="x", pady=5)
        
        frame_hostname_lbl = tk.Frame(frame_hostname, height=20)
        frame_hostname_lbl.pack(side="left", expand=True, fill="x")
        frame_hostname_entry = tk.Frame(frame_hostname, height=30, width=20)
        frame_hostname_entry.pack(side="right", expand=True, fill="x")

        hostname_lbl = tk.Label(frame_hostname_lbl, text="hostname: ", width=10)
        hostname_lbl.pack(side="right", expand=False)
        self.hostname_entry = tk.Entry(frame_hostname_entry)
        self.hostname_entry.pack(side="left")

        #username frame
        frame_username = tk.Frame(frame_content, height=10)
        frame_username.pack(side="top", fill="x", pady=5)
        
        frame_username_lbl = tk.Frame(frame_username, height=20)
        frame_username_lbl.pack(side="left", expand=True, fill="x")
        frame_username_entry = tk.Frame(frame_username, height=30, width=20)
        frame_username_entry.pack(side="right", expand=True, fill="x")

        username_lbl = tk.Label(frame_username_lbl, text="username: ", width=10)
        username_lbl.pack(side="right", expand=False)
        self.username_entry = tk.Entry(frame_username_entry)
        self.username_entry.pack(side="left")

        #password frame
        frame_password = tk.Frame(frame_content, height=10)
        frame_password.pack(side="top", fill="x", pady=5)
        
        frame_password_lbl = tk.Frame(frame_password, height=20)
        frame_password_lbl.pack(side="left", expand=True, fill="x")
        frame_password_entry = tk.Frame(frame_password, height=30, width=20)
        frame_password_entry.pack(side="right", expand=True, fill="x")

        password_lbl = tk.Label(frame_password_lbl, text="password: ", width=10)
        password_lbl.pack(side="right", expand=False)
        self.password_entry = tk.Entry(frame_password_entry)
        self.password_entry.pack(side="left")

        #test connection button frame
        frame_testconnection = tk.Frame(self.mainframe, height=35, pady=5)
        frame_testconnection.pack(side="top", fill="x", expand=False)
        
        self.bt_testconnection = tk.Button(frame_testconnection, text="Test connection")
        self.bt_testconnection.pack(side="top", expand=False)
        self.bt_testconnection.bind("<Button-1>", self.test_connection)

        #add service and exit frame
        frame_buttons = tk.Frame(self.mainframe, pady=15)
        frame_buttons.pack(side="top", fill="both")

        frame_left = tk.Frame(self.mainframe)
        frame_left.pack(side="left", fill="x", expand=True)
        frame_right = tk.Frame(self.mainframe)
        frame_right.pack(side="right", fill="x", expand=True)

        self.bt_apply = tk.Button(frame_left, text="Add", width=6)
        self.bt_apply.pack(side="right", expand=False)
        self.bt_exit = tk.Button(frame_right, text="Exit", width=6)
        self.bt_exit.pack(side="left", expand=False)
        
        self.bt_apply.bind("<Button-1>", self.add_service)
        self.bt_exit.bind("<Button-1>", self.exit_w)

        #add service and exit frame
        frame_separator = tk.Frame(self.mainframe, height=60)
        frame_separator.pack(side="top", expand=True)

    #test connection method
    def test_connection(self, event):
        sn, h, u, p = self.get_entries_content()
        
        #try ssh connection, if error popups return
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(hostname=h, username=u, password=p)
        except:
            messagebox.showerror(message="SSH connection error.", title="Error: SSH connection")
            return
        
        #format command, run command, get result
        c_run = self.service_str_c + sn
        stdin, stdout, stderr = client.exec_command(c_run)
        msg = stdout.read().decode()

        #show messagebox depending on service status
        if "active" in msg:
            messagebox.showinfo(message="SSH connection successful, service up.", title="SSH successful")
        elif "failed" in msg:    
            messagebox.showinfo(message="SSH connection successful, service down.", title="SSH successful")

    #apply config
    def add_service(self, event):
        sn, h, u, p = self.get_entries_content()
        print(sn, h, u, p)

    #return entries content
    def get_entries_content(self):
        servicename = self.service_entry.get()
        hostname = self.hostname_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        return servicename, hostname, username, password

    #exit app
    def exit_w(self, event):
        self.destroy()