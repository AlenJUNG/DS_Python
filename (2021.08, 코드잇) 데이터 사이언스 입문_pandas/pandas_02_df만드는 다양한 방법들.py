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

#  # 2차원 리스트나 2차원 numpy array로 DataFrame을 만들 수 있음
#  1. list를 DF
#  2. numpy array를 DF
#  3. pandas series를 F

# #### import numpy as np
# import pandas as pd

two_dimensional_list = [['dongwook', 50, 86], ['sineui', 86, 31], ['ikjoong', 68, 91], ['yoonsoo', 88, 75]]

two_dimensional_array = np.array(two_dimensional_list)

# - 1차원 pandas > Series

list_of_series = [
    pd.Series(['dongwook', 50, 86]),
    pd.Series(['sineui', 86, 31]),
    pd.Series(['ikjoong', 68, 91]),
    pd.Series(['yoonsoo', 88, 75]),
]

# 리스트를 df화
df1 = pd.DataFrame(two_dimensional_list)

# numpy array를 df화
df2 = pd.DataFrame(two_dimensional_array)

# series를 df화
df3 = pd.DataFrame(list_of_series)

print(df1)

print(df2)

print(df3)


