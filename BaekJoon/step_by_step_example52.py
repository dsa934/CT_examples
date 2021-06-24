'''

 Backjoon _ exampels #

  "Baek 10819 - 차이를 최대로 (BF)"   by Jinwoo Lee


 # Algorithm 

  0. |A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]| 의 최대값을 구하라 

  1. 입력범위가 3 <= n <= 8으로 작기때문에 BF 가능 => permutation으로 모든 조합 찾기


  
 # Attention for Implementation

  1. itertools library 사용시 list 는 iterative 한 객체 여야 하며,

     * permuations (list, number)     len(list) <= number (순열 : 순서에 관계가 있기 떄문에 원소 종류가 같아도 순서가 다르면 다른 배열 )

     * combinations (list, number)     len(list) < number (조합 : 순서에 관계가 없기 떄문에 원소 종류가 같으면 같은 배열)


  2. sys로 입력받을떄 .rstrip() 안하면 \n이 포함되서 이를 제거하기 위해 사용 


'''
import sys
from itertools import permutations

num = int(sys.stdin.readline().rstrip())

num_list = list(map(int,sys.stdin.readline().split()))


permutation = permutations(num_list, num)

result = []

for value in permutation:
    total = 0

    for idx in range(len(value)-1):

        total += abs(value[idx] -value[idx+1])

    result.append(total)

print(max(result))