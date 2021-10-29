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

# # numpy의 ndarray의 데이터 세트 선택하기 - 인덱싱(Indexing)
# 1. 특정한 데이터만 추출 : 원하는 위치의 인덱스 값을 지정하면 해당 위치의 데이터 반환
# 1. 슬라이싱 : 연속된 인덱스상 ndarray를 추출
# 1. 팬시 인덱싱 : 일정한 인덱싱 집합을 리스트 or ndarray 형태로 지정해 해당 위치의 ndarray를 반환
# 1. 불린 인덱싱 : 특정 조건에 해당하는 여부 True/False 값 인덱싱 집합 기반으로 반환 

# +
# 1부터 9까지의 1차원 ndarray 생성

array1 = np.arange(start=1, stop=10)
print('array1:', array1)

# +
# index는 0부터 시작하므로 array1[2]는 3번째 index 위치의 데이터값을 의미

value = array1[2]
print('value:', value)
print(type(value))
# -

print('맨 뒤의 값:', array1[-1], '맨 뒤에서 두번째 값:', array1[-2])

# +
# 단일 인덱스를 이용 ndarray 내 데이터값 수정

array1[0] = 9
array1[8] = 0
print('array1:', array1)
# -

# ## 다차원 ndarray에서 단일값 추출
# > axis 0이 로우 방향축, axis 1이 컬럼 방향축, default는 axis 0

array1d = np.arange(start=1, stop=10)
array2d = array1d.reshape(3, 3)
print(array2d)

print('(row=0, col=0) index 가리키는 값:', array2d[0,0])
print('(row=0, col=1) index 가리키는 값:', array2d[0,1])
print('(row=1, col=0) index 가리키는 값:', array2d[1,0])
print('(row=2, col=2) index 가리키는 값:', array2d[2,2])

# ## 슬라이싱
# - 단일 데이터값 추출을 제외한 슬라이싱, 팬시 인덱싱, 불린 인덱싱으로 추출된 데이터 세트는 모두 ndarray type

array1 = np.arange(start=1, stop=10)
array3 = array1[0:3]
print(array3)
print(type(array3))

array1 = np.arange(start=1, stop=10)
array4 = array1[:3]
print(array4)

array5 = array1[3:]
print(array5)

array6 = array1[:]
print(array6)

array1d = np.arange(start=1, stop=10)
array2d = array1.reshape(3, 3)
print('array3d:\n', array2d)

print('array2d[0:2] \n', array2d[0:2, 0:2])

# ## 2차원 슬라이싱
# > row, column
# - ex) [0:2, 0:2] 는 row 0:2 , column 0:2 를 의미

print('array2d[0:2, 0:2] \n', array2d[0:2, 0:2])
print('array2d[1:3, 0:3] \n', array2d[1:3, 0:3])
print('array2d[1:3, :] \n', array2d[1:3, :])
print('array2d[:, :] \n', array2d[:, :])
print('array2d[:2, 1:] \n', array2d[:2, 1:])
print('array2d[:2, 0] \n', array2d[:2, 0])

# ## 만약 2차원 ndarray에서 뒤에 오는 인덱스를 없애면 1차원 ndarray를 반환함
# - row 단위 반환

print(array2d[0])

print(array2d[1])

print('array2d[0] shape:', array2d[0].shape, 'array2d[1] shape:', array2d[1].shape)

# ## 팬시 인덱싱
# - 리스트나 ndarray로 인덱스 집합을 지정하면 해당 위치의 인덱스에 해당하는 ndarray를 반환하는 인덱싱 방식

array1d = np.arange(start=1, stop=10)
array2d = array1d.reshape(3, 3)
array2d

array3 = array2d[[0, 1], 2]
print('array2d[[0, 1], 2] => ', array3.tolist())

array4 = array2d[[0, 1], 0:2]
print('array2d[[0, 1], 0:2] => ', array4.tolist())

array5 = array2d[[0, 1]]
print('array2d[[0, 1], 2] => ', array5.tolist())


