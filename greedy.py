# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 03:13:27 2018

@author: ashis
"""

def get_move(instance):
    s={}
    if instance.move_down()[0]:
        s[instance.move_down()[1]]=0
    if instance.move_up()[0]:
        s[instance.move_up()[1]]=1
    if instance.move_left()[0]:
        s[instance.move_left()[1]]=2
    if instance.move_right()[0]:
        s[instance.move_right()[1]]=3
    m=0
    m_i=0
    print(s)
    for key in s:
        if key>=m:
            m_i=s[key]
    return m_i
