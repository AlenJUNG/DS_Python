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

# # 불린 인덱싱
# - 조건 필터링과 검색을 동시에 함
# - 불린 인덱싱은 ndarray의 인덱스를 지정하는 [] 내 조건문을 그대로 기재하면 된다
# - how to
#   1. array1d > 5 와 같이 ndarray의 필터링 조건을 [ ] 안에 기재
#   1. True값을 가진 인덱스만 저장
#   1. 저장된 인덱스 데이터 세트로 ndarray 조회

array1d = np.arange(start=1, stop=10)
array1d > 5

# [ ] 안에 array1d > 5 Boolean indexing을 적용
array3 = array1d[array1d > 5] # array1d에서 5보다 큰 값을 = True값만 array1d 전체에서 반환함
print('array1d > 5 boolean indexing :', array3)

# # 행렬의 정렬 - sort()와 argsort()
# - numpy sort() 방식 : 원본행렬은 그대로 유지
# - ndarray.sort() 방식 : 원본행렬 자체를 정렬하며 반환 값은 None

org_array = np.array([3, 1, 9, 5])
print('원본 행렬:', org_array)

# +
# np.sort()로 정렬

sort_array1 = np.sort(org_array)
print('np.sort() 호출 후 반환된 정렬 행렬:', sort_array1)
print('np.sort() 호출 후 원본 행렬:', org_array)

# +
# ndarray.sort()로 정렬

sort_array2 = org_array.sort()
print('org_array.sort() 호출 후 반환된 행렬:', sort_array2)
print('org_array.sort() 호출 후 원본 행렬:', org_array)
# -

# ### 내림차순으로 정렬하기 위해서는 [::-1] 를 적용
# > np.sort()[::-1]

sort_array1_desc = np.sort(org_array)[::-1]
print('내림차순으로 정렬:', sort_array1_desc)

# ### 행렬이 2차원 이상일 경우 axis 축 값 설정을 통해 방향 정렬 수행
# - axis=0 : 행끼리 정렬
# - axis=1 : 열끼리 정렬

# +
array2d = np.array([[8, 12],
                   [7, 1]])

sort_array2d_axis0 = np.sort(array2d, axis=0)
print('로우 방향으로 정렬:\n', sort_array2d_axis0)

sort_array2d_axis1 = np.sort(array2d, axis=1)
print('컬럼 방향으로 정렬:\n', sort_array2d_axis1)
# -

# ### 행렬 정렬 시, 원본 행렬의 인덱스 변화를 미리 알아보기

org_array = np.array([3, 1, 9, 5])
sort_indices = np.argsort(org_array)
print(type(sort_indices))
print('행렬 정렬 시 원본 행렬의 인덱스:', sort_indices)

org_array = np.array([3, 1, 9 ,5])
sort_indices_desc = np.argsort(org_array)[::-1]
print('행렬 내림차순 정렬 시 원본 행렬의 인덱스:', sort_indices_desc)

# ### argsort()의 높은 활용도
# - 실제 값과 그 값이 뜻하는 메타 데이터를 별도의 ndarray에 별도로 가져가서 활용해야 함

# +
name_array = np.array(['John', 'Mike', 'Sarah', 'Kate', 'Samuel'])
score_array = np.array([78, 95, 84, 98, 88])

sort_indices_asc = np.argsort(score_array)
print('성적 오름차순 정렬 시 score_array의 인덱스:', sort_indices_asc)
print('성적 오름차순으로 name_array의 이름 출력:', name_array[sort_indices_asc])
# -

# # 선형대수 - 행렬 내적과 전치 행렬 구하기
# ### 행렬 내적 : 행렬 곱
# > np.dot( )

# +
A = np.array([[1, 2, 3],
              [4, 5, 6]])
B = np.array([[7, 8],
              [9, 10],
              [11, 12]])

dot_product = np.dot(A, B)
print('행렬 내적 결과:\n', dot_product)
# -

# ### 전치 행렬 : 원본 행렬에서 행과 열 위치를 교환한 원소로 구성한 행렬 
# > np.transpose()

A = np.array([[1, 2],
              [3, 4]])
transpose_mat = np.transpose(A)
print('A의 전치 행렬:\n', transpose_mat)


