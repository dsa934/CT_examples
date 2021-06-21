'''

 Backjoon _ exampels #

  "Baek 10773 - 제로 "   by Jinwoo Lee


 # Algorithm 

  0. 입력받은 정수가 "0"일 경우 지울 수가 있음을 보장하기 때문에 stack을 사용하여 유효한 수의 합을 구하면 된다


 # Attention for Implementation

  - sys를 사용한 input()을 사용하지 않을 경우 시간초과 발생 

     1 <= nums <= 100,000 이라 선형시간 알고리즘으로 작성하였는데 시간초과 판정 => input() 함수의 복잡도가 상당히 높음


'''
import sys

num = int(sys.stdin.readline())

nums = [int(sys.stdin.readline()) for _ in range(num)]

stack = [] 

while nums :

    temp = nums.pop(0)

    if temp != 0: stack.append(temp)

    else:

        stack.pop()

print(sum(stack))

