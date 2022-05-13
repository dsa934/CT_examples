
'''

 Backjoon _ exampels 11726

  ""   by Jinwoo Lee

  < algorithm >
 

'''

def solution():

    num = int(input())

    dp = [0,1,2]

    if num > 2: 

        for idx in range(3, num+1):

            value = dp[idx-1] +dp[idx-2]

            dp.append(value)

    print(dp[num]%10007)



solution()