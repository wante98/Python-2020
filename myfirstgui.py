# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 22:03:55 2021

@author: bea
"""

import tkinter as tk

def hello():
    print("Hello World")
window = tk.TK()
window.title('Hello World')
window.geometry("300*100+250+150")

# make a button
button = tk.Button(window,
                   text = 'Hello',
                   command = hello)

button.pack()

window.mainloop()
