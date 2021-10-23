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

# # Pandas로 데이터 읽어들이기

# - option 확인

import numpy as np
import pandas as pd

iphone_df = pd.read_csv('data/iphone.csv')

iphone_df

type(iphone_df)

print(iphone_df.dtypes)

iphone_df2 = pd.read_csv('data/iphone.csv', header=None)

iphone_df2

type(iphone_df2)

print(iphone_df2.dtypes)

iphone_df3 = pd.read_csv('data/iphone.csv', index_col=0)

iphone_df3

type(iphone_df3)

print(iphone_df3.dtypes)


