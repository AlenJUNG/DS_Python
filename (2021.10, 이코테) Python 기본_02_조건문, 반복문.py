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

# ### 조건문을 사용할 때는 코드의 블록을 들여쓰기로 설정한다는 점을 기억
# > 들여쓰기는 스페이스바 4번 or tab

# +
x = 15

if x >= 90:
    print('A')
elif x >= 80:
    print('B')
elif x >= 70:
    print('C')
else:
    print('F')
# -

# ## 논리 연산자
# - X and Y : X와 Y가 모두 참일 때 참
# - X or Y : X와 Y 중에 하나만 참이어도 참
# - not X : X가 거짓일 때 참

# ## 파이썬의 기타 연산자
# - 파이썬에서는 추가적으로 in 연산자와 not in 연산자를 제공
#   - X in 리스트 : 리스트 안에 x가 들어가 있으면 참
#   - X not in 문자열 : 문자열 안에 X가 들어가 있지 않을 때 참
# - 자료형으로는 리스트, 튜플, 문자열, 사전과 같은 자료형 존재

# +
score = 85

if score >= 80:
    pass # 나중에 작성할 코드
else:
    print('성적이 80점 미만입니다.')
    
print('프로그램을 종료합니다.')
# -

# ### 조건부 표현식 (Conditional Expression)
# - 리스트에 있는 원소의 값을 변경해서 또 다른 리스트를 만들고자 할 때 매우 간결하게 사용할 수 있음

# +
score = 85

result = 'Success' if score >= 80 else 'Fail'

print(result)

# +
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

result = []
for i in a:
    if i not in remove_set:
        result.append(i)
        
print(result)

# +
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

result = [i for i in a if i not in remove_set]

print(result)
# -

# ## 파이썬은 조건문 안에서 수학의 부등식을 그대로 사용 가능
# - if 0 < x < 20: # 이런 형태로도 사용 가능

# # 반복문
# ## while 
# - 1부터 9까지 각 정수의 합을 계산하는 코드

# +
x = 1
result = 0

while x < 10:
    result += x
    x += 1

print(result)
# -

# - 1부터 9까지 홀수들의 합

# +
x = 1
result = 0

while x < 10:
    if x % 2 == 1:
        result += x
    x += 1

print(result)
# -

# ## for문
# - in 뒤에 오는 데이터에 포함되어 있는 모든 원소를 첫 번째 인덱스부터 차례대로 하나씩 방문
# - in 뒤에 오는 데이터로는 리스트, 튜플, 문자열 등이 사용될 수 있음
#
# for 변수 in 리스트:  
#   실행할 소스코드

# +
result = 0

for x in range(1, 10):
    result += x
    
print(result)

# +
scores = [90, 85, 77, 65, 97]

for i in range(5):
    if scores[i] >= 80:
        print(i + 1, '번 학생은 합격입니다.')

# +
scores = [90, 85, 77, 65, 97]
cheating_list = {2, 4}

for i in range(5):
    if i + 1 in cheating_list:
        continue
    if scores[i] > 80:
        print(i + 1, '번 학생은 합격입니다.')
# -


