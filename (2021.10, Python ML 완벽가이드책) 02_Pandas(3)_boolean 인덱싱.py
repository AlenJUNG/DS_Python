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

# # Boolean 인덱싱
# - loc[]에서는 지원하나 iloc[]에서는 정수형만 지원하기 때문에 Boolean 인덱싱 불가

import pandas as pd
import numpy as np

df = pd.read_csv(r'C:\Users\Administrator\DS_Python\data\titanic\train.csv')
df.head(3)

filter = df[df['Age'] > 60]

df['Age'] > 60

df[df['Age'] > 60]

filter

print(type(filter))

# #### Age가 60보다 큰 값 중 Name과 Age 컬럼 2개만 select
# > 컬럼 2개를 묶기 위해 이중 대괄호 사용
# - df에서 select 조건 vs df.loc에서 select 조건 주의

df[df['Age'] > 60][['Name', 'Age']].head(3)

# +
# ['Name', 'Age']는 컬럼 위치에 놓여야 함

df.loc[df['Age'] > 60, ['Name', 'Age']].head(3)

# +
# 다중 조건 시, 각 조건마다 괄호로 ( ) 묶어줄 것

df.loc[ (df['Age'] > 60) & (df['Pclass'] >= 1) & (df['Sex'] == 'female') ]
# -

cond1 = df['Age'] > 60
cond2 = df['Pclass'] >= 1
cond3 = df['Sex'] == 'female'
df[cond1 & cond2 & cond3]


