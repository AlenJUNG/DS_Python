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

# # 정렬, Aggregation, Group By
# ## DataFrame, Series의 정렬 : sort_values()
# - sort_values()는 sql의 order by와 유사함
#   - 주요 파라미터
#     1. by : 특정 컬럼을 입력하면 해당 컬럼으로 정렬 수행
#     1. ascending=True 오름차순, ascending=False 내림차순 > default값은 오름차순
#     1. inplace

import pandas as pd
import numpy as np

df = pd.read_csv(r'C:\Users\Administrator\DS_Python\data\titanic\train.csv')

# +
# Name 오름차순 정렬

sorted = df.sort_values(by=['Name'])
sorted.head(3)

# +
# Pclass, Name 내림차순 정렬
# 여러 개의 컬럼으로 정렬하려면 by에 리스트 형식으로 정렬하려는 컬럼을 입력

sorted = df.sort_values(by=['Pclass', 'Name'], ascending=False)
sorted.head(3)
# -

# ## Aggregation 함수의 사용
# ### min(), max(), sum(), count(), mean()
# - 바로 호출할 경우 전 컬럼에 적용하므로 특정 컬럼에 적용하기 위해서는 추출 후 적용할 것

df.count()

df['Age'].count()

df[['Age', 'Fare']].mean()

# ## groupby() 적용
# ### DF의 groupby() 사용 시, 입력 파라미터 by에 컬럼을 입력하면 대상 컬럼으로 groupby 됌
# - DataFrame에 groupby()를 호출하면 DataFrameGroupBy라는 또다른 형태의 DF를 반환

groupby = df.groupby(by='Pclass')
print(type(groupby))

# - DF에 groupby()를 호출해 반환된 결과에 aggregation 함수를 호출하면 groupby() 대상 컬럼을 제외한 모든 컬럼에 aggregation 함수를 적용함

groupby = df.groupby('Pclass').count()
groupby

# - DF의 groupby()에 특정 컬럼만 aggregation 함수를 적용하려면 groupby()로 반환된 DataFrameGroupBy 객체에 해당 컬럼을 필터링한 뒤 aggregation 함수 적용

groupby = df.groupby('Pclass')[['PassengerId', 'Survived']].count()
groupby

df.groupby('Pclass')[['Age', 'Fare']].agg([max, min])

df.groupby('Pclass')['Age'].agg([max, min])

# - groupby()는 agg() 내에 입력값으로 딕셔너리 형태로 aggregation이 적용될 컬럼들과 aggregation 함수를 입력

agg_format = {'Age' : 'max', 'SibSp' : 'sum', 'Fare' : 'mean'}
df.groupby('Pclass').agg(agg_format)

# ## 결손 데이터 처리 (Missing Data)
# - isna() : 데이터가 NaN인지 아닌지를 True나 False로 알려줌

# +
# True > Missing Data

df.isna().head(3)

# +
# Missing Data의 개수는 isna() 결과에 sum() 함수를 추가해 구할 수 있음
# sum() 호출 시, True는 내부적으로 숫자 1로 변환되므로 개수를 구할 수 있음

df.isna().sum()
# -

# ## fillna()로 결손 데이터 대체하기
# > fillna()를 이용해 반환값을 다시 받거나 inplace=True 파라미터를 fillna()에 추가해야 실제 데이터 세트 값이 반영 됌
# #### Q) Cabin 컬럼의 NaN 값을 C000 으로 대체하기

df['Cabin'] = df['Cabin'].fillna('C000')
# df['Cabin'].fillna('C000', inplace=True) 와 같음
df.head(3)

df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Embarked'] = df['Embarked'].fillna('S')
df.isna().sum()


