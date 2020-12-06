# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 14:28:22 2020

@author: User
"""

#資料標準化練習
#z_score計換
import pandas as pd
import numpy as np
from sklearn import preprocessing
#Facebook好友追蹤數
f_tracking=np.array([110,1018,1130,417,626,957,90,951,946,797,981,125,456,731,1640,486,1309,472,1133,1773,906,532,742,621,855])
#快樂程度
f_happy=np.array([0.3, 0.8, 0.5, 0.4, 0.6, 0.4, 0.7, 0.5, 0.4, 0.3, 0.3, 0.6, 0.2, 0.8, 1, 0.6, 0.2, 0.7, 0.5, 0.7, 0.1, 0.4, 0.3, 0.6, 0.3])
print('-----------original data------------')
original_data=pd.DataFrame({'f_tracking':f_tracking,'f_happy':f_happy},columns=['f_tracking','f_happy'])
print(original_data)
print('---------------way1---------------')
f_tracking_mean=f_tracking.mean()
f_tracking_std=f_tracking.std()
f_happy_mean=f_happy.mean()
f_happy_std=f_happy.std()
tracking_z_score=(f_tracking-f_tracking_mean)/f_tracking_std
happy_z_score=(f_happy-f_happy_mean)/f_happy_std
df=pd.DataFrame({'f_tracking_s1':tracking_z_score,'f_happy_s1':happy_z_score},columns=['f_tracking_s1','f_happy_s1'])
print(df)
df.plot(kind='scatter',x='f_tracking_s1',y='f_happy_s1')
print('---------------way2---------------')
df2=pd.DataFrame(preprocessing.scale(original_data),columns=['f_tracking_s2','f_happy_s2'])
print(df2)
df2.plot(kind='scatter',x='f_tracking_s2',y='f_happy_s2')
print('---------------way3---------------')
scaler=preprocessing.StandardScaler()
df3_std=scaler.fit_transform(original_data)
df3=pd.DataFrame(df3_std,columns=['f_tracking_s3','f_happy_s3'])
print(df3)
df3.plot(kind='scatter',x='f_tracking_s3',y='f_happy_s3')
