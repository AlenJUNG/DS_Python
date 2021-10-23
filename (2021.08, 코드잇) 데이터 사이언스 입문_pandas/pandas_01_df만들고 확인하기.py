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

import pandas as pd

# - pandas는 숫자형, 문자형 자료형 가능

# list 먼저 만들고
two_dimensional_list = [['dongwook', 50, 86],['sineui', 89, 31],['ikjoong', 68, 91],['yoonsoo', 88, 75]]

# df화 하기
my_df = pd.DataFrame(two_dimensional_list)

my_df

type(my_df)

my_df.columns

my_df.index

# 데이터타입
my_df.dtypes


