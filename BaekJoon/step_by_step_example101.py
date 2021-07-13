'''

 Backjoon _ exampels #

  "Baek 2504 - 괄호의 값"(구현)   by Jinwoo Lee


 # Algorithm 

  0. 이 문제는 특별한 설계없이 차례대로 여러케이스를 따지면 된다 


  1. 입력된 문자열이 '[', '('일 경우 stack에 넣기 

  2. 입력된 문자열이 ']' or ')' 일 경우, while문을 사용하여 3가지 케이스를 고려

    2-1. [ 2 3 ] case :  num을 선언하여 괄호 에 여러가지 숫자들이 있을 경우를 대비 (ex. [ 2 3 ] -> 10 (문제의 조건에 의해) )

    2-2. num의 값이 0이면 [], ()와 같이 괄호만 있는것이기 떄문에 stack에 각각 2,3을 추가 

    2-3. 입력된 문자열이 ')' 인데 stack[-1]=='['일 경우 0을 return 

  3. 2번의 과정을 거쳐 최종 stack에 숫자만 있을 경우 sum(stack), 그 외의 경우 0을 출력 







 # Attention for Implementation

  1. 최초 시도에서 올바른 괄호일 경우를 먼저 따지고 그 후에 계산하려다가 구현 실패 ->  차례대로 구현하기

  2. 구현시 while문 범위를 True로 잡으면 index error -> 계속 돌기 떄문 

     while stack 으로 stack에 요소가 있을떄까지만 돌림  


'''



def VPS_score(string):

    for char_value in string :

        if char_value in ['[','(']: stack.append(char_value)

        elif char_value == ')':

            num = 0

            while stack:

                if stack[-1] == '(' :

                    stack.pop()
                    stack.append(2 if num == 0 else num*2)
                    break

                elif stack[-1] == '[' : return 0

                else: 
                    num+=stack.pop()

        elif char_value == ']':

            num = 0

            while stack:

                if stack[-1] == '[' :

                    stack.pop()
                    stack.append(3 if num == 0 else num*3)
                    break

                elif stack[-1] == '(' : return 0

                else: 
                    num+=stack.pop()


    for value in stack :

        if not str(value).isdigit() : return 0

    return stack



string = input()

stack = []

score = VPS_score(string)

if score == 0 : print(0)

else:print(sum(stack))