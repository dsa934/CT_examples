
'''

 Backjoon _ exampels 2670

  "연속부분최대곱"   by Jinwoo Lee

  < algorithm >
 
  1. 연속 + dp 문제면 보통 idx, idx-1을 비교하면 해결이 된다


   => 현재 idx 기준, 아래와 같이 식이 전개 

      dp[idx] = max( dp[idx], dp[idx-1] * dp[idx] )   # 현재값, 혹은 이전값에 현재값을 곱한 값 중에 큰것

      dp[idx-1]은 이미, 이전 시점에서 연속인 수를 곱한 결과 max( dp[idx-1] , dp[idx-2] * dp[idx-1]) 의 연산이 끝났기 떄문에

      시점 idx-1 에 대해서는 연속이 보장 되어있다고 할 수 있다 ( 연속이 아니라면 idx-1번쨰 값에 변화가 없기 떄문 )

      즉, idx 기준에서 idx-1 시점과 비교만 해도 되는 것 



  2. 1의 연속을 뒷받침 하기 위해, 초기화를 제대로 해야 한다

   => 자리수/ 길이 문제 : dp = [ 1 for _ in range( 문제에서 주어지는 범위 )]

   => 합과 같은 값 문제 : dp = [ value for value in range(문제에서 주어지는 범위 )]
  

   * python 소수점 이하 자리수 제한 방법 3가지 

   1. round(1.3267, 3 ) = 1.326

   2. answer= 5.3247 f'{answer : .3f}   = 5.324

   3. "{:.3f}" . format(5.324522)  = 5.324



'''


def solution():

    num = int(input())

    numbers = [] 

    for _ in range(num):

        numbers.append(float(input()))
        
    dp = [0] + [value for value in numbers ]
    

    for idx in range(2, num+1):

        dp[idx] = max( dp[idx], dp[idx-1] * dp[idx])
            

    return f'{max(dp):.3f}'

print( solution() )