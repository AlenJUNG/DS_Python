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

# # pandas_07_df 값변경

import numpy as np
import pandas as pd

iphone_df = pd.read_csv('data/iphone.csv', index_col=0)

iphone_df

iphone_df.loc['iPhone 8', '메모리']

iphone_df.loc['iPhone 8', '메모리'] = '2.5GB'

iphone_df.loc['iPhone 8', '메모리']

iphone_df.loc['iPhone 8']

iphone_df.loc['iPhone 8'] = ['2016-09-22', '4.7', '2GB', 'iOS 11.0', 'No']

iphone_df.loc['iPhone 8']

iphone_df.loc[:, 'Face ID']

iphone_df.loc[:, 'Face ID'] = 'YES'

iphone_df

iphone_df[['디스플레이', 'Face ID']]

iphone_df['디스플레이'] == 5.5

print(iphone_df.dtypes)

iphone_df.loc[iphone_df['디스플레이'] == 5.5] = 'z'

iphone_df

iphone_df[['디스플레이', 'Face ID']] = 'x'

iphone_df

iphone_df.loc[['iPhone 7', 'iPhone X']]

iphone_df.loc[['iPhone 7', 'iPhone X']] = 'o'

iphone_df

iphone_df.loc['iPhone 7' : 'iPhone X']

iphone_df.loc['iPhone 7' : 'iPhone X'] = 'o'  # loc는 데이터 프레임 행열 명대로 사용

iphone_df

iphone_df.iloc[[1, 3], [1, 4]]  # iloc는 꼭 숫자 좌표로 해야함

iphone_df.iloc[[1, 3], [1, 4]] = 'v'

iphone_df.loc['HJ phone'] = ['2021-09-24', 9.0, '256GB', 'iOS 99.0', 'YES']
iphone_df

iphone_df['제조사'] = 'Apple'
iphone_df

iphone_df.drop('HJ phone', axis='index', inplace=False)
iphone_df

iphone_df.drop('HJ phone', axis='index', inplace=True)
iphone_df

iphone_df.drop('제조사', axis='columns', inplace=True)
iphone_df

iphone_df.drop(['iPhone 7', 'iPhone X', 'iPhone XS Max'], axis='index', inplace=True)
iphone_df


