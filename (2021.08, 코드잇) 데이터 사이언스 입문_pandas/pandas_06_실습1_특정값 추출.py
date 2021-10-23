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

# # 특정 열만 추출하기

# - data/broadcast.txt 이용

import numpy as np
import pandas as pd

df = pd.read_table('data/broadcast.txt', sep=',', index_col=0)

df

df.loc[2016, 'KBS']

type(df)

print(df.dtypes)

df.loc[:, ['KBS', 'SBS']]   #특정 컬럼들만 추출하기

condition = df['KBS'] > 30

df[condition]

df.loc[condition, ['KBS']]

condition2 = df['SBS'] < df['TV CHOSUN']

df.loc[condition2, ['SBS', 'TV CHOSUN']]


