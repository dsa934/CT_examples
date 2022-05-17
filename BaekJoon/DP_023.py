
'''

 Backjoon _ exampels 12865

  "평범한 배낭"   by Jinwoo Lee

  < algorithm >

  1. 냅색 알고리즘 이용

    i)  if w_idx < info[idx][0] then  dp[idx][w_idx] = dp[idx-1][w_idx]

        => 입력받은 idx번쨰 물건의 무게(info[idx][0])가 현재의 무게 제한(w_idx) 보다 클 경우 ,

           idx 번쨰 물건을 포함하지 않기 떄문에, w_idx 는 변화가 없으며, 물건의 개수 idx 는 하나 줄어든 것과 같다

           즉, 이전의 [idx-1][w_idx] 의 값과 같아진다.
           


    ii) if w_idx >= info[idx][0] then dp[idx][w_idx] = amx (dp[idx-1][w_idx] , dp[idx-1][w_idx - info[idx][0] ] + info[idx][1] )

        => 현재의 무게 제한(w_idx) 보다 입력받은 idx 번쨰 물건의 무게(info[idx][0]) 이 작거나 같기 떄문에, 2가지 case를 고려 해야한다

           a) i-th 물건 미포함 : 포함하지 않을 경우 i) 와 같은 상황임으로,  dp[idx-1][w_idx]

           b) i-th 물건 포함 : 물건을 포함하기 위해선 현재의 무게 제한에서 i-th 번쨰 물건의 무게를 제외 해야 하고, i-th번쨰 아이템의 가치를 더해줘야 한다.

             -> dp[idx][w_idx] = dp[idx][w_idx - info[idx][0] ] + info[idx][1]  

             
    iii) dp[idx][w_idx] = max(dp[idx-1][w_idx] , dp[idx-1][w_idx - info[idx][0]] + info[idx][1])



  2. dp_table 형성 

    * 냅색 알고리즘 사용시, 보통 조건이 2개인듯 하며, 주어진 조건 N, M에 대하여 

     0 <= N <= max(N),   0<= M <= max(m) 의 범위로 dp_table을 형성하여, bottom_up 방식으로 채워나가며

     마지막 요소 dp_table[N][M]을 return 하면 된다.



  3. 보정

    * dp_table 형성 시, 각 조건(N,M)의 첫번쨰 요소를 채우기 위해, 0번쨰 요소를 zero_padding 해줘야 한다.

     table 형성에는 문제가 없는데, (N,M)에 대한 입력 데이터를 받을때 0번쨰에 대한 정보는 없기 떄문에 

     [0] + info_lst 와 형태로 보정이 필요하다.

 

'''


def solution():


    n_item, n_weight = list(map(int, input().split()))

    info = [0] + [ list(map(int, input().split())) for _ in range(n_item)]

    dp = [[0 for _ in range(n_weight+1)] for _ in range(n_item+1)]


    for idx in range(1,n_item+1):

        for w_idx in range(1, n_weight+1):

            if w_idx < info[idx][0] :

                dp[idx][w_idx] = dp[idx-1][w_idx]

            else:

                dp[idx][w_idx] = max(dp[idx-1][w_idx] , dp[idx-1][w_idx - info[idx][0]] + info[idx][1])

        
    return dp[n_item][n_weight]
    

print( solution() )