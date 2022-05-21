
'''

 Backjoon _ exampels 15489

  "파스칼 삼각형"   by Jinwoo Lee

  < algorithm >

  1. dp 를 통한 파스칼 삼각형 만들기

  2. 특정 범위 내 합 구하기 

   * start = [raw][col] 

    raw : raw ~ raw + w 

    col : col ~ col + w 

    => 지정 범위 내의 column 의 합만 구하면 되기 떄문에 while , for문 사용

       raw에 대한 for문 없이 [raw+w_idx] 로 하면됨 

       while cnt < w+1 :  # w를 포함해야 하기 떄문

        for col_idx in rnage(col, col+cnt):
            
           ans += dp_table[ raw + cnt -1 ] [ col_idx ]
        
 
    * 애시당초 3중 포문으로 구현할 필요가 없음

     => n^3 이 되면 TLE에 걸릴 수 있음 

     => '3중 포문 해야 하나?' 생각 되면 하나의 for문은 indexing으로 없앨 수 있는지 없는지 체크 

'''


def solution():
    

    raw, col, w = list(map(int, input().split()))


    dp_table = [[0 for _ in range(30+1)] for _ in range(30+1) ]

    dp_table[1][1] = 1

    for i in range(2,31):

        for j in range(1, i+1):

            if j == 1 : 

                dp_table[i][j] = dp_table[i-1][j]

            else:
                dp_table[i][j] = dp_table[i-1][j] + dp_table[i-1][j-1]
        
    ans = 0 
    cnt = 1

    while cnt < w+1 :
        
        for col_idx in range(col, col+cnt):

            ans +=  dp_table[raw+ cnt -1 ][col_idx] 

        cnt +=1


    return ans


print( solution() )

