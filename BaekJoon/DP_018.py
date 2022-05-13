
'''

 Backjoon _ exampels 9095

  "1,2,3 더하기 "   by Jinwoo Lee

  < algorithm >
 
  1.

   [1] = [ 1 ] = 1 

   [2] = [ (1,1), (2) ] = 2

   [3] = [ (1,1,1), (1,2), (2,1), (3) ] = 4

   [4] = 7 (sample)


   2. 점화식을 찾을 때, 떄론 피보나치일 수도 있다는 점을 기억

'''


def solution():

    num = int(input())

    candidate = [0]

    for _ in range(num):

        candidate.append( int(input()) )

    max_value = max(candidate)
    
    dp = [0, 1, 2, 4]

    if max_value > 3:

        for idx in range(4, max_value+1):

            value = dp[idx-1] + dp[idx-2] + dp[idx-3] 

            dp.append(value)

    for value in candidate:

        if value == 0 : continue

        print(dp[value])

solution()