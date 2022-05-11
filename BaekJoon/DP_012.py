
'''

 Backjoon _ exampels 11504

  "가장 긴 바이토닉 부분 수열"   by Jinwoo Lee


  < algorithm >

  1. 11503 LIS 문제의 방법을 두번 이용하면 된다.


   * idx를 기준으로 0 ~ idx-1 범위의 수에 대해 dp 알고리즘을 적용한다

     dp[idx] = max ( dp[idx], dp[cmp_idx]+1 ) 





  * 문제에서는 바이토닉 수열 가능 여부까지 판단하라고 했는데, 해당 부분에 대한 처리가 없어도 pass 판정을 받을 수 있음

    => LIS 계열 문제를 더 풀어보면서 추후 총 정리하기 

 

'''


def solution():

    num = int(input())

    field = list(map(int, input().split()))

    dp_increase = [1 for _ in range(num)]
    dp_decrease = [1 for _ in range(num)]


    rev_field = field[::-1]
    
    for idx in range(num):

        for cmp_idx in range(0,idx):

            if field[cmp_idx] < field[idx] :

                dp_increase[idx] = max(dp_increase[idx] , dp_increase[cmp_idx]+1 ) 


            if rev_field[cmp_idx] < rev_field[idx] :

                dp_decrease[idx] = max(dp_decrease[idx], dp_decrease[cmp_idx]+1) 

    max_value = 0

    dp_decrease = dp_decrease[::-1]

    for idx in range(num):

        if dp_decrease[idx] + dp_increase[idx] > max_value:

            max_value = dp_decrease[idx] + dp_increase[idx] -1


    return max_value




print( solution() )