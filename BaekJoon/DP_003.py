
'''

 Backjoon _ exampels 1904

  "01타일"   by Jinwoo Lee

  < algorithm >


 0. DP 알고리즘 풀기

   * 관계식 구하기 ( F(n) = F(n-1) + F(n-2) .. )

   * 문제에 따라 초기값이 달라짐으로 초기값 설정 

   * memoization을 통한 bottom - up 방식으로 문제 해결하기 



 1. F[0] = 0, F[1] = 1, F[2] = 2 

   F[N] = F[n-1] + F[n-2]



 2. 문제에서 결과값을 15746으로 나눈 나머지를 출력한다 라는 언급이 있었음

    * 문제 정독하기 ( 나누지 않을 경우 메모리 초과 오류 발생 )

    * 메모리 초과 오류 

    => 수가 커지는 경우, 그 수를 정확하게 표현하기 위해 더 많은 메모리를 할당 받게 된다.

       즉, 모든 항의 값을다 구하려 하면 N에 비례하여 자릿수가 늘어남으로 공간 복잡도 O(n^2) 가 된다.

       따라서 값 하나하나를 구하면서 크기를 줄일 필요가 있다 ( ex)  num = (dp[idx-1] + dp[idx-2]) % 15746 ) 

'''


def make_tile():

    n = int(input())

    dp = [1,2]

    if n > len(dp):

        for idx in range(2, n+1):

            num = (dp[idx-1] + dp[idx-2]) % 15746

            dp.append(num)

    return dp[n-1]

print(make_tile())

