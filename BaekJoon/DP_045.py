
'''

 Backjoon _ exampels 2193

  "이친수"   by Jinwoo Lee

  < algorithm >

  1. 01 타일 문제와 다를게 없음 ( 피보나치 수열)
 

'''

def solution():

    num = int(input())

    dp = [0,1]

    if num > 1 : 

        for idx in range(2, num+1):

            value = dp[idx-1] +dp[idx-2]

            dp.append(value)

    return dp[num]


print(solution())