'''

 Backjoon _ exampels #

  "Baek 2309 - 일곱 난쟁이"   by Jinwoo Lee


 # Algorithm 

  - itertools library에서 제공하는 조합(combination)을 사용하여 문제해결 

'''
from itertools import combinations

height = [int(input()) for _ in range(9)]


answer = list(combinations(height, 7))

result = []

for value in answer:

    if sum(value) ==100:

        result = value
        break

for value in sorted(result):
    print(value)


