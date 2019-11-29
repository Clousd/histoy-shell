#!/bin/bash
# tail  -n 999900 /usr/local/apache2/logs/access_log |grep 28/Jui
# 113.143.180.248
#  -
#  -
#  image.zhaoits.com
#  [09/Sep/2019:15:05:22 +0800]
# "GET /upload/AppIcon/System/1517534895-5a73beaff0430.png HTTP/1.1"
#  "-"
# "Mozilla/5.0 (iPhone; CPU iPhone OS 12_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"
#  200 4602
from pandas import DataFrame as dd
file = open(u'access_log')


def listformart(line):

    space1 = line.split()
    split11 = line.split(' "')
   # print(split11[0])
    #print(split11[1])
    #print(split11[2])
   # print(split11[3])
# xiaojunliang
   # tmp=[]
    #print(split11[1])
    if len(split11[1].split())>1:
       # print(split11[2]+'\t'+split11[1])
        if split11[2].split('"')[0]=='-':
            print('111\n')
            tmp = ['b',space1[0], 
            space1[3],
            (space1[4].split('[')[1]).split()[0], 
            split11[1].split()[0], 
            space1[3]+split11[2],split11[1].split('"')[0],
            split11[3].split('"')[0].split('" ')[0]+split11[3].split('"')[1].split()[0], split11[3].split('"')[1].split()[1]]
        else:
            tmp = ['a',space1[0], 
            space1[3], 
            (space1[4].split('[')[1]).split()[0],
            split11[1].split()[2], 
            split11[1].split()[0], 
            split11[2].split('" ')[0]+split11[1].split()[1].split('" ')[0],  split11[3].split('"')[0], split11[3].split('"')[1].split()[0], split11[3].split('"')[1].split()[1]]
    
    else:
        tmp = ['c',space1[0], 
        space1[3],
         (space1[4].split('[')[1]).split()[0], 
         split11[1].split()[0], 
         split11[2],split11[1].split('"')[0],
         split11[3].split('"')[0].split('" ')[0]+split11[3].split('"')[1].split()[0], split11[3].split('"')[1].split()[1]]
    return tmp


while 1 == 1:
    line1 = file.readline()
    if not line1:
        break
    print(listformart(line1))


#dds = dd(['ip','url'],[line.split()[0],line.split()[2]])
# print(dds)
# for t in tt:
#   print (t)
# print(tt)
# while 1:
#    iffin=1
#    lines = file.readlines(1000000)
#    if  iffin==1:
#       if findvchar(lines)!='':
#           print   ()
#    if not lines:
#     break
#
#     if u'Nov/2019' in lines:
#       iffin==2
