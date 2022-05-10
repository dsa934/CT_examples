
'''

 Backjoon _ exampels 10844

  "쉬운계단수"   by Jinwoo Lee

  < algorithm >

  number :    0 1 2 3 4 5 6 7 8 9

  자리수(1) : 0 1 1 1 1 1 1 1 1 1

  자리수(2) : 1 1 2 2 2 2 2 2 2 1

  자리수(3) : 1 3 3 4 4 4 4 4 3 2


  1. 점화식

   num == 0 : 

   num == 9 :  dp[pos][num] = dp[pos][8]

   others   :  dp[pos][num] = dp[pos-1][num-1] + dp[pos-1][num+1]


  2. init value

     1자리의 계단 수일 경우,  1 ~ 9까지 맨 뒤에 배치되는 경우는 1, 0은 없음(자리수가 1이면 0으로 시작하는 수 이기 떄문 )

     dp_table[1][1~9] = 1 , dp_table[1][0] = 0 


  * dp table은 n차원 배열로 구성할 수 있다.

    dp_table[자리수][계단수 마지막에 위치할 숫자]


  * 문제를 읽고 dp_table의 idx로써 정할 속성이 무엇인지 먼저 파악하고, 그에 대한 점화식 구성하기 


'''



def dp():

    num = int(input())

    mod = 1000000000

    dp_table = [[ 0 for _ in range(10) ] for _ in range(num+1)]

    # init value
    for idx in range(1,10):

        dp_table[1][idx] = 1


    # dp algorithm

    for idx in range(2, num+1):

        for j in range(10):

            if j == 0 :

                dp_table[idx][j] = dp_table[idx-1][1]

            elif j == 9 :

                dp_table[idx][j] = dp_table[idx-1][8]

            else:

                dp_table[idx][j] = dp_table[idx-1][j+1] + dp_table[idx-1][j-1]

    #print(dp_table)


    return sum(dp_table[num]) % mod 

print ( dp() )