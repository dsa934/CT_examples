'''

 Backjoon _ exampels #

  "Baek 10974 - 모든순열 (BF)"   by Jinwoo Lee


 # Algorithm 

  0. 순열함수를 이용하면 해결



 # Attention for Implementation

  - itertools library 를 사용하면 return value가 tuple의 형태로 제공 되는데 

    Online Judge 에서 (1,2,4) 가 아닌 1,2,4 형태의 출력을 요구함으로 

    ( )를 제거하기 위해 2중포문 + print( ... , end = ' ') 형태로 출력 

    => list의 마지막 원소 뒤에 띄어쓰기가 되있는지 안되있는지를 출력을 보고 판단할 수 없지만 이 문제에서는 정답판정 



'''

from itertools import permutations

num = int(input())
num_list = [value for value in range(1,num+1)]
result = sorted(list(permutations(num_list,num)))


for value in result:

    for number in value:

        print(number, end=' ')

    print()