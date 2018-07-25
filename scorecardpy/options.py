# -*- coding: utf-8 -*-
"""
Created on Thu May  3 13:28:54 2018

@author: TomasLarsson
"""


def set_options(colors='',outcomes=''):
    print("wf")
    if colors!='' :
        global IH_colors
        IH_colors=colors
    if outcomes!='' :
        global IH_outcomes
        IH_outcomes=outcomes


def get_options(option):
    global IH_colors, IH_outcomes
    if option=="colors":
        r=IH_colors
    if option=="outcomes":
        r=IH_outcomes
    return(r)


