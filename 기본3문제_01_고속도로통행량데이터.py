# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

import pandas as pd
import numpy as np

df_1 = pd.read_csv('../DS_Python/01.  기본3문제/1_Highway/ds_highway_01_07.csv', 
                 encoding='utf-8', sep=',')
df_2 = pd.read_csv('../DS_Python/01.  기본3문제/1_Highway/ds_highway_08_12.csv', 
                 encoding='utf-8', sep=',')

df_1.head(10)

df_2.head(10)


# +
def function(x):
    if x == 'gyeonggi':
        return 'GYEONGGI'
    elif x == 'chungcheong':
        return 'CHUNGCHEONG'
    elif x == 'jeolla':
        return 'JEOLLA'
    elif x == 'gyeongsang':
        return 'GYEONGSANG'
    elif 'gangwon':
        return 'GANGWON'
    
    
df_2['StartPoint'] = df_2['StartPoint'].apply(lambda x : function(x))
# 1. apply( ) 안에 모든 수식이 들어감
# 2. df_2['StartPoint'] = 로 반드시 저장해주기
# -

# 두 df의 row bind는 concat 함수를 사용
df = pd.concat([df_1, df_2])
df

# # 문1

# 강원에서 출발한 통행량을 df1에 저장
df1 = df[df['StartPoint'] == 'GANGWON']

df1

# df1(강원에서 출발하여) 각 도시로 도착한 통행량을 하나의 컬럼으로 통합
df1 = pd.concat([df1['Gyeonggi'], df1['Chungcheong'], df1['Jeolla'], 
                 df1['Gyeongsang'], df1['Gangwon']])
df1

# q1, median, q3 구하기
df1.quantile(q = [0.25, 0.5, 0.75])

# # 문2

# 경기를 출발하여 경상에 도착한 통행량
df_gi = df[df['StartPoint'] == 'GYEONGGI']['Gyeongsang']
df_gi

# 경상을 출발하여 경기에 도착한 통행량
df_sang = df[df['StartPoint'] == 'GYEONGSANG']['Gyeonggi']
df_sang

# T-test를 사용하기 위해 호출
from scipy import stats
stats.ttest_ind(df_gi, df_sang)

# # 문3

df3 = df[df['StartPoint'] == 'CHUNGCHEONG'][['date', 'Gangwon']]
df3

import datetime
df3['weekday'] = df3['date'].apply(lambda x : datetime.datetime.strptime(str(x), '%Y%m%d').weekday()) # 월요일이 0
df3['weekday']

df3['month'] = df3['date'].apply(lambda x: str(x)[4:6])
df3['month']

df3

df3_group = df3.groupby(['weekday', 'month']).agg({'Gangwon': 'mean'})
df3_group.reset_index(inplace=True) # 인덱스 초기화, 실행 시, 보다 표가 깔끔하게 나옴
df3_group

# 사이킷런의 preprocessing 모듈의  minmaxScaler 서브 모듈을 이용
from sklearn.preprocessing import MinMaxScaler 
mms = MinMaxScaler()
arr3 = pd.DataFrame()

# +
for i in range(7):
    temp = mms.fit_transform(df3_group[df3_group['weekday'] == i][['Gangwon']])
    arr3 = pd.concat([arr3, pd.DataFrame(temp)])
    
arr3
# -


