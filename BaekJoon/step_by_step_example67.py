'''

 Backjoon _ exampels #

  "Baek 10798 - 세로읽기(문자열)"   by Jinwoo Lee


 # Algorithm 

  0. 주어진 5개의 문자열을 세로로 읽었을떄의 결과를 이어붙여 출력하기 

  1. 빈칸이 있을 경우를 고려해야한다. 

  2. 각 문장의 길이를 비교하여 max_len 보다 짧은곳에 빈칸을 추가하였음

  3. 2의 방법을 통해 배열의 원소가 " " 인 경우 pass 하는 형태로 처리 


 # Attention for Implementation

'''

string = [input() for _ in range(5)]

max = 0 

for value in string:

    if len(value) > max : max = len(value)

result =[] 


for idx in range(5):

    if len(string[idx]) < max :

        string[idx] = string[idx] +" " *(max - len(string[idx]))


for col_idx in range(max):

    for row_idx in range(5):

        if string[row_idx][col_idx] == " " : continue
        else : result.append(string[row_idx][col_idx])


print(''.join(result))
