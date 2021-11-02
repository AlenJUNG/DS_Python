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
import numpy as np

df = pd.read_csv(r'C:\Users\Administrator\DS_Python\data\titanic\train.csv')


# # apply lambda 식으로 데이터 가공

# +
def get_squared(a):
    return a**2

print('3의 제곱은:', get_squared(3))

# +
lambda_square = lambda x : x**2

print('3의 제곱은:', lambda_square(3))
# -

# ### lambda : 함수의 선언과 처리를 한 줄의 식으로 쉽게 변환하는 식
# > lambda 입력인자 : 입력인자의 계산식(반환값)
# - 여러 개의 값을 입력 인자로 사용해야할 경우에는 보통 map() 함수를 결합해서 사용

a = [1, 2, 3]
squares = map(lambda x : x**2, a)
list(squares)

df['Name_len'] = df['Name'].apply(lambda x : len(x))
df[['Name', 'Name_len']].head(3)

# ### if else 절 사용 시, 좌우 구분 주의

# +
# Q) 나이가 15세 미만이면 Child 그렇지 않으면 Adult로 구분하는 새로운 컬럼 Child_Adult를 apply lambda를 이용해 생성

df['Child_Adult'] = df['Age'].apply(lambda x : 'Child' if x <= 15 else 'Adult')
df[['Age', 'Child_Adult']].head(8)
# -

# ### else if를 이용하려면 else절을 ()로 내포해 () 내에서 다시 if else를 적용해 사용
# - Q) 나이가 15세 이하이면 Child, 15 ~ 60세는 Adult, 61세 이상은 Elderly로 불류하는 'Age_Cat' 컬럼을 만들어라

df['Age_cat'] = df['Age'].apply(lambda x : 'Child' if x <= 15 else ('Adult' if x <= 60 else 'Elderly'))
df['Age_cat'].value_counts()


# ### else if가 많이 나와야하는 경우 별도 함수가 더 나을 수 있음
# - Q) 5살 이하는 Baby, 12살 이하는 Child, 18살 이하는 Teenage, 25살 이하는 Student, 35살 이하는 Young Adult, 60세 이하는 Adult, 그 이상은 Elderly

# 나이에 따라 세분화된 분류를 수행하는 함수 생성
def get_category(age):
    cat=''
    
    if age <= 5: cat = 'Baby'
    elif age <= 12: cat = 'Child'
    elif age <= 18: cat = 'Teenage'
    elif age <= 25: cat = 'Student'
    elif age <= 35: cat = 'Young Adult'
    elif age <= 60: cat = 'Adult'
    else: cat = 'Elderly'
        
    return cat


# +
# lambda 식에서 위에 생성한 get_category() 함수를 반환값으로 지정
# get_category(x)는 입력값으로 'Age' 컬럼값을 받아서 해당하는 cat 반환

df['Age_cat'] = df['Age'].apply(lambda x : get_category(x))
df[['Age', 'Age_cat']].head()
# -


