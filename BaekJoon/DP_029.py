

def solution():
    
    num = int(input())


    dp = [0, 1]

    if num >= 2 :

        for idx in range(2,num+1):

            value = dp[idx-2] + dp[idx-1]

            dp.append(value)

    return dp[num]

print( solution() )