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

# # DataFrame을 만드는 다양한 방법 

# - dictionary로도 DataFrame을 만들 수 있음

import numpy as np
import pandas as pd

names = ['dongwook', 'sineui', 'ikjoong', 'yoonsoo']
english_scores = [50, 89, 68, 88]
math_scores = [86, 31, 91, 75]

dict1 = {
    'name' : names,
    'english_score' : english_scores,
    'math_score' : math_scores
}

dict2 = {
    'name' : np.array(names),
    'english_score' : np.array(english_scores),
    'math_score' : np.array(math_scores)
}

dict3 = {
    'name' : pd.Series(names),
    'english_score' : pd.Series(english_scores),
    'math_score' : pd.Series(math_scores)
}

df1 = pd.DataFrame(dict1)

df2 = pd.DataFrame(dict2)

df3 = pd.DataFrame(dict3)

print(df1)

print(df2)

print(df3)


