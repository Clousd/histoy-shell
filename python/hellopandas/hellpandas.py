#!/bin/bash/env python3.6
import numpy as np
import pandas as pd
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)
df = pd.DataFrame([s,s])
print(df)