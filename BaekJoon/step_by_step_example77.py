'''

 Backjoon _ exampels #

  "Baek 1051 - 숫자 정사각형(Implementation)"   by Jinwoo Lee


 # Algorithm 

  0. 꼭지점에 해당하는 숫자가 같은 정사각형 중 가장 큰 정사각형의 크기 구하기  

  1. min(row,col) 값이 조사할 범위에 해당하며, tmp = idx+ min(row,col)의 값이 (row,col)범위를 넘어가지 않는지 체크

  2. 1에서 범위를 넘지 않았다면, 현 위치 (i,j)에서 (i+tmp,j), (i+tmp,j+tmp), (i,j+tmp) 값이 같은지 확인하여 같을 경우 chk+1 저장 

  3. 해당하는 chk가 없다면 사각형 최대크기는 1이된다.



'''

def is_check(row_idx,col_idx,chk):

    if row_idx+chk > row -1 or col_idx+chk > col -1 : return False

    else: return True

row, col = list(map(int,input().split()))

array = [list(map(int,input())) for _ in range(row)]

chks = min(row,col)-1

total = []

for row_idx in range(row):

    for col_idx in range(col):

        for chk in range(1,chks+1) :

            if is_check(row_idx, col_idx, chk):

                if array[row_idx][col_idx] == array[row_idx+chk][col_idx] and array[row_idx][col_idx] == array[row_idx][col_idx+chk] and array[row_idx][col_idx] == array[row_idx+chk][col_idx+chk]:

                   total.append(chk+1)


if total : print(max(total)**2)
else : print(1)