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

df1 = pd.read_csv('../DS_Python/01.  기본3문제/1_Highway/ds_highway_01_07.csv', encoding='utf-8', sep=',')
df2 = pd.read_csv('../DS_Python/01.  기본3문제/1_Highway/ds_highway_08_12.csv', encoding='utf-8', sep=',')

df1

df2


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
    elif x == 'gangwon':
        return 'GANGWON'    

df2['StartPoint'] = df2['StartPoint'].apply(lambda x : function(x)) # 열만 조건부 변경하기
# -

df2

df = pd.concat([df1, df2]) # pd.concat([]) pandas와 대괄호 실수
df

df_1 = df[df['StartPoint'] == 'GANGWON']

df_1_1 = pd.concat([df_1['Gyeonggi'], df_1['Chungcheong'], df_1['Jeolla'], df_1['Gyeongsang'], df_1['Gangwon']])
df_1_1

df_1_1.describe()

df_1_1.quantile(q = [0.25, 0.5, 0.75])


