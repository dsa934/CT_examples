
'''

 Backjoon _ exampels 15624

  "피보나치 수 7"   by Jinwoo Lee

  < algorithm >

  1. dp 문제는 어지간하면 bottom_up & memoization으로 구현 

 

'''


def solution():

    num = int(input())

    dp = [0, 1]


    if num > 1: 

        for idx in range(2, num+1):

            value = (dp[idx-1] + dp[idx-2])% 1000000007

            dp.append(value)

    return dp[num]

print(solution())