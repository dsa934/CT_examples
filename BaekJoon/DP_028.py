
'''

 Backjoon _ exampels 2839

  "설탕 공장"   by Jinwoo Lee

  < algorithm >

  1. 주어진 무게 N kg 에 대하여 ,   3kg, 5kg 봉지로 가장 최소로 배달 하기 

    => dp 문제가 나오면, 구해야 하는 목적을 축으로 dp array를 구성해보기 

                                               0   1   2  3  4  5 
      dp = [ 0 for _ in range(num+1) ]   =>   [ 0 , 0 ,0 ,0 ,...  ]


    => 3, 5 kg 은 각각 1번으로 이동 시킬 수 있음  =>   0   1   2  3  4  5 
                                                      [ 0 , 0 ,0 ,1 ,0, 1 ,  ...    ]  


  2. 위 dp table을 통해, 6kg 부터는 [idx-3], [idx-5]를 통해 표현이 가능

     dp[idx] = min ( dp[idx-3] , dp[idx-5] ) +1

     => 이 문제에서는 3,5로 만들 수 없는 kg에 대해서는 관심이 없기 떄문에 따로 처리할 이유가 없음 

     6의 경우 

     dp[6] = min(dp[3], dp[5]) + 1

     => 3kg 일 경우 1봉지 이며,  6kg 이면 3kg가 남기 떄문에 또 한봉지를 추가 => 결과적으로 2봉지 

     dp[9] = min (dp[6], dp[4] ) + 1 

     =>  2 봉지 + 1  => 3봉지 





  3. dp array 초기 설정

     dp = [ (5000 +1) for _ in range(num+5) ]

     num = 0~ 4가 나올경우 for문이 out of idx 문제가 발생하기 떄문에 이를 위한 처리 



      
  


  * dp 풀다 열받아서 기본부터 다시 시작하기 
 

'''



def solution():
    
    num = int(input())

    
    dp = [ (5000 +1 ) for _ in range(num+5) ]


    dp[3] = 1
    dp[5] = 1

    for idx in range(6, num+1):

        dp[idx] = min (dp[idx-3] , dp[idx-5]) + 1

        
    return dp[num] if dp[num] < 5001 else -1 


print( solution() )