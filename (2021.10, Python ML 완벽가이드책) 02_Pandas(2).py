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

# # Index 객체
# - 한 번 만들어진 DF 및 Series의 Index 객체는 함부로 변경 불가
# - Series 객체는 Index 객체를 포함하지만 Series 객체에 연산 함수를 적용할 때 Index는 연산에서 제외됌
# - Index는 오직 식별용으로만 사용된다

import pandas as pd
import numpy as np

df = pd.read_csv(r'C:\Users\Administrator\DS_Python\data\titanic\train.csv')

df.head(3)

indexes = df.index # 인덱스 객체 추출
print(indexes)
print('Index 객체 array값:\n', indexes.values)

print(type(indexes.values))
print(indexes.values.shape)
print(indexes[:5].values)
print(indexes.values[:5])
print(indexes[6])

series_fair = df['Fare']
print('Fair Series max 값:', series_fair.max())
print('Fair Series sum 값:', series_fair.sum())
print('sum() Fair Series:', sum(series_fair))
print('Fair Series + 3:\n', (series_fair + 3).head(3))

# - reset_index() 메서드를 수행하면 새롭게 인덱스를 연속 숫자형으로 할당하며 기존 인덱스는 'index'라는 새로운 컬럼명으로 추가함
# - 인덱스가 연속된 int 숫자형 데이터가 아닐 경우에 주로 사용
# - reset_index()의 파라메터 중 drop=True로 설정하면 기존 인덱스는 신규 컬럼으로 추가되지 않고 drop 됌
#   > 이 경우 새로운 컬럼으로 추가되지 않으므로 그대로 Series로 유지
# - 주의 : Series에 reset_index()를 적용하면 Series가 아닌 DataFrame이 반환되니 주의

reset_df = df.reset_index(inplace=False)
reset_df.head(3)

# +
print('### before reset_index ###')
value_counts = df['Pclass'].value_counts()
print(value_counts)
print('value_counts 객체 변수 타입:', type(value_counts))
new_value_counts = value_counts.reset_index(inplace=False)    

print('\n### After reset_index ###')
print(new_value_counts)
print('new_value_counts 객체 변수 타입:', type(new_value_counts))
# -

# ## 데이터 셀렉션 및 필터링
# - Pandas vs Numpy 헷갈리므로 주의
#   - Numpy : [] 연산자 내 단일 값 추출, 슬라이싱, 팬시 인덱싱, 불린 인덱싱을 통해 데이터 추출
#   - Pandas : ix[], iloc[], loc[] 연산자를 통해 동일 작업 수행

print('단일 컬럼 데이터 추출:\n', df['Pclass'].head(3))

print('여러 컬럼의 데이터 추출:\n', df[['Survived','Pclass']].head(3))

print('[]안에 숫자 index는 keyError 오류 발생:\n', df[0])

# 단일 숫자는 안되지만 Pandas의 인덱스 형태로 변환 가능한 표현식은 []에 입력 가능
df[0:2]

# [] 내 불린 인덱싱 기능은 사용 가능
df[df['Pclass'] == 3].head(3)

# ### DataFrame[ ] 혼돈 방지 가이드
# - DF 바로 뒤의 []연산자는 numpy[]와 Series[]가 다르다.
# - DF 바로 뒤의 [] 내 입력값은 컬럼명 or 컬럼의 리스트를 지정해 사용하거나 불린 인덱스 용도로만 사용해야함
# - DataFrame[0:3]과 같은 슬라이싱 연산으로 데이터를 추출하는 방법은 비추

# - loc[] : 컬럼 명칭 기반 인덱싱 연산자
# - iloc[] : 컬럼 위치 기반 인덱싱 연산자


