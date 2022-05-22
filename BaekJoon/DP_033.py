
'''

 Backjoon _ exampels 19947

  "������ ���� ������"   by Jinwoo Lee

  < algorithm >

  1. n ������ �ݾ��� n-1, n-3, n-5�� ���Ͽ� ���ϰ� ���� ū ���� ���


   1�� ���� : dp[idx-1] * 1.05

   3�� ���� : dp[idx-3] * 1.2

   5�� ���� : dp[idx-5] * 1.35


  2.  dp array idx == 0 �� ������ �־���� ������ ���� 

 

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