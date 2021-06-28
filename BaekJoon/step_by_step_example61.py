'''

 Backjoon _ exampels #

  "Baek 11656 - 접미사 배열(문자열)"   by Jinwoo Lee


 # Algorithm 

  0.  문자열 s의 모든 접미사 사전순 정렬 

  1. 문자열을 단위별로 잘라서 list넣고 sort 


'''

string = input()

result = []

for idx in range(len(string)):

    result.append(string[idx:])

for value in sorted(result):

    print(value)