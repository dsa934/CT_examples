

'''

 Backjoon _ exampels 2491

  "수열"   by Jinwoo Lee

  < algorithm >

  1. LIS로 풀려고 했으나, 연속된 수의 경우 LIS를 할 필요가 없음

    => 2중 포문을 이용해서 idx 기준, 0~idx에 대해 비교할 필요가 없다는 것


  2. 연속된 수 임으로 , idx 기준 idx-1과의 크기 비교만  해서 dp[idx]에 저장하면됨

     => dp[idx] = max( dp[idx], dp[idx-1] +1 )


  3. 감소하는 수열의 길이도 포함임으로 부호를 뒤집어서 실행 
 

'''


def solution():
    

    length = int(input())

    numbers = [0] + list(map(int, input().split()))

    dp = [1 for _ in range(length+1)]

    dp_rev = [ 1 for _ in range(length+1) ]

    
    for idx in range(2,length+1):
        
        if numbers[idx] >= numbers[idx-1]:

            dp[idx] = max(dp[idx], dp[idx-1] + 1 )

        if numbers[idx] <= numbers[idx-1]:
                
            dp_rev[idx] = max(dp_rev[idx], dp_rev[idx-1] + 1 )
                  
    
    return max( max(dp_rev) , max(dp) )


print( solution() )


