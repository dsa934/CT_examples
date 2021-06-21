'''

 Backjoon _ exampels #

  "Baek 14501 - 퇴사 "   by Jinwoo Lee


 # Algorithm 

  0. N일에 예정된 회의를 무조건 해야 최대 금액을 달성하는 것이 아니기 때문에 1일이 아닌 N일 에서부터 시작을 해야 한다.

  1. dp[n]을 n일에 대한 누적 수익이며, 현재 N일이라고 가정하면,

     N일차에 잡힌 회의 진행시 얻게되는 수익 p[n] + N일차에 잡힌 회의 끝나는 날( n + T[n] )의 누적금액 vs N+1일차에 잡힌 회의를 했을떄의 누적금액 


  2. dp[n] = max ( (dp[n + T[n]] + p[n]), dp[n+1]  )


     ex) if N== 6 then , (즉, 7일차)

            6 + 2  > 7 이라 회의 진행이 안됨 -> 7일차는 누적금액이 없음

         if N==4 then, (즉, 5일차)

            p[4] = 15 , dp[n + t[n] ] -> dp[4 +2 ] = 0   => 6일차도 기간초과라 누적금액 0  => 0+15 = 15

         if N==3 then , (즉 4일차)

            p[3] = 20, dp[3+1]= 15 -> 20+15 => 4일차 회의하고 회의가 끝나게되는 5일차의 누적금액은 35

         
  3. dp[idx] = dp[idx+1] 

     idx일에 잡힌 상담이 nums를 초과할 경우 누적금액이 생기지 않기 떄문에 이전 누적금액으로 치환 


 # Attention for Implementation

  1. 완전탐색 / greedy 에서 입력값 N의 범위가 크면 greedy, 작으면 완전탐색 문제일 확률이 높다.

 



'''

num = int(input())

conference = [list(map(int,input().split())) for _ in range(num)]

# N일에 대한 알고리즘 2번을 처리하기 위해 num+1
dp = [0 for _ in range (num+1)]

for idx in range(num-1, -1, -1):

    if idx + conference[idx][0] > num:
        dp[idx] = dp[idx+1]

    else:

        dp[idx] = max( dp[idx+1] , dp[idx + conference[idx][0]]+ conference[idx][1])


print(dp)
print(max(dp))



