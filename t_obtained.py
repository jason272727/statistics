# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 12:55:57 2020

@author: User
"""

#某飲料工廠生產飲料，其標準為每瓶飲料必須為500ml。為了驗證其產出皆符合規定，故對此進行抽樣，而其結果為:502.2,501.6,499.8,502.8,498.6,502.2,499.2,503.4,499.2
#請藉由其抽樣結果，推論該飲料公司生產之飲料容量，是否皆符合規定。
#假設:
    #H0:其生產飲料容量皆為500ml
    #H1:其生產飲料容量不為500ml

import pandas as pd
import numpy as np
from scipy import stats
import math
data=np.array([502.2,501.6,499.8,502.8,498.6,502.2,499.2,503.4,499.2])
u=500
xbar=data.mean()
sigma=data.std()
n=len(data)-1
t_obtained=stats.ttest_1samp(a=data, popmean=u)
print(t_obtained)
t_critical=stats.t.ppf(q=0.975,df=n)
print('t分數:',t_critical)
print('-----------way2-----------')
t_obtained2=(xbar-u)/(sigma/math.sqrt(n))
print('檢定統計量:',t_obtained2)
print('-%.2f<%.2f<%.2f'%(t_critical,t_obtained2,t_critical))
print('接受H0虛無假設，該飲料工廠所生產之飲料皆符合規定。')