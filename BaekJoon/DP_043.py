
'''

 Backjoon _ exampels 25214

  "크림 파스타"   by Jinwoo Lee

  < algorithm >
 
  1. 문제 이해 

    < 정의 >  A : 빈배열, a_i : i번째로 추가할 데이터

    => a_i를 A에 추가할 때,  A[0 : i] (자기 자신 제외 임으로 i까지)  범위에 있는 데이터와 비교하여 가장 큰 값 기록

    dp[idx] = max( dp[idx-1], numbers[idx] - min_value)

    dp array를 갱신하는 것 처럼, 배열에서 가장 작은 값도 갱신 ( 추가할떄마다 한번만 비교 하기 때문에 O(1) 복잡도 )


  * 최초 시도에 min(numbers[:idx]) 를 사용했는데 N 개중에 찾아야 함으로 O(N) 

    추가 되는 데이터가 n개임으로 총 시간복잡도가 O(N^2) 이 되어 TLE


    => 추가할때마다 가장 작은 min_value를 갱신하면 해당 작업은 시간복잡도 O(1)

       총 시간 복잡도는 O(N * 1 ) = O(N)  => TLE 해결 



'''



def solution():
    

    num = int(input())

    numbers = list(map(int, input().split()))

    dp = [0 for _ in range(num)]

    min_value = numbers[0]
    
    for idx in range(1,num):

        if min_value > numbers[idx]:

            min_value = numbers[idx]

        dp[idx] = max( dp[idx-1] , numbers[idx] - min_value )


    return dp


print(* solution() )
