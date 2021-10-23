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

df = pd.read_table('data/body_imperial1.txt', sep=',', index_col=0)

df

df.iloc[1, 1] = 200
df

df.drop(21, axis='index', inplace=True)
df

df.loc[20] = [70, 200]
df

df['비만도'] = '정상'

df

df.loc[:10,'비만도'] = '비정상'

df


