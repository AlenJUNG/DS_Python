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

# +
import numpy as np

array1 = np.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31])
array1
# -

type(array1)

array1.shape

array1.size

array2 = np.random.random(8)
array2

array3 = np.arange(2, 8, 2)

array3

array4 = np.arange(1, 9)
array4

array4[2:3] # 인덱싱과 슬라이싱은 대괄호 안에서 진행

for i in range(10):
    i += 1
    print(i)

array5 = np.full(10, 2)
array5

array1 = np.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31])

filter = np.where(array1 > 4) # 핵심코드

array1[filter]

array1.max()

array1.min()

array1.mean()

array1.std()

array1.var()

np.median(array1)

filter = np.where(array1 > 6)

array1[filter]

# +
import numpy as np 

revenue_in_yen = [ 300000, 340000, 320000, 360000, 440000, 140000, 180000, 340000, 330000, 290000, 280000, 380000, 
                  170000, 140000, 230000, 390000, 400000, 350000, 380000, 150000, 110000, 240000, 380000, 380000, 340000, 
                  420000, 150000, 130000, 360000, 320000, 250000 ]
# -

yen = np.array(revenue_in_yen)

filter = np.where(yen <= 200000)

yen[filter]


