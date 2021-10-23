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

# - numpy 모듈의 array 메소드에 파라미터로 파이썬 리스트를 넘겨주면 numpy array가 리턴됌

array1 = np.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31])
array1

type(array1)

array1.shape

array1.size

array2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

type(array2)

array2.shape

array2

array2.size

array3 = np.full(6, 7) # full 메소드 : 6개 7을 균일하게 넣음
array3

# #### numpy의 random 모듈의 random 함수 사용
# - numpy 모듈 안에 random 모듈이 있고, 그 안에 또 random 함수가 있음

# +
array1 = np.random.random(6)
array2 = np.random.random(6)

print(array1)
print()
print(array2)
# -

# ## arange : 연속된 값들이 담긴 numpy array
# - Python의 range와 비슷한 원리
# - 파라미터의 수에 따라 조금씩 달라짐

array1 = np.arange(6) # 0부터 6까지 넣음
array1

array2 = np.arange(2, 7) # 2부터 7-1 까지 넣음
array2

array3 = np.arange(3, 17, 3) # 3부터 17 미만까지 넣는데 3배수로 넣음
array3

x = np.arange(1, 101, 3)
x

# # 인덱싱

array1 = np.array([2, 3, 5, 6, 11, 13, 17, 19 ,23 ,29, 31])

array1[0]

array1[-1]

array1[-2]

array1[[1, 3, 5]] # 여러 숫자를 호출할 때는 대괄호 안에 괄호로 호출한다.

array2 = np.array([2, 1, 3])

array1[array2]

# # 슬라이싱

array1[2:7]

array1[0:7]

array1[:4]

array1[3:]

array1[2:11:2] # 2의 배수로 호출

array1[2:11:3] # 3의 배수로 호출



array1 = np.arange(10)
array2 = np.arange(10, 20)

array1

array2

for i in range(len(array1)):
    array1[i] = 2 * array1[i]    

array1

array1 * 2

array1 / 2

array1 + 2

array1 ** 2

# #### 중요 : 위는 저장되지 않았다

array1 # 저장되지 않음을 확인

array1 *= 2 # 값을 넣어줘야 최종 저장 된다
array1

array1 + array2

array1 * array2

array1 / array2

# ## 실습과제 : 신주쿠 흥부부대찌개

import numpy as np 
revenue_in_yen = [ 300000, 340000, 320000, 360000, 440000, 140000, 180000, 340000, 330000, 290000, 280000, 380000, 170000, 140000, 230000, 390000, 400000, 350000, 380000, 150000, 110000, 240000, 380000, 380000, 340000, 420000, 150000, 130000, 360000, 320000, 250000 ]
revenue_in_yen = np.array(revenue_in_yen)

won = np.full(31, 10.08)

won = won * revenue_in_yen

won

# ## Numpy boolean 연산 : np.where(booleans)

array1 = np.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31])

array1 > 4

array1 % 2 == 0

booleans = np.array([True, True, False, True, True, False, True, True, True, False, True])

np.where(booleans) # True인 값은 어디에 있나?

np.where(array1 > 4)

filter = np.where(array1 > 4) # array1에서 4보다 큰값, 즉 filter하고 싶은 조건 저장
filter

array1[filter] # 중요 : 필터를 걸 때는 대괄호 안으로 건다.

# ## Numpy 라이브러리 기본 통계 기능

array1.max()

array1.min()

array1.mean() # 평균

array1.std() # 표준편차

array1.var() # 분산

# - 특이하게 median은 numpy array의 메소드가 아니라 numpy의 메소드임

np.median(array1) # 중앙값

# ## 실습과제 : Numpy boolean 연산
# - 20만엔 이하의 매출만 담긴 numpy array 출력

# +
import numpy as np 

revenue_in_yen = [ 300000, 340000, 320000, 360000, 440000, 140000, 180000, 340000, 330000, 290000, 280000, 380000, 
                  170000, 140000, 230000, 390000, 400000, 350000, 380000, 150000, 110000, 240000, 380000, 380000, 340000, 
                  420000, 150000, 130000, 360000, 320000, 250000 ]
# -

yen = np.array(revenue_in_yen)

filter = np.where(yen <= 200000)
yen[filter]


