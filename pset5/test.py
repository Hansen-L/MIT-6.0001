# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 20:57:08 2018

@author: Hanen
"""
trigger_dic = {'TITLE':'TitleTrigger','DESCRIPTION':'DescriptionTrigger','AFTER':'AfterTrigger','BEFORE':'BeforeTrigger','NOT':'NotTrigger','AND':'AndTrigger','OR':'OrTrigger'}
triggers = []
lines =['t1,TITLE,election', 't2,DESCRIPTION,Trump', 't3,DESCRIPTION,Clinton', 't4,AFTER,3 Oct 2016 17:00:10', 't5,AND,t2,t3', 't6,AND,t1,t4', 'ADD,t5,t6']
for i,entry in enumerate(lines,0):
    entry = entry.split(',')
    trigger_type = trigger_dic[entry[1]]
    t1 = exec(trigger_type + '("' + entry[2] + '")')