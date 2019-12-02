#!/bin/bash/env pyt hon3.6
import numpy as np
file = open(u'python/hellopandas/access_log')


def fomartlist(info1):
    info1 = line.split()
    info1 = line.split('" ')
    info2 = info1[0].split(' ')
    if '408' in info1[3] :
       # print (info2)
        #print (info1[3])
        i=0
    else:
        li = info2+[info1[1],info1[2],info1[3]]
        if len(li) != 10:
            print (li,len(li))
        return li

while 1==1 :
    line = file.readline()
    if not line:
        break
    fomartlist(line)