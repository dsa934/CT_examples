
'''

 Backjoon _ exampels 2565

  "전깃줄"   by Jinwoo Lee

  < algorithm >

  1. A 기준 정렬 후 , LIS 적용

    * A기준, 오름차순 정렬을 하고, 최장수열 요소만 찾을 경우,

      info[idx] 기준, info[0:idx-1] 에서 info[idx] 보다 작은 값의 수를 DP로 순차적으로 업데이트 함

      DP[idx] = max(dp[idx] , dp[cmp_idx] + 1) 

      DP로 찾기 떄문에, 순차적 update -> 교차하지 않는 모든 전깃줄의 수를 구할 수 있음 

     

  

 

'''

def solution():

    num = int(input())

    info = [list(map(int, input().split())) for _ in range(num) ]
    
    sorted_info = sorted(info)
    
    
    dp = [1 for _ in range(num)]

    for idx in range(num):

        for cmp_idx in range(idx):

            if sorted_info[idx][1] > sorted_info[cmp_idx][1] :

                dp[idx] = max(dp[idx], dp[cmp_idx] +1)


    return num - max(dp)





print( solution() )