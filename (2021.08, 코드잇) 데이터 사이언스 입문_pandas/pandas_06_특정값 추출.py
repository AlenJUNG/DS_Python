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

# ---

# # pandas_06_특정값 추출

import numpy as np
import pandas as pd

iphone_df = pd.read_csv('data/iphone.csv', index_col=0)

iphone_df

iphone_df.loc['iPhone 8', '메모리']

iphone_df.loc[:, '출시일'] # 컬럼 1열 통째로 받기

type(iphone_df.loc[:, '출시일'])

iphone_df.loc[['iPhone 7', 'iPhone XS']]

iphone_df.loc[:, ['출시일', '출시 버전']]

type(iphone_df.loc[['iPhone 7', 'iPhone XS']])

iphone_df.loc['iPhone 8' : 'iPhone XS', '디스플레이' : '출시 버전']

iphone_df.loc[[True, False, True, False, True, False, True]]

iphone_df.loc[:, [True, False, True, False, True]]

iphone_df['디스플레이'] > 5

iphone_df.loc[iphone_df['디스플레이'] > 5]

iphone_df['Face ID'] == 'Yes'

iphone_df.loc[iphone_df['Face ID'] == 'Yes']

(iphone_df['디스플레이'] > 5) & (iphone_df['Face ID'] == 'Yes')

iphone_df.loc[(iphone_df['디스플레이'] > 5) & (iphone_df['Face ID'] == 'Yes')]

condition = (iphone_df['디스플레이'] > 6) | (iphone_df['Face ID'] == 'Yes')

iphone_df[condition]

iphone_df.loc[condition]

iphone_df.iloc[0, 0]

iphone_df.iloc[[0,3], [1,3]]


