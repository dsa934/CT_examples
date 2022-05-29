
'''

 Backjoon _ exampels 11727

  "2 x N ≈∏¿œ∏µ 2"   by Jinwoo Lee

  < algorithm >

  1. recurrence realtion 

     => dp[idx] = dp[idx-2] *2 + dp[idx-1] 

 

'''

def solution():

    num = int(input())

    dp = [0, 1, 3]

    if num > 2 :

        for idx in range(3, num+1):

            value = (dp[idx-2]*2 + dp[idx-1])%10007

            dp.append(value)

    return dp[num]

print( solution() )