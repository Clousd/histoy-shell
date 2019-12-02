#!/bin/bash/env python3.6
import numpy as np
import pandas as pd
df = pd.read_excel('kate.xlsx',sheet_name='11',)
print(df)
data=df.head()
print(u'获取到所有的值:\n{0}'.format(data))
