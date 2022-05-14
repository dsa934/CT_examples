
'''

 Backjoon _ exampels 1309

  "동물원"   by Jinwoo Lee

  < algorithm >

  1. dp[idx] = dp[idx-2] + dp[idx-1] + dp[idx-1]


  < n condition >   <0마리> <1마리 > ... < n마리 >

    n = 1   then ,   1         2                        = 3

    n = 2   then ,   1         4        2               = 7  

    n = 3   then ,   1         6        8        2      = 17  ( 3 + 7 + 7 )



  * dp 문제에서의 점화식 형성은 보통 n = 3부터 , n =1,2 값을 이용하여 나타내는 문제가 많은듯 하다. ( dp 문제의 카테고리화를 위한 db 쌓는중 2022/5/15)


'''

def solution():

    num = int(input())

    dp = [0,3,7]

    if num > 2 :

        for idx in range(3, num+1):

            value = dp[idx-2] + 2 * dp[idx-1]

            dp.append(value%9901)

    return dp[num]

print( solution() )