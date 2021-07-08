'''

 Backjoon _ exampels #

  "Baek 5397 - 키로거 "(문자열)   by Jinwoo Lee


 # Algorithm 

  0. 시간초과 문제로 insert(0)을 활용할 수 없기 떄문에 stack 의 구조를 사용하는것이 핵심

  1. '<' 입력되는 경우 stack 안에 값을 뺴서 save에 저장 

  2. '>' 입력되는 경우 save 값을 뺴서 stack에 저장 

  3. AB<<C 의 경우, stack, save에 모두 값이 들어있기 떄문에 최종 결과는 stack + reversed(save)의 형태로 출력해야 정답판정 


 # Attention for Implementation

  1. insert(0, value) 사용시 시간초과 

   -> 0번쨰 원소 삽입을 위해 모든 원소를 한칸씩 뒤로 미는 과정이 필요함 


  2. 문제 설명에서 커서가 제일 마지막이 아닌 경우 커서와 커서오른쪾 문자들이 오른쪾으로 이동한다는데 이말이 사실상 없었으면 금방 풀었을듯 



'''
import sys

num_test = int(sys.stdin.readline())

result = []

for _ in range(num_test):

    string = list(sys.stdin.readline().rstrip())
    stack = []
    save = []
    
    for s_value in string:

        if s_value == '<' :

            if stack : save.append(stack.pop())
            
        elif s_value == '>' : 

            if save : stack.append(save.pop())
            
        elif s_value == '-' : 

            if stack : stack.pop()
            
        else: stack.append(s_value)

    print(''.join(stack) + ''.join(reversed(save)))
