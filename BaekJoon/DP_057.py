
'''

 Backjoon _ exampels 17175

  "피보나치는 지겨웡~"   by Jinwoo Lee

  < algorithm >

  *  출력값이 커질 때 int(1e9)+7로 나눈 나머지를 출력하는 이유는 ?

   => 
 

'''





def solution():

    num = int(input())

    dp = [1,1]

    mode = int(1e9) +7

    if num > 1: 

        for idx in range(2, num+1):

            value = (dp[idx-1] + dp[idx-2] + 1)%mode

            dp.append(value)

    print( dp[num] )

solution()
