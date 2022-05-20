
'''

 Backjoon _ exampels 13301

  "타일 장식물"   by Jinwoo Lee

  < algorithm >

  1. 각 타일의 순열  1, 1, 2, 3, 5, 8 

     => dp[idx] = dp[idx-2] + dp[idx-1] 


  2. 직사각형 넓이 

    =>  dp[num] + dp[num]  + dp[num+1] + dp[num+1]
 

  3. num일 때, num+1 도 필요하기 떄문에 

    if num >= 6 then  for idx in range( 7 ,  num +2  )   // num+2 까지 설정해야 num, num+1 까지 만들어짐

'''

def solution():
    
    num = int(input())

    dp = [0,1,1,2,3,5,8]

    if num >= 6:

        for idx in range(7, num+2):

            value = dp[idx-1] + dp[idx-2]

            dp.append(value)

    return (2* dp[num] + 2* dp[num+1])





print( solution() )