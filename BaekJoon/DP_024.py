
'''

 Backjoon _ exampels 14916

  "거스름 돈 "   by Jinwoo Lee

  < algorithm >

  1. 거스름돈의 개수가 중점, user는 1명

    => 금액에 따른 거스름돈의 수로 dp array 형성 ( 설탕 공장과 동일한 문제 )

    =>     0     1     2     3     4     5     6     7     8
          max   max    1    max    2     1     


          idx > 5 , dp[idx] = min ( dp[idx-2], dp[idx-5] ) + 1 


  2. idx-5를 사용하기 떄문에, init value를 1~ 5까지는 만들어줘야 함 

     => dp [ max_value for _ in range( num + 5 )]   // num+5 인 이유 

     => 초기 요소값들을 크게 잡아놓으면 min 연산 비교가 용의 함 


'''



def solution():
    
    num = int(input())

    max_value = 100000 +1

    dp = [max_value for _ in range(num+5) ]

    dp[2] = 1
    dp[4] = 2
    dp[5] = 1

    for idx in range(6, num+1):
        
        dp[idx] = min( dp[idx-2], dp[idx-5]) + 1

    return  dp[num] if dp[num]!= max_value else -1


print( solution() )