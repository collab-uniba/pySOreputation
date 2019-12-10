# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 09:22:23 2019

@author: Roberto Bellarosa
"""

#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Nov 25, 2019 09:20:47 AM CET  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

from tkinter import messagebox

from StackOverflowClient.result import result_interface_support
import os.path
import json

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    root = tk.Tk()
    top = Toplevel1 (root)
    result_interface_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    result_interface_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font9 = "-family {Calibri} -size 13 -weight normal "  \
            "-slant roman -underline 0 -overstrike 0"

        top.geometry("941x453+793+170")
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.resizable(0, 0)
        top.title("Stack Overflow Client")
        top.configure(background="white")
        
        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.021, rely=0.309, height=28, width=100)
        self.Label1.configure(background="white")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''User name:''')

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.244, rely=0.751,height=26, relwidth=0.217)
        self.Entry1.configure(background="#efefef")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font=font9)
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.009, rely=0.419, height=26, width=100)
        self.Label2.configure(background="white")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font9)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''User id:''')

        self.Entry2 = tk.Entry(top)
        self.Entry2.place(relx=0.244, rely=0.64,height=26, relwidth=0.217)
        self.Entry2.configure(background="#efefef")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font=font9)
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.018, rely=0.53, height=28, width=127)
        self.Label3.configure(background="white")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font9)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Creation Date:''')

        self.Entry3 = tk.Entry(top)
        self.Entry3.place(relx=0.244, rely=0.53,height=26, relwidth=0.217)
        self.Entry3.configure(background="#efefef")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font=font9)
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(insertbackground="black")

        self.Label4 = tk.Label(top)
        self.Label4.place(relx=0.018, rely=0.64, height=28, width=138)
        self.Label4.configure(background="white")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font=font9)
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''Real reputation:''')

        self.Entry4 = tk.Entry(top)
        self.Entry4.place(relx=0.244, rely=0.309,height=26, relwidth=0.217)
        self.Entry4.configure(background="#efefef")
        self.Entry4.configure(disabledforeground="#a3a3a3")
        self.Entry4.configure(font=font9)
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(insertbackground="black")

        self.Label5 = tk.Label(top)
        self.Label5.place(relx=0.017, rely=0.751, height=28, width=179)
        self.Label5.configure(background="white")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font=font9)
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''Estimated reputation:''')

        self.Entry5 = tk.Entry(top)
        self.Entry5.place(relx=0.244, rely=0.419,height=26, relwidth=0.217)
        self.Entry5.configure(background="#efefef")
        self.Entry5.configure(disabledforeground="#a3a3a3")
        self.Entry5.configure(font=font9)
        self.Entry5.configure(foreground="#000000")
        self.Entry5.configure(insertbackground="black")

        self.Label6 = tk.Label(top)
        self.Label6.place(relx=0.015, rely=0.861, height=28, width=201)
        self.Label6.configure(background="white")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(font=font9)
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(text='''Total time for execution:''')

        self.Entry6 = tk.Entry(top)
        self.Entry6.place(relx=0.244, rely=0.861,height=26, relwidth=0.217)
        self.Entry6.configure(background="#efefef")
        self.Entry6.configure(disabledforeground="#a3a3a3")
        self.Entry6.configure(font=font9)
        self.Entry6.configure(foreground="#000000")
        self.Entry6.configure(insertbackground="black")
        

        self.Listbox1 = tk.Listbox(top)
        self.Listbox1.place(relx=0.521, rely=0.309, relheight=0.393
                , relwidth=0.419)
        self.Listbox1.configure(background="#efefef")
        self.Listbox1.configure(disabledforeground="#a3a3a3")
        self.Listbox1.configure(font=font9)
        self.Listbox1.configure(foreground="#000000")
        
        file = "C:\\Users\\Roberto Bellarosa\\SOWebService\\StackOverflowClient\\result_file.json"                        
        with open(file, "r") as read_file:
            data = json.load(read_file)
            
        i = 0
        for item in data['user_id']:
            self.Listbox1.insert(i, item)
            i = i + 1
            
        def show_result_user(file):
            return
            
        def close_result():
            msg = messagebox.askquestion("Exit from result!", "Do you really want to exit?")
            if msg == 'yes':
                root.destroy()
            else:
                return
        
        self.Button1 = tk.Button(top, command=close_result)
        self.Button1.place(relx=0.659, rely=0.773, height=73, width=146)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#efefef")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font9)
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Go back''')
        
        self.Label7 = tk.Label(top)
        self.Label7.place(relx=0.255, rely=0.044, height=85, width=439)
        self.Label7.configure(background="#efefef")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(foreground="#000000")
        photo_location1 = os.path.join(prog_location,"//imgso.png")
        global _img1
        _img1 = tk.PhotoImage(file=photo_location1)
        self.Label7.configure(image=_img1)
        self.Label7.configure(relief="sunken")
        self.Label7.configure(text='''Label''')
        

if __name__ == '__main__':
    vp_start_gui()


def result_gui():
    vp_start_gui()
