
'''

 Backjoon _ exampels 10826

  "피보나치의 수 4"   by Jinwoo Lee

  < algorithm >

  1. 기본 피보나치 문제, bottom up 방식 구현 
 

'''


def solution():

    num = int(input())

    dp = [0 for _ in range(num+1)]

    if num >=1 :

        dp[1] = 1

        for idx in range(2, num+1):

            dp[idx] = dp[idx-1] + dp[idx-2]


    return dp[num]

print( solution() )