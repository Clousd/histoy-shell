#!/bin/bash/env python3.6
import numpy as np
import pandas as pd
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)
df = pd.DataFrame([1,2,3],['A','B','C'])

df2 =  pd.DataFrame([['a','b','c'],['a','b','c'],['a','b','c']],columns=['A','B','C'])
df3 =  pd.DataFrame([['a','b','c'],['a','b','c'],['a','b','c']],columns=['C','D','E'])
#print(type([[1],[2]]),type([1]))
#print(df)
df4= df2.append(df3,ignore_index=True,sort=True)
#print(df)
#print('df3',df3)