# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 23:58:47 2020

@author: User
"""

import pandas as pd
import numpy as np
from scipy import stats
observed=np.array([20,16,34,40,38,32])
expected=np.array([30,30,30,30,30,30])
chi_square,p_value=stats.chisquare(f_obs=observed,f_exp=expected)
chi_critical=stats.chi2.ppf(q=0.95,df=5)
print('臨界值:',chi_critical)
print('---------輸出結果---------')
print('卡方值:',chi_square)
print('p_value:',p_value)
print('-----------way2-----------')
chi_square2=(((observed-expected)**2)/expected).sum()
print('卡方值:',chi_square2)