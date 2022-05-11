
'''

 Backjoon _ exampels 11053

  "LIS (Longest Increasing Subsequence)"   by Jinwoo Lee

  < algorithm >

  1. cur_idx 기준,  0 ~ cur_idx -1 까지 수를 비교하여 자기 자신보다 작은 경우

    dp[cur_idx] = max ( dp[cur_idx], dp[ cur_idx -1] + 1 )


    * dp[cur_idx-1 ] +1 
    
    => dp[cur_idx-1] :=  cur_idx 보다 하나 이전의 수까지 봤을떄, 만들 수 있는 최대 수열의 길이

       +1            :=  numbers[cur_idx-1] 이 numbers[cur_idx]보다 작기 떄문에, numbers[cur_idx-1]에 해당하는 수가 numbers[cur_idx]의 부분수열로 들어가기 떄문에 +1 



 * dp로 풀경우 O(N^2) 의 복잡도 를 갖기 떄문에, 이분탐색 (Binary Search)를 통한 O(nlogn)의 방법또한 추가로 공부해야 함 

'''

def solution():

    num = int(input())

    numbers = list(map(int, input().split()))

    dp = [1 for _ in range(num)]
    
    for idx in range(num):

        for cmp_idx in range(idx):

            if numbers[idx] > numbers[cmp_idx]:

                dp[idx] = max( dp[idx], dp[cmp_idx]+1)

    return max(dp)





print( solution() )
