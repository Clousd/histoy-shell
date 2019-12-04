#!/bin/bash/env pyt hon3.6
import numpy as np
import pandas as pd
file = open(u'python/hellopandas/td')


def fomartlist(info1):
    info1 = line.split()
    info1 = line.split('" ')
    info2 = info1[0].split(' ')
    #print (len(info1),info1[3],'\n',info2)
    if len(info2)==5 :
        return [info2[0],info2[1][1:],info2[3],'Null','Null','Null']+info1[3].split()
    elif len(info2)==7:
        li = [info2[0],info2[1][1:],info2[3],info2[4],info2[5],info2[6]]+info1[3].split()+[info1[1],info1[2]]
        if len(li) == 10:
            return li
        else:
            Exception: print("数组长度不符合要求")
    elif len(info2)==6:
        li = [info2[0],info2[1][1:],info2[3],info2[4],'Null',info2[5]]+info1[3].split()+[info1[1],info1[2]]
        if len(li) == 10:
            return li
        else:
            Exception: print("数组长度不符合要求")
    else:
        Exception: print("发生异常")
        print(info1,len(info2))
        return ['0']
i=0
it = []
while 1==1 :
    line = file.readline()
    if not line:
        break
    it.append(fomartlist(line))
headers = ['ip','time','url','type','file','protocol','code','byte','to','device']
df = pd.DataFrame(it,columns=headers)

   # print(fomartlist(line))

#df.to_excel("test.xls")
