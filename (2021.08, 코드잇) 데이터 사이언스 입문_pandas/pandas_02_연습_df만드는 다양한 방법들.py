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

# - 대문자 주의

import numpy as np
import pandas as pd

list = [['dongwook', 50, 86], ['sineui', 86, 31], ['ikjoong', 68, 91], ['yoonsoo', 88, 75]]

arr = np.array(list)
dfx = pd.read_table

# 대문자 주의
seri = [
    pd.Series(['dongwook', 50, 86]),
    pd.Series(['sineui', 86, 31]),
    pd.Series(['ikjoong', 68, 91]),
    pd.Series(['yoonsoo', 88, 75])
]

df1 = pd.DataFrame(list)
df2 = pd.DataFrame(arr)
df3 = pd.DataFrame(seri)

df1

df2

df3

names = ['dongwook', 'sineui', 'ikjoong','yoonsoo']
english_scores = [50, 89, 68 ,88]
math_scores = [86, 31, 91, 75]

dic1 = {
    'name' : names,
    'english_score' : english_scores,
    'math_score' : math_scores
}

dic2 = {
    'name' : np.array(names),
    'english_score' : np.array(english_scores),
    'math_score' : np.array(math_scores)
}

dic3 = {
    'name' : pd.Series(names),
    'english_score' : pd.Series(english_scores),
    'math_score' : pd.Series(math_scores)
}

df_dic1 = pd.DataFrame(dic1)
df_dic2 = pd.DataFrame(dic2)
df_dic3 = pd.DataFrame(dic3)

df_dic1

df_dic2

df_dic3


