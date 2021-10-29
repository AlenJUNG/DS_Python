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

# # Numpy 개요

import numpy as np

# - ndarray.shape : ndarray의 차원과 크기를 튜플 형태로 나타내 줌. 

# +
array1 = np.array([1, 2, 3])
print('array1 type:', type(array1))

# 행과 열의 수를 튜플 형태로 가지고 있으며 ndarray의 차원까지 알 수 있음
print('array1 array 형태 :', array1.shape) # 1차원

# +
array2 = np.array([[1, 2, 3],
                  [2, 3, 4]])

print('array2 type:', type(array2))
print('array2 array 형태 :', array2.shape) # 2차원

# +
# 1개의 로우와 3개의 컬럼으로 구성된 2차원 데이터를 의미
array3 = np.array([[1, 2, 3]])

print('array3 type:', type(array3))
print('array3 array 형태 :', array3.shape)

# +
# 각 array의 차원을 ndarray.ndim을 이용해 확인

print('array1: {:0}차원, array2: {:1}차원, array3: {:2}차원'.format(array1.ndim, array2.ndim, array3.ndim))
# -

# # ndarray의 데이터 타입
# - ndarray 내 데이터 값은 연산의 특성상 같은 데이터 타입만 가능
#   - 한 개의 ndarray 객체에 int와 float가 함께 있을 수 없음
#   - 데이터 타입 확인 > dtype

list1 = [1, 2, 3]
print(type(list1))

array1 = np.array(list1)
print(type(array1))
print(array1, array1.dtype)

# ## ndarray 내 데이터 타입은 연산의 특성상 같은 데이터 타입만 가능
# - 만약 데이터 유형이 섞여 있다면 데이터 크기가 더 큰 데이터 타입으로 일괄 형변환 적용하게 됌

list2 = [1, 2, 'test']
array2 = np.array(list2)
print(array2, array2.dtype)

# ### 1, 2가 문자열로 변경되었음

list3 = [1, 2, 3.0]
array3 = np.array(list3)
print(array3, array3.dtype)

# ### 1, 2가 float 형으로 변경되었음

# > 형변환은 astype 사용

array_int = np.array([1, 2, 3])
array_float = array_int.astype('float64')
print(array_float, array_float.dtype)

array_int1 = array_float.astype('int32')
print(array_int1, array_int1.dtype)

array_float1 = np.array([1.1, 2.1, 3.1])
array_int2 = array_float1.astype('int32')
print(array_int2, array_int2.dtype)

# # ndarray를 편리하게 생성하기 - arange, zeros, ones

# +
# 파이썬의 range와 유사

sequence_array = np.arange(10)
print(sequence_array)
print(sequence_array.dtype, sequence_array.shape)

# +
# 모든 값을 0으로 채운 해당 shape을 가진 ndarray를 반환

zero_array = np.zeros((3, 2), dtype='int32')
print(zero_array)
print(zero_array.dtype, zero_array.shape)

# +
# 모든 값을 1로 채운 ndarray를 반환
# 함수 인자로 dtype을 설정해주지 않으면 default는 float64로 채움

one_array = np.ones((3, 2))
print(one_array)
print(one_array.dtype, one_array.shape)
# -

# # ndarray의 차원과 크기를 변경하는 reshape()
# - 지정된 사이즈로 변경이 불가능하면 오류가 발생함

array1 = np.arange(10)
print('array1:\n', array1)

array2 = array1.reshape(2, 5)
print('array2:\n', array2)

array3 = array1.reshape(5, 2)
print('array3:\n', array3)

array1.reshape(4, 3) # 지정된 사이즈로 변경 불가

# ## -1 인자의 활용
# > -1이 아닌 옆에 인자에 맞추어 reshape

array1 = np.arange(10)
print(array1)

array2 = array1.reshape(-1, 5)
print('array2 shape:', array2.shape)

array2

array3 = array1.reshape(5, -1)
print('array3 shape:', array3.shape)

array3

# ## -1인자는 reshape(-1, 1) 형태로 자주 사용
# - 원본 ndarray가 어떤 형태라도 2차원이고 여러 개의 로우를 가지되 반드시 1개의 컬럼을 가진 ndarray로 변환됨을 보장
# - 여러 개의 numpy ndarray는 stack이나 concat으로 결합할 때 각각의 ndarray의 형태로 통일해 유용하게 사용
# - ndarray는 tolist() 메서드를 이용해 리스트 자료형으로 변환
#   - list는 행으로 계속 연결되어 출력, ndarray는 행열을 지키며 출력된다 < 차이점 알기

array1 = np.arange(8)
array3d = array1.reshape((2, 2, 2))

array3d # 3차원

print('array3d:\n', array3d.tolist())

# +
# 3차원 ndarray를 2차원 ndarray로 변환

array5 = array3d.reshape(-1, 1)
print('array5:\n', array5.tolist())
print('array5 shape:', array5.shape)

# +
# 1차원 ndarray를 2차원 ndarray로 변환

array6 = array1.reshape(-1, 1)
print('array6:\n', array6.tolist())
print('array6 shape:', array6.shape)
# -


