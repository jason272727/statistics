# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 12:31:00 2020

@author: User
"""

#假設檢定
#題目:
#某大學招收外籍生，對此有些人認為，外籍生成績表現比本國學生好；反之也有人認為之間沒有差異。
#為了驗證外籍生與本國生之間成績差異，該校隨機抽樣了100位外籍生，其平均成績為71.5分。
#而該校平均成績為70分，母體標準差為2.5。請由上述資料進行驗證，探討之間是否有所差異。
#sol:
#   假設:
#       H0:外籍生與本國生之間成績沒有差異
#       H1:外籍生與本國生之間成績有差異

import pandas as pd
import numpy as np
from scipy import stats
import math
xbar=71.5
u=70
sigma=2.5
n=100
z_obtained=(xbar-u)/(sigma/math.sqrt(n))
print('z檢定統計量',z_obtained)
z_critical=stats.norm.ppf(q=0.975)
print('z分數:',z_critical)
print('%.2f>%.2f,-%.2f<%.2f'%(z_obtained,z_critical,z_critical,z_obtained))
print('拒絕H0，外籍生與本國生之間成績有所差異')