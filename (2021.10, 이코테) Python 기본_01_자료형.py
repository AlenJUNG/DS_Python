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

# # 수 자료형

# ## 정수형

a = 1000
print(a)

a = -7
print(a)

# ## 실수형

a = 5.
print(a) # 소수부가 0일 때 0을 생략

a = -.7
print(a) # 정수부가 0일 때 0을 생략

a = 1e9 # 10억의 지수 표현 방식
print(a)

a = 0.3 + 0.6
print(a)

# 컴퓨터가 실수를 정확히 표현하지 못한다
if a == 0.9:
    print(True)
else:
    print(False)

# +
# 실수형 데이터 연산 시, round 함수 사용
a = 0.3 + 0.6
print(round(a, 4))

if round(a, 4) == 0.9:
    print(True)
else:
    print(False)
# -

b = 2
b = b **3
print(a)

# ## 리스트 자료형

# 크기가 N이고, 모든 값이 0인 1차원 리스트 초기화
n = 10
a = [0] * n
print(a)

# +
# 리스트의 인덱싱
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a[-1])
print(a[3])
a[3] = 7
print(a)
# -

# 리스트의 슬라이싱
print(a[3:6])

# 리스트 컴프리헨션 : 대괄호[] 안에 조건문과 반복문을 넣어 리스트 간략 초기화
array = [i for i in range(20) if i % 2 == 1]
print(array)

# +
# 리스트 컴프리헨션을 사용하지 않을 경우
array2 = []
for i in range(20):
    if i % 2 == 1:
        array2.append(i)

print(array2)
# -

array3 = [i * i for i in range(1, 10)]
print(array3)

# 2차원 리스트 초기화
n = 3
m = 4
array = [[0] * m for _ in range (n)] # 언더바는 반복을 수행하되 반복을 위한 변수의 값을 무시함
print(array)

# ## 리스트 관련 기타 메서드

a = [1, 4, 3]
print('기본 리스트: ',a)

a.append(2)
print('삽입: ', a)

a.sort()
print('오름차순 정렬: ', a)

a.sort(reverse= True)
print('내림차순 정렬', a)

a.reverse()
print('원소 뒤집기: ', a)

a.insert(2, 3)
print('인덱스 2에 3 추가: ', a)

print('값이 3인 데이터 개수: ', a.count(3))

a.insert(2, 3)
print('인덱스 2에 3 추가: ', a)

a.remove(1)
print('값이 1인 데이터 삭제: ', a)

# +
# 특정한 값의 원소를 모두 제거하려면?
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

# remove_set에 포함되지 않은 값만을 저장
result = [i for i in a if i not in remove_set]
print(result)
# -

# ## 문자열 자료형

data = 'Hello World'
print(data)

# 특수문자를 사용하고 싶다면? 역슬래쉬 + 특수문자 사용!
data = 'Don\'t you know \"Python\"?' 
print(data)

# +
a = 'Hello'
b = 'World'

print(a + ' ' + b)
# -

a = 'String'
print(a * 3)

a = 'ABCDEF'
print(a[2 : 4])

# ## 튜플 자료형
# - 튜플은 한번 선언된 값 변경 불가
# - 리스트는 [] 대괄호를 이용하지만 튜플은 () 소괄호 이용

# +
a = (1, 2, 3, 4)
print(a)

a[2] = 7 # 변경이 안되니 에러 뜨는 것이 정상
# -

# ## 사전 자료형
# - key : value 쌍 데이터

# +
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

print(data)
# -

# ### 리스트, 문자열, 튜플 등 순차적 정보를 담는 자료형은 iterable 자료형이라하며 in 문법 사용 가능

# 특정한 문법이 있는지 검사 if ~ in
if '사과' in data:
    print("'사과'를 키로 가지는 데이터가 존재")

# ## 사전 자료형 관련 함수

# 키 데이터만 담은 리스트
key_list = data.keys()
print(key_list)

# 값 데이터만 담은 리스트
key_value = data.values()
print(key_value)

# 각 키에 따른 값을 하나씩 출력
for key in key_list:
    print(data[key])

# ## 집합 자료형
# - 집합은 중복 허용 불가
# - 순서 없음 (사전 자료형, 집합 자료형 공통) > 인덱싱으로 값을 얻을 수 없음

data = set([1, 1, 2, 3, 4, 4, 5])
print(data)

data = {1, 1, 2, 3, 4, 4, 5}
print(data)

# +
a = set([1, 2, 3, 4, 5])
b = set([3, 4, 5, 6, 7])

print(a | b)
print(a & b)
print(a - b)
# -

data = set([1, 2, 3])
print(data)

# 새로운 원소 하나 추가: add
data.add(4)
print(data)

# 새로운 원소 여러 개 추가
data.update([5, 6])
print(data)

data.remove(3)
print(data)


