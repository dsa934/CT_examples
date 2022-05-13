
'''

 Backjoon _ exampels 1912

  "연속합"   by Jinwoo Lee

  < algorithm >
 
  1.  dp[idx] = max( dp[idx-1] + info[idx] , info[idx] ) 

  2. '연속된 수' 임으로  idx, idx-1을 이용


  * dp_table을 자기 자신의 수로 초기화하고, 이전값(idx-1)과 비교하여 dp_table 갱신하기



  * dp 문제의 카테고리화는 어떤것들이 있을까.. ? (2022/5/14)



'''

def solution():

    num = int(input())

    info = list(map(int, input().split()))


    dp = [value for value in info]


    for idx in range(1,num):

        dp[idx] = max( dp[idx-1] +info[idx] , info[idx])


    return max(dp)

print(solution())


