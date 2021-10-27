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


