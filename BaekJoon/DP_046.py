

'''

 Backjoon _ exampels 24416

  "알고리즘 수업- 피보나치 수 1 "   by Jinwoo Lee

  < algorithm >

  *  5 <= n < = 40 일떈 아래의 코드가 성립 하지만,

   n 의 범위가 더 커지면 아래의 코드는 TLE에 빠지게 됨  ( ref, 알고리즘 수업 - 피보나치 수 2 )

   => 이를 해결하기 위한 방법이 필요 요망 (2022.5.30)


 

'''




num =int(input())

dp = [1,2]

if num > 1:

    for idx in range(2, num+1):
            
        value = (dp[idx-1] + dp[idx-2]) % 1000000007

        dp.append(value)

print( dp[num-2], num-2 )

