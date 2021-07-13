'''

 Backjoon _ exampels #

  ""(BF)   by Jinwoo Lee


 # Algorithm 

  0. 가장 긴 순열(이어져 있음) 찾기 + swap 후 reswap이 핵심 

   0-1. 단순히 C,Z,Y,P의 개수 중 가장 큰것을 찾는것이 아니라 이어져 있는 순열 중 가장 긴 것을 찾는다

   0-2. 문맥상 한번만 바꿨을떄 최대 사탕개수를 구하는것임으로 Swap이후에 본래 상태로 되돌려야 문제상황에 적합하다

        -> copy module의 deepcopy는 시간복잡도 측면에서 비효율적

   0-3. attention-3에 의거하여 CC와 같이 인접한 색이 동일할 경우도 확인해주어야 하기떄문에 결과적으로 모든 케이스를 고려해야한다.
     
        -> if field[i][j] != field[i][j+1] 과 같이 따지지 않음  => just swap => check


  1. 한줄이 모두 같을 수도 있기 떄문에 해당 부분에 대한 예외처리 필요

    -> if j== num-2 and result < row_cnt : result = row_cnt


 # Attention for Implementation

  1. 2차원 배열에서 numpy 없이 transpose 하려면 list(zip(*배열))  
  
     -> 이 방법을 통해 구현할 경우 시간초과가 발생함 

     -> 배열에서 col 기준 접근을 위해 transpose 없이 field[row][col] ->  field[col][row]로 사용하면 조금 더 간략하게 구현 가능



  2. 1번만 swap하고 최대로 먹을 수 있는 사탕의 개수를 구하는 것이기 떄문에 

     Swap -> 개수체크 -> re-swap 과정을 거쳐야함 ( deepcopy로 일일히 필드 복사시 시간복잡도 측면에서 비효율)



  3. Swap이 일어나지 않는 경우도 고려해야함 
     
     cc
     yy  일경우 최대 2 



'''


def long_permutation(array, result):

    # 행기준
    for i in range(num):

        row_cnt = 1

        for j in range(num-1):

            if array[i][j] == array[i][j+1] : 
                
                row_cnt+=1

                if j == num-2 and result < row_cnt :  result = row_cnt


            else:

                if result < row_cnt : result = row_cnt

                # 다를 경우 무조건 cnt 1로 변환 
                row_cnt = 1


    # 열기준
    for i in range(num):

        col_cnt = 1

        for j in range(num-1):

            if array[j][i] == array[j+1][i] : 
                
                col_cnt+=1

                if j == num-2 and result < col_cnt :  result = col_cnt


            else:
                if result < col_cnt : 

                    result = col_cnt

                col_cnt =1


    return result


import sys
num = int(sys.stdin.readline())
field = [list(sys.stdin.readline().rstrip()) for _ in range(num)]
result = 0

# 행고정 열 swap
for i in range(num):

    for j in range(num-1):

        # swap
        field[i][j], field[i][j+1] = field[i][j+1], field[i][j]

        # 최대순열 찾기
        result = long_permutation(field,result)

        # re-swap
        field[i][j], field[i][j+1] = field[i][j+1], field[i][j]

# 열고정 행 swap
for i in range(num):

    for j in range(num-1):

        # swap
        field[j][i], field[j+1][i] = field[j+1][i], field[j][i]

        # 최대순열 찾기
        result = long_permutation(field,result)


        # re-swap
        field[j][i], field[j+1][i] = field[j+1][i], field[j][i]

print(result)