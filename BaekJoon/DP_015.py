

'''

 Backjoon _ exampels 9625

  "BABBA"   by Jinwoo Lee

  < algorithm >

  1. A,B에 대한 DP_table을 구성해보면,  n-2, n-1 의 합이라는 사실을 알 수 있음

  * print() 문에서 list의 []와 , 을 없애면서 출력하는 방법이 print ( *list_name ) 인데

    이게 print()에서만 작동한다는걸 알아야 함
 

'''


def solution():


    num = int(input())

    dp_table = [ [1,0] , [0,1]]


    if num > 1 :

        for idx in range(2, num+1):

            
            dp_table[0].append( dp_table[0][idx-2] + dp_table[0][idx-1] )
            dp_table[1].append( dp_table[1][idx-2] + dp_table[1][idx-1] )



    answer = [ dp_table[0][num] , dp_table[1][num] ]

    return answer


print( *solution() )