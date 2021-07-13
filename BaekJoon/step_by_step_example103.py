'''

 Backjoon _ exampels #

  "Baek 2503 - 숫자야구"(BF)   by Jinwoo Lee


 # Algorithm 

    0. Permutation을 통해 1~9 숫자중 3가지 조합을 모두 구한 후, 이 조합에서 strkie, ball 조건을 이용하여 조건에 맞지 않는 요소를 제거 

 

  
 # Attention for Implementation

    1. permutation 함수를 사용 -> 요소가 tuple형태로 주어지기 떄문에 string의 형태로 변환된 candidates list를 생성 

    2.  print('1' == 1) -> False

    3. 최초 시도에 strkie, ball 조건에 맞는 요소를 뽑아서 따로 저장했는데, 이 경우에 따로 저장된 요소들까지 두번 처리를 해야 하기 떄문에 효율적이지 못함 


'''
import sys
from itertools import permutations


permutations = list(permutations([1,2,3,4,5,6,7,8,9], 3))


candidates = [] 

for value in permutations:

    candidates.append(str(value[0]) + str(value[1]) + str(value[2]))


num_test = int(sys.stdin.readline())

for _ in range(num_test):

    num, st, ball = list(sys.stdin.readline().split())

    num = str(num)

    stack = [] 

    for value in candidates:

        cmp_st, cmp_ball = 0, 0

        for idx in range(len(value)):

            if value[idx] in num :

                if value[idx] == num[idx] : cmp_st +=1
                else: cmp_ball +=1
        

        if cmp_st != int(st) or cmp_ball != int(ball) : 
            
            stack.append(value)



    for s_value in stack:

        if s_value in candidates : candidates.remove(s_value)


print(len(candidates))
