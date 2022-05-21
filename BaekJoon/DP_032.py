
'''

 Backjoon _ exampels 9656

  "µπ ∞‘¿” 2"   by Jinwoo Lee

  < algorithm >

 
 

'''


def solution():
    

    num = int(input())


    dp = [ [False for _ in range(num+1)] for _ in range(2) ]

    dp[0][1] = True
    

    for idx in range(2, num+1):

        if not dp[0][idx-1] : 

            dp[0][idx] = True

        if not dp[1][idx-1] :

            dp[1][idx] = True

    

    return 'SK' if not dp[0][num] else 'CY'

print( solution() )