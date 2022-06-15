
'''

 Backjoon _ exampels 11051

  "���� ��� "   by Jinwoo Lee

  < algorithm >

  1. ���� ��� ������  �Ʒ��� ����

     n    n! / ( k! (n-k) ! )    0 <= k <= n
       =  0                      k < 0
     k    0                      k > n 


    => but, ���� ��� �Ľ�Į�� �ﰢ�� �����ϱ� 

      1
      1 1
      1 2 1
      1 3 3 1
      1 4 6 4 1
      1 5 10 10 5 1 
      ...
      
      => 1)  col = 0 �� ��� 1�� ���� 

         2)  ������  dp[row][col] = dp[row-1][col] + dp[row-1][col-1] 


 

'''



def solution():

    row, col = map(int, input().split())

    dp_table = [[0 for _ in range(row+1)] for _ in range(row+1)]

    dp_table[0][0] = 1

    mode = int(1e4) +7 
    

    for row_idx in range(1,row+1):

        for col_idx in range(col+1):

            if col_idx == 0 :

                dp_table[row_idx][col_idx] = (dp_table[row_idx-1][col_idx]) % mode


            else :

                dp_table[row_idx][col_idx] = (dp_table[row_idx-1][col_idx] + dp_table[row_idx-1][col_idx-1]) % mode



    print( dp_table[row][col])


solution()