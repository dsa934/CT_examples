'''

 Backjoon _ exampels 16395

  "ÆÄ½ºÄ®ÀÇ »ï°¢Çü"   by Jinwoo Lee

  < algorithm >

   1. 

     if j == 1 , dp_table[i][j] = dp_table[i-1][j]

     else , dp_table[i][j] = dp_table[i-1][j] + dp_table[i-1][j]


   * init value

    => dp_table[1][1] = 1 
 

'''




def solution():
    
    n, k = list(map(int, input().split()))

    dp_table = [ [0 for _ in range(n+1)] for _ in range(n+1) ]

    dp_table[1][1] = 1

    for i in range(2, n+1):

        for j in range(1, i+1):

            if j == 1 :

                dp_table[i][j] = dp_table[i-1][j]

            else:

                dp_table[i][j] = dp_table[i-1][j] + dp_table[i-1][j-1]


    return dp_table[n][k]


print( solution() )


