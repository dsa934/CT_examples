'''

 Backjoon _ exampels #

  "Baek 17413 - 단어 뒤집기 2 "(문자열)   by Jinwoo Lee


 # Attention for Implementation

  1. 문자열의 마지막이 알파벳 or 숫자로 끝나는 경우에 대한 예외처리가 추가적으로 필요했던 문제 


'''

string = list(input())

stack = []

chk_idx = 0

tag_flag = False

for idx, value in enumerate(string):
  
    # tag
    if value =='<' : tag_flag = True

    elif value =='>' : tag_flag = False


    #alphabet
    if not tag_flag and value.isalpha() or value.isdigit():

        if not stack : chk_idx = idx 

        stack.append(value)

    
    if idx != len(string)-1 and not value.isalpha() and not value.isdigit() : 

        if stack : 
            string[chk_idx:chk_idx+len(stack)] = stack[::-1]
            stack = []

    elif idx == len(string)-1 :

        string[chk_idx:chk_idx+len(stack)] = stack[::-1]
              

print(''.join(string))





