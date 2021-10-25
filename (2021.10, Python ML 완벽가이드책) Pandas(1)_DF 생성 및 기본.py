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

# # Pandas의 핵심 객체는 DataFrame
# - DF : 여러 개의 행과 열로 이루어진 2차원 데이터를 담는 데이터 구조체
# - Index : 개별 데이터를 고유하게 식별하는 Key 값
# - Series와 DataFrame은 모두 Index를 key 값으로 가지고 있음
# - Series vs DataFrame
#   - Series는 칼럼이 하나뿐인 데이터 구조체, DataFrame은 칼럼이 여러 개인 데이터 구조체
#   - DataFrame은 여러 개의 Series로 이루어져 있음

import pandas as pd

df = pd.read_csv(r'C:\Users\Administrator\DS_Python\data\titanic\train.csv')

# - read_csv()는 csv뿐 아니라 어떤 필드 구분 문자 기반의 파일 포맷도 DataFrame으로 변환 가능
# - 탭으로 필드가 구분되어 있다면 read_csv('파일명', sep = '\t')
# - sep 인자를 생략하면 자동으로 콤마로 할당

df.head(3)

type(df)

print('변수 type : ', type(df))

df.shape # DF의 행과 열 크기를 알아보는 가장 좋은 방법 = shape

df.info() # 총 데이터 건수 및 타입, Null 건수를 알 수 있음

df.describe() # 오직 숫자형 컬럼의 분포도 조사 > 문자형은 자동으로 출력 제외

value_counts = df['Pclass'].value_counts() # 지정된 컬럼의 데이터 건수를 반환
print(value_counts)

type(df['Pclass'])

# ## DF와 리스트, 딕셔너리 넘파이 ndarray 상호 변환

# ### 넘파이 ndarray, 리스트, 딕셔너리를 DF로 변환하기
# - DF는 리스트와 넘파이 ndarray와는 다르게 칼럼명을 가지고 있음 > 상대적으로 편하게 데이터 핸들링 가능

# #### 1차원 DF 생성

# +
import numpy as np

col_name1 = ['col1']
list1 = [1, 2, 3]
array1 = np.array(list1)
# -

print('array1 shape:', array1.shape)

# 리스트를 이용해서 DF 생성
df_list1 = pd.DataFrame(list1, columns=col_name1)
print('1차원 리스트로 만든 DF:\n', df_list1)

# Numpy ndarray를 이용해 DF 생성
df_array1 = pd.DataFrame(array1, columns=col_name1)
print('1차원 ndarray로 만든 DF:\n', df_array1)

# +
col_name = ['col1', 'col2', 'col3']

list2 = [[1, 2, 3],
         [11, 22, 33]]
array2 = np.array(list2)
print('array2 shape:', array2.shape)
# -

df_list2 = pd.DataFrame(list2, columns=col_name)
print('2차원 리스트로 만든 DF:\n',df_list2)

df_array2 = pd.DataFrame(array2, columns=col_name)
print('2차원 array로 만든 DF:\n', df_array2)

# #### 딕셔너리를 DF로 변환
# - 일반적으로 딕셔너리의 key는 컬럼명, value는 키에 해당하는 컬럼 데이터로 변환된다
# - So, 키의 경우는 문자열, 값의 경우는 리스트 or ndarray 형태로 딕셔너리 구성

# Key는 문자열 컬럼명으로 매핑, Value는 리스트형 or ndarray 컬럼 데이터로 매핑
dict = {'col1':[1, 11], 'col2':[2, 22], 'col3':[3,33]}
df_dict = pd.DataFrame(dict)
print('딕셔너리를 만든 DF:\n', df_dict)

# ## DataFrame을 넘파이 ndarray, 리스트, 딕셔너리로 변환하기
# - 많은 ML 패키지가 기본 데이터 형으로 numpy ndarray를 사용하기 때문에 데이터 핸들링은 DF를 사용하더라도 재변환 필요
# - DF를 numpy ndarray로 변환하는 것은 DF 객체의 values를 이용해 쉽게 가능

# +
# DF를 ndarray로 변환

array3 = df_dict.values
print('df_dict.values 타입:', type(array3), 'df_dict.values shape:', array3.shape)
# -

print(array3)

# +
# DataFrame을 리스트로 변환 : values로 얻은 ndarray에 tolist()를 호출

list3 = df_dict.values.tolist()
print('df_dict.values.tolist() 타입:', type(list3))
# -

print(list3)

# +
# DataFrame을 딕셔너리로 변환 : DF 객체의 to_dict()메서드를 호출하는데 인자로 'list'를 입력

dict3 = df_dict.to_dict('list')
print('\n df_dict.to_dict() 타입:', type(dict3))
# -

print(dict3)

# ## DataFrame의 컬럼 데이터 세트 생성과 수정

df['Age'] = 0 # Age 컬럼 Series에 일괄 0 할당
df.head()

df = pd.read_csv(r'C:\Users\Administrator\DS_Python\data\titanic\train.csv')

df['Age_by_10'] = df['Age'] * 10
df['Family_No'] = df['SibSp'] + df['Parch'] + 1

df.head()

df.head()

# #### DataFrame 데이터 삭제
# - 가장 중요한 파라미터 : labels, axis, inplace
# - axis=0 : 로우 방향축, axis=1 : 컬럼 방향축
# - labels : 두 개 이상 컬럼을 삭제 시에는 대괄호 안에 따옴표 처리 (ex: drop_result = df.drop(['Age_by_10', 'Family_No'], axis=1, inplace=True)
# > drop(inplace=True) 설정 시, 반환값이 None이 되므로 반환값을 자신의 DF로 할당하면 안된다

drop_df = df.drop('Age_by_10', axis=1)
drop_df.head(3)

df.head(3)

drop_result = df.drop(['Age_by_10', 'Family_No'], axis=1, inplace=True)
print('inplace=True 로 drop 후 반환된 값:', drop_result)
df.head(3)

pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 15)
print('### before axis 0 drop ####')
print(df.head(3))

# +
# Index 0, 1, 2에 위치한 로우를 삭제
df.drop([0, 1, 2], axis=0, inplace=True)

print('### after axis 0 drop ####')
print(df.head(3))
# -

# - axis : DF의 로우를 삭제할 때는 0, 컬럼을 삭제할 때는 1로 설정
# - 원본 DF는 유지하고 드롭된 DF를 새롭게 객체 변수로 받고 싶다면 inplace=False로 설정(디폴트 False)
# - 원본 DF에 드롭된 결과를 적용할 경우에는 inplace=True를 적용


