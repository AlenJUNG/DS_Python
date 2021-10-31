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

# # 함수

# +
# def 함수명(매개변수):
#     실행할 소스코드
#     return 반환값

def plus(a, b):
    return a + b

plus(2, 4)


# +
def plus(a, b):
    print('result = ', a + b)
    
plus(2, 4)
# -

# ## global 키워드
# - 함수 안에서 함수 밖의 변수 데이터를 변경해야 하는 경우 사용 ex) 자바의 static 전역변수와 비슷

# +
a = 0

def func():
    global a
    a += 1
    
for i in range(10):
    func()
    
print(a)


# -

# ## lambda 표현식
# - 람다 표현식을 이용하면 함수를 매우 간단하게 작성하여 적용 가능
# - 특정한 기능을 수행하는 함수를 한 줄에 작성할 수 있음

# +
def add(a, b):
    return a + b

# 일반적인 add() 메서드 사용
print(add(3, 7))

# lambda 표현식으로 구성한 add() 메서드
print((lambda a, b: a + b)(3, 7))
# -

# # 입출력

# ## input() : 한 줄의 문자열 입력
# - 정수형 데이터로 바꿔 받으려면 int(input()) 사용
#
# ## list(map(int, input().split())) 이용
# 1. input() 으로 입력받은 문자열을 split()을 이용해 공백으로 나눈 리스트로 변경
# 1. map을 이용하여 해당 리스트의 모든 원소에 int() 함수 적용
# 1. 최종 결과를 list()로 다시 바꿈으로써 입력받은 문자열을 띄어쓰기로 구분, 각각 숫자 자료형으로 저장

# +
# 데이터의 개수 입력
n = int(input())

# 각 데이터를 공백으로 구분하여 입력
data = list(map(int, input().split()))

data.sort(reverse = True)
print(data)
# -

# ## 공백으로 구분된 데이터 수가 많지 않다면
# > 단순 map(int, input().split()) 이용

# +
# n, m, k를 공백으로 구분하여 입력
n, m, k = map(int, input().split())

print(n, m, k)
# -

# ## 더욱 빠른 데이터 입력 방법
# > sys.stdin.readline() 함수 사용 : sys.stdin.readline().rstip()
# - sys 라이브러리 사용시 한 줄 입력 받고 반드시 rstrip() 함수를 호출하여야 함
#   - readline()으로 입력하면 입력 후 엔터가 줄 바꿈 기호로 입력되는데 이 공백 문자를 제거하기 위해서 rstrip() 함수 사용

# +
import sys

data = sys.stdin.readline().rsplit()
print(data)
# -

# ### 문자열과 수를 함께 출력하는 방법
# > 단순 +를 사용 시, 오류 발생
# 1. str()함수로 변수를 문자열로 변경하고 + 사용
# 1. 각 자료형을 , 기준으로 구분하여 출력

answer = 7
print('정답은' + answer + '입니다.')

answer = 7
print('정답은' + str(answer) + '입니다.')

answer = 7
print('정답은', answer, '입니다.')

# ### 각 변수를 콤마로 구분하여 출력 시, 변수의 값 사이에 의도치 않은 공백이 발생됨에 유의


