'''

 Backjoon _ exampels #

  "Baek 2012 - 등수 매기기" (Greedy)  by Jinwoo Lee


 # Algorithm 

  0. 불만도의 합이 최소가 되도록 하는 프로그램

  1. 예상 등수와 동일한 입력이 있는지 check

  2. 1번 조건에 만족하지 못한수들을 오름차순 정렬하여 불만도를 계산하면 불만도의 합이 최소가 된다


 # Attention for Implementation

  1. 첫 시도는 시간초과 -> 입력을 sys를 통하니 정답판정 



'''

import sys

num_user = int(sys.stdin.readline())

order = sorted([int(sys.stdin.readline()) for _ in range(num_user)])

result = []
total =0 

for idx, value in enumerate(order):

    if idx+1 != value: result.append([idx+1, value])

for value in result:

    total += abs(value[0] - value[1])

print(total)


