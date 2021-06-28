'''

 Backjoon _ exampels #

  " Baek 14888 - 연산자 끼워넣기(BF-)"   by Jinwoo Lee


 # Algorithm 

  0. 주어진 숫자 조합 순서 바꾸지않고, 숫자 사이에 연산자를 끼워넣어 만들어지는 최소/최대값 출력 ( 연산자 우선순위 무시, 앞에서부터 계산)

  1. Permutation을 통해 주어진 연산자로 만들어질 수 있는 모든 경우의 수를 구한다.

  2. 연산자조합을 하나씩 선택해 계산한 값을 result에 넣고 min/max를 찾는다.

  3. 나눗셈의 경우 

     3.1 음수 / 양수일 경우 (조건에 의해 몫만 음수가 될수있음 1 <= A_n <= 100 ) => - ( abs(음수) / 양수 ) 값으로 처리 

     


 # Attention for Implementation

  1. 시간초과 발생 -> permutation 관련 

   => Permutations 사용시, 순열 생성에 사용되는 배열의 요소에서 중복인 요소가 있을 경우 set을 통해 중복을 없애줘야 한다.


'''

from collections import deque
from itertools import permutations
import copy 
import sys

def cal(set_oper, numbers):

    tmp = numbers.popleft()

    while numbers:

        value = numbers.popleft()
        oper = set_oper.popleft()

        if oper == '+' : tmp += value 

        elif oper == '-' : tmp -= value 

        elif oper == '*' : tmp *= value 

        elif oper == '/' :

            if tmp == 0  : tmp = 0

            elif tmp < 0 : tmp = -(abs(tmp) // value)

            else: tmp //= value

    return tmp



num = int(sys.stdin.readline())
numbers = deque(list(map(int,sys.stdin.readline().split())))
# + - * / 순서
chk_oper = list(map(int,sys.stdin.readline().split()))

oper = []
for idx, value in enumerate(chk_oper):
    
    for _ in range(value):

        if idx == 0 : oper.append('+')
        elif idx == 1: oper.append('-')
        elif idx == 2 : oper.append('*')
        else : oper.append('/')


# 연산자 조합
permutation = set(list(permutations(oper)))

result = []

for operations in permutation :

    set_oper = deque(operations)

    answer = cal(set_oper, copy.deepcopy(numbers))

    result.append(answer)

        
print(max(result))
print(min(result))