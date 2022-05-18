
'''

 Backjoon _ exampels 1010

  "다리 놓기 "   by Jinwoo Lee

  < algorithm >

  1. 점화식을 구하기 위해 table을 구현해봄
  
   
   n / m   0  1  2  3  4  5

    0      0  0  0  0  0  0

    1      0  1  2  3  4  5              => dp[n][m] = dp[n-1][1 : m-1]

    2      0  0  1  3  6  10

    3      0  0  0  1  4  10       

   
 

'''



def solution():


    raw, col = list(map(int, input().split()))

    dp_table = [[0 for _ in range(col+1)] for _ in range(raw+1)]

    
    for idx in range(1, col+1):

        dp_table[1][idx] = idx


    if raw >= 2 :

        for raw_idx in range(2, raw+1):

            for col_idx in range(1, col+1):
                
                if col_idx == 1 :

                    dp_table[raw_idx][col_idx] = dp_table[raw_idx-1][0] 

                else:

                    dp_table[raw_idx][col_idx] = sum(dp_table[raw_idx-1][:col_idx])

                
                
    print(dp_table[raw][col])


   


num_test = int(input())



for _ in range(num_test):


    solution()