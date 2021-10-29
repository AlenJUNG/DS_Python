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
# 대문자로 바꿔주는 함수 만들기

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

df1.describe()

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
# 0이 월요일부터 시작됌
df3['weekday'] = df3['date'].apply(lambda x : datetime.datetime.strptime(str(x), '%Y%m%d').weekday())
df3['weekday']

df3['month'] = df3['date'].apply(lambda x: str(x)[4:6])
df3['month']

df3

# 요일과 월별 그루핑으로 강원의 평균값 구하기
df3_group = df3.groupby(['weekday', 'month']).agg({'Gangwon': 'mean'})
df3_group.reset_index(inplace=True) # 인덱스 초기화, 실행 시, 보다 표가 깔끔하게 나옴
df3_group

# 사이킷런의 preprocessing 모듈의  minmaxScaler 서브 모듈을 이용
from sklearn.preprocessing import MinMaxScaler 
mms = MinMaxScaler()
arr3 = pd.DataFrame() 

# +
# arr3에 누적시킴에 주의할 것. '첫 번째 값은 0'

for i in range(7):
    # 특정 요일에 Gangwon 컬럼의 MinMax 값 구하기
    temp = mms.fit_transform(df3_group[df3_group['weekday'] == i][['Gangwon']])
    # 특정 데이터 프레임에 저장
    # 잘의 arr3은 어차피 0인데 왜 concat을 해야하는가? > arr3으로 계속 누적되기 때문 
    arr3 = pd.concat([arr3, pd.DataFrame(temp)])
# -

# DF에만 사용 가능
arr3.reset_index(inplace=True, drop=True)
arr3

# +
# 컬럼명 변경, inplace 주의

arr3.rename(columns={arr3.columns[0]:'mms'}, inplace=True)
# -

arr3

df3_group

# +
# 열 결합

df3_1 = pd.concat([df3_group, arr3], axis=1)
df3_1

# +
# 월별 그루핑 + mms의 평균 구하기

df3_2 = df3_1.groupby(['month']).agg({'mms' : 'mean'})
df3_2.reset_index(inplace=True)
# -

# 사이킷런의 클러스터를 호출
from sklearn.cluster import KMeans
# Kmeans 초기화 : 구하고자하는 클러스터는 3개, fit함수로 kmeans 학습시킴 
kmeans = KMeans(n_clusters=3, max_iter=100, random_state=1234).fit(df3_2[['mms']])
kmeans.predict(df3_2[['mms']])

# DF 형태로 보기 좋게 만들기 > 총 3개의 군집으로 나옴
pd.DataFrame(kmeans.predict(df3_2[['mms']]), columns=['cls'])

# 열결합
df3_3 = pd.concat([df3_2, pd.DataFrame(kmeans.predict(df3_2[['mms']]), 
                                       columns=['cls'])], axis=1)
df3_3

# df3_3에서 df3_3의 cls가 1인 컬럼을 뽑아내자 
df3_3[df3_3['cls'] == 1]

len(df3_3[df3_3['cls'] == 1])

m = df3_3[df3_3['cls'] == 1]['month']
m

# +
# 다양한 데이터를 비교하기 위해서 isin 함수 사용
# df3_1 month에 m 이 포함된 df3_1 전체 출력

df3_1[df3_1['month'].isin(list(m))]
# -

temp = df3_1[df3_1['month'].isin(list(m))]
temp[temp['weekday'] == 0]

temp[temp['weekday'] == 0]['mms'].mean()

# # 문4

df4 = df[df['StartPoint'] == 'GYEONGGI'][['date', 'Chungcheong', 'Gyeongsang', 'Gangwon', 'Jeolla']]
df4

# +
# joella 컬럼을 하나씩 밑으로 밀기

df4['Jeolla_before'] = df4['Jeolla'].shift(periods=1)
df4
# -

df4['month'] = df4['date'].apply(lambda x : str(x)[4:6])
df4['weekday'] = df4['date'].apply(lambda x : datetime.datetime.strptime(str(x), '%Y%m%d').weekday())
df4

df_train = df4[(df4['date'] < 20140701) & (df4['weekday'] == 6)]
df_test = df4[(df4['date'] == 20140706) | (df4['date'] == 20140713)
             | (df4['date'] == 20140720)]
df_train

df_test

from sklearn.linear_model import LinearRegression
# model에 학습, fit( 독립변수, 종속변수 )
model = LinearRegression().fit(df_train[['Chungcheong', 'Gyeongsang', 'Gangwon', 'Jeolla_before']], 
                       df_train['Jeolla'])
model

model.predict(df_test[['Chungcheong', 'Gyeongsang', 'Gangwon', 'Jeolla_before']])
