'''

 Backjoon _ exampels #

  "Baek 9012 - 괄호 "   by Jinwoo Lee


 # Algorithm 

  0. 입력된 문자열이 바르게 구성된 VPS(valid parenthesis string)일 경우 Yes, else No

  1. 문자열에 대해 find("()") 찾아서 replace 


 # Attention for Implementation


'''

nums = int(input())

answer = []

str_list = [input() for _ in range(nums)]


for value in str_list:

    while True:

        idx = value.find("()")

        if idx == -1 :
            answer.append("NO")
            break

        value = value.replace(value[idx:idx+2], "",1)


        if len(value) == 0: 
            answer.append("YES")
            break

for value in answer:
    print(value)