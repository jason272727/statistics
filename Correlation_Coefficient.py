# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 17:02:39 2020

@author: User
"""
#本題探討手機使用時間，與工作效率表現之間，是否有所相關。

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#手機使用時間
phone=np.array([0,0,0,1,1.3,1.5,2,2.2,2.6,3.2,4.1,4.4,4.4,5])
#工作效率
performance=np.array([87,89,91,90,82,80,78,81,76,85,80,75,73,72])
df=pd.DataFrame({'phone':phone, 'performance':performance})
#圖
df.plot(kind='scatter', x='phone',y='performance')
phone_mean=phone.mean()
performance_mean=performance.mean()
n=len(performance)
Covariance=((phone-phone_mean)*(performance-performance_mean)/n).sum()
print('共變異數為:',Covariance)
phone_std=phone.std()
performance_std=performance.std()
Corr=Covariance/(phone_std*performance_std)
print('相關係數:',Corr)
print('結果發現，手機使用時間與工作效率呈現負相關，如圖所示。意即當手機使用時間愈短，其工作效率愈佳。且根據皮爾森相關係數發現，其值為%.2f，屬於高度負相關。'%(Corr))
print('--------求相關係數-方法2--------')
print(df.corr())