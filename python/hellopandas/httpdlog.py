#!/bin/bash/env python3.6
file = open(u'access_log')
for i in file.readline():
    print (i.split('" ')[3][:3])