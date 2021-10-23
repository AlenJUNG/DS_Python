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

# # 조건에 따라 column 변경하기

#

import numpy as np
import pandas as pd

df = pd.read_table('data/toeic.txt', sep=',')
df

df['합격 여부'] = 'O'

df

total = df['LC'] + df['RC'] > 600
each = (df['LC'] >= 250) & (df['RC'] >= 250)

df['합격 여부'] = total & each
df


