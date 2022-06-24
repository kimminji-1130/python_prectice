#표준 라이브러리 활용
import math
math.pi
--3.141592653589793238...

#프로그램을 파일에 저장하여 한꺼번에 실행
iadius = 25.365
form math import pi
area = pi * radius ** 2
print(area)
--2021.2480131029088

#표준 입력
radius = float(input())
from math import ** 2
area = pi * radius ** 2
print(area)

#반올림은 round
round(1.49)
--1
round(2.356, 2)
--2.36

#람다 함수
#원의 면적 함수 계산 문제에서 반지름 각각 3, 5, 9인 원의 면적을 모두 계산할 때 반지름 별로 식을 따로 세워서 계산을 수행할 수 있다.
from math import pi
radius = 3
print(pi * radius ** 2)
radius = 5
print(pi * radius ** 2)
radius = 9
print(pi * radius ** 2)
#이러한 문제를 람다 함수를 이용하며 lambda <변수> : <식>으로 바꿈
form math import pi

def area_circle(radius):
  return pi * radius ** 2

print(area_circle(3))
print(area_circle(5))
print(area_circle(9))
--28.27433...
--78.53982...
--254.4600...
