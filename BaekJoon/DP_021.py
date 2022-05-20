
'''

 Backjoon _ exampels 9655

  "돌 게임"   by Jinwoo Lee

  < algorithm >

  1. 이전 idx 가 true /false 이면 각각 반대로 진행 


 

'''



def solution():

    num = int(input())

    dp = [ [ False for _ in range(num+1) ] for _ in range(2) ]

    dp[0][1] = True



    if num >=2 :

        for idx in range(2,num+1):


            if not dp[0][idx-1] : dp[0][idx] = True
            
            if not dp[1][idx-1] : dp[1][idx] = True

            
    if dp[0][num] : return 'SK'

    elif dp[1][num] : return 'CY'


print( solution() )