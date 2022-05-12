
'''

 Backjoon _ exampels 11055

  "가장 큰 증가 부분 수열 "   by Jinwoo Lee


  < algorithm >

  0. dp_table의 초기값을 <무엇> 으로 잡냐 및 점화식에  따라 다양한 응용 가능


     a) dp_table의 초기값을 모두 1로 잡을 경우, LIS의 길이 문제 해결
     
     b) dp_table의 초기값을 입력받은 원소로 할 경우, LIS의 구성 요소문제 해결


     점화식 : dp[idx] = max ( dp[idx] , dp[cmp_idx] + @  )

 
             @ =>   a)  + 1  : 길이 문제

                    b)  + value : 구성 요소의 합 문제 
   

    * 현 위치(idx) 기준보다 작은 값들을 이중 포문을 통해 비교함으로써 dp[idx]가 계속 update 되는 것





 
  1. 이중 포문을 통해 현재 위치(idx) 와 그 이전 수 (cmp_idx)를 비교하며 dp[idx] 값을 갱신 
 
      idx  :      0  1  2 3  4  5 6... 

      info  :     1 100 2 50 60 3 5 6 7 8 

      dp    :     1 100 2 50 60 3 5 6 7 8 

                  1 101 3 53 ( 1 + 2 + 50 )

                            113 ( 1 + 2 + 50 + 60 )


            info[idx] = 2, 50일떄를 각각 보면, 

            for idx(2) in range(num):

                for cmp_idx(1) in range(idx):

                if info[idx] > info[cmp_idx] :

                 cmp_idx == 1 , 즉 info[cmp_idx] =1 일 때,    dp[idx] (2) 과 dp[cmp_dx]+ info[idx] (1 + 2) 비교 

                 => dp[2] = 3


            for idx(3) in range(num):

                for cmp_idx(1, 100, 2) in range(idx):

                 if info[idx] > info[cmp_idx] :

                 cmp_idx == 1 , 즉 info[cmp_idx] =1 일 때,    dp[idx] (50) 과 dp[cmp_dx]+ info[idx] (1 + 50) 비교 

                 cmp_idx == 2 , 즉 info[cmp_idx] =100 일 때,    조건 불만족 continue

                 cmp_idx == 3 , 즉 info[cmp_idx] =2 일 때,  dp[idx] (1+ 50) 과 dp[cmp_dx]+ info[idx] ( 1+ 2 + 50) 비교 



'''

def solution():

    num = int(input())

    info = list(map(int , input().split()))


    dp = [value for value in info]
    
    for idx in range(num):

        for cmp_idx in range(idx):

            if info[idx] > info[cmp_idx]:

                dp[idx] = max( dp[idx], dp[cmp_idx] + info[idx])

    return max(dp)

    

print( solution() )