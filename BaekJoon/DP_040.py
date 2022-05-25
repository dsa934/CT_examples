
'''

 Backjoon _ exampels 14606

  "ÇÇÀÚ (small) "   by Jinwoo Lee

  < algorithm >

  1. if idx >=2 , dp[idx] = dp[idx-1] +idx-1
 

'''


def solution():

    num = int(input())

    dp = [0 for _ in range(num+1)]

    dp[1] = 0

    if num > 1:

        for idx in range(2,num+1):

            dp[idx] = dp[idx-1] + idx-1

    return dp[num]


print( solution() )