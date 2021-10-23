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







import numpy as np
import pandas as pd

df = pd.read_csv('data/iphone.csv', index_col=0)

df

df.rename(columns={'출시일' : 'New'})

df

df.rename(columns= {'출시일' : 'New'}, inplace=True)

df

df.rename(columns= {'New' : '출시일'}, inplace=True)

df

df.index.name = 'iPhone 종류'

df

df['iPhone 종류'] = df.index

df.set_index('메모리', inplace=True)

df

df.set_index('iPhone 종류', inplace=True)


