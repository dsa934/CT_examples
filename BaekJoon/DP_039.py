
'''

 Backjoon _ exampels 14495

  "피보나치 비슷한 수열"   by Jinwoo Lee

  < algorithm >

  1. dp[idx] = dp[idx-1] + dp[idx-3]

  2. init value 

     dp =  [0] + [ 1,1,1 ] or

     dp = [ 1 for _ in range(num+1) ]
 

'''

def solution():

    num = int(input())

    dp = [1 for _ in range(num+1) ]

    if num >3 :

        for idx in range(4, num+1):

            dp[idx] = dp[idx-1] + dp[idx-3]

    return dp[num]

print(solution())

