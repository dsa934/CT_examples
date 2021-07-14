'''

 Backjoon _ exampels #

  "Baek 9184 - 신나는 함수 실행"(DP)   by Jinwoo Lee


 # Algorithm 

  0. 재귀 함수에 대하여 그대로 구현하지 않고, Memoization을 사용하는 방식을 통해 설계 

  1. a,b,c입력에 관계없이 20초과시, 20으로 치환되기 떄문에 최대값은 21로 설정하여 dp array 셋팅 

  2. 문제에서 주어진 점화식에 따라 dp[a][b][c]의 값을 채워넣는다.



 # Attention for Implementation

  1. DP문제의 경우 재귀함수를 memoization으로 재구성하는 형태의 문제가 많이 나온다.

    -> 재귀함수 구현시 사용되는 params가 n개여도 n차원 배열을 선언하여 memoization이 가능하다.


'''


def w(a,b,c):

    if a<=0 or b<=0 or c<=0 : return 1

    elif a>20 or b > 20 or c>20 : return w(20,20,20)


    if dp[a][b][c] != 0 : return dp[a][b][c]

    else:

        if a<b and b<c : 

            dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

        else:

            dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

        return dp[a][b][c]




dp_max = 21

dp = [[[0 for _ in range(dp_max)] for _ in range(dp_max)] for _ in range(dp_max)]



while True:

    a,b,c = list(map(int,input().split()))

    if a == -1 and b == -1 and c == -1 : break

    else:

        answer = w(a,b,c)

        print("w({}, {}, {}) = {}".format(a,b,c,answer))
