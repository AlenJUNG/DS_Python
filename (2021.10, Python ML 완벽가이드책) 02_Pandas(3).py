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

df[df['Age'] > 60][['Name', 'Age']].head(3)


