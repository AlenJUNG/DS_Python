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

# # From list of dicts

# - 리스트가 담긴 사전이 아니라, 사전이 담긴 리스트로도 DataFrame을 만들 수 있음

import pandas as pd
import numpy as np

my_list = [
    {'name' : 'dongwook', 'english_score' : 50, 'math_score' : 86},
    {'name' : 'sineui', 'english_score' : 89, 'math_score' : 31},
    {'name' : 'ikjoong', 'english_score' : 68, 'math_score' : 91},
    {'name' : 'yoonsoo', 'english_score' : 88, 'math_score' : 75}
]

df = pd.DataFrame(my_list)

print(df)

print(df.dtypes)


