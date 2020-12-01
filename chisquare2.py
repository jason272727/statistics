# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 21:46:05 2020

@author: User
"""

import pandas as pd
import numpy as np
from scipy import stats
data=pd.DataFrame([[331,217,548],[315,352,667],[646,569,1215]],columns=['喜歡','不喜歡','小計'],index=['男','女','小計'])
observed=data.iloc[0:3,0:3]
print('-------印出DataFrame-------')
print(observed)
gender=observed.iloc[0:2,2]
favorite=observed.iloc[2,0:2]
expected=np.outer(gender, favorite)/1215
expected=pd.DataFrame(expected)
expected.index=['男','女']
expected.columns=['喜歡','不喜歡']
print('-----------期望值----------')
print(expected)
row=2
col=2
df_value=(row-1)*(col-1)
chi_square=(((observed-expected)**2)/expected).sum().sum()
print('----------結果輸出----------')
print('卡方值',chi_square)
chi_critical=stats.chi2.ppf(q=0.95,df=df_value)
print('臨界值',chi_critical)
print('----------way2----------')
chi_square2,p_value,df,matrix=stats.chi2_contingency(observed=observed)
print('卡方值',chi_square2)
print('p_value:',p_value)