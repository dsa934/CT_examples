'''

 Backjoon _ exampels #

  "Baek 1080 - 행렬 "

 by Jinwoo Lee ( 2021/06/xx )


 # Attention for Implementation

  - 3*3 부분행렬에 대하여 raw_matrx / cmp_matrix의 각각의 row에 대한 col이 같지 않으면 행렬이 같아질 수가 없음 

    => raw/cmp의 각 row별 col을 비교하는 함수 

    => 비교 이후 다르다면 변환하는 함수


  - 문자열 입력에 대해 (주로 행렬문제)

   -> 문자열 입력받을떄 '0000' 와 같은 문자열을 [0,0,0,0]으로 받고싶으면 input().split()을 안하면됨 
   
   => split() : ()안이 비었기 떄문에 공백기준으로 문자열을 나누는데 0000은 공백이없음으로 map(int,input().split())하게되면 0000이 0으로 출력

  
  - 1 <-> 0 변환의 경우

   => matrix[row][col] = 1 - matrix[row][col] 


  - 행렬 비교 

   => if  m_chage == m_compare  : 비교하는 두 행렬의 모든 원소가 같으면 true


'''


row, col = list(map(int, input().split()))

m_change = [list(map(int,input())) for _ in range(row)]
m_compare = [list(map(int,input())) for _ in range(row)]

def change(m_change, row_idx, col_idx):

    for row in range(row_idx, row_idx+3):

        for col in range(col_idx, col_idx+3):

            m_change[row][col] = 1 - m_change[row][col]



answer = 0 

for row_idx in range(row-2):

    for col_idx in range(col-2):

        if m_change[row_idx][col_idx] != m_compare[row_idx][col_idx]:

            change(m_change, row_idx, col_idx)

            answer +=1


if m_change == m_compare:

    print(answer)
else:
    print(-1)

