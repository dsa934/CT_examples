'''

 Backjoon _ exampels #

  "Baek 4949 - 균형잡힌 세상(문자열)"   by Jinwoo Lee


 # Algorithm 

  0. 옳은 괄호인지 검사하자 

  1. Stack을 이용한다 -> 괄호가 여러개일 경우 안쪽에서부터 짝을 찾아야 하기 때문에 FILO 구조의 STACK 유리

  2. 주어진 문자열이 (, [ 이면 stack에 넣고 ) , ] 일 경우에는 아래와 같이 따져본다

     2-1. stack is empty ? -> 스택이 비었고 ) or ] 부터 나왔으면 no에 해당

     2-2. stack is not empty 

          if current_char == ')'  & stack[-1] == '('  => stack.pop()   // stack[-1] != '(' => no
         

     2-3. [ab 와 같이 즉 모든 문자열을 검사했는데 stack이 비어있지 않는 경우를 고려해야 한다. (여기때문에 계속 오답판정)


  3. 문자열에 괄호가 없는 경우는 문제에 의해 균형잡혔다고 간주 => yes 


 # Attention for Implementation

  - 입력 라인의 수가 정해져 있지 않기 떄문에 한줄 받아서 결과처리하고 다시하는 식으로 진행

  - tmp in list : 구조 사용시 list 대신 직접적인 문자 표현( '()[]' ) 가능 

'''

result = []

while True:

    string = input()
    flag = True

    if string =='.' : break

    stack = []

    for char in string :

        if char in '([' : stack.append(char)

        elif char == ')' :
            if not stack : 
                flag = False
                break
                        
            elif stack and stack[-1] =='(' : stack.pop()

            else : 
                flag = False
                break

        elif char == ']' :

            if not stack : 
                flag = False
                break

            elif stack and stack[-1] =='[' : stack.pop()

            else : 
                flag = False
                break
    
    if not stack and flag : result.append("yes")
    elif stack or flag == False :  result.append("no")


for value in result:
    print(value)
