
'''

 Backjoon _ exampels 19947

  "투자의 귀재 배주형"   by Jinwoo Lee

  < algorithm >

  1. n 시점의 금액을 n-1, n-3, n-5에 대하여 구하고 가장 큰 값을 기록


   1년 투자 : dp[idx-1] * 1.05

   3년 투자 : dp[idx-3] * 1.2

   5년 투자 : dp[idx-5] * 1.35


  2.  dp array idx == 0 에 원금을 넣어줘야 계산식이 성립 

 

'''

def solution():

    amount, year = list(map(int, input().split()))


    dp = [amount] + [0 for _ in range(year)]

    year_1, year_3, year_5 = 0, 0, 0

    for idx in range(1,year+1):

        if idx >= 3:

            year_3 = int(dp[idx-3]*1.2)

        if idx >= 5 :
            
            year_5 = int(dp[idx-5]*1.35)

        year_1 = int( dp[idx-1] * 1.05)

        dp[idx] = max(year_1, year_3, year_5)

    return dp[year]

print( solution() )