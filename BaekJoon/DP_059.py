
'''

 Backjoon _ exampels 19621

  "회의실 배정2"   by Jinwoo Lee

  < algorithm >

  1. 문제에서 k-th 회의는 k+1, k-1 회의랑 시간이 겹친다는 부분에서 DP 문제임을 알 수 있음

     k번쨰 기준으로, k-2, k-3 회의 인원수와 비교하여 더 큰것을 채택하면 된다


     점화식 :  dp[idx] = max(dp[idx-2] , dp[idx-3] ) + conference[idx][2]


     bottom_up & memoization에 의거하여 풀면 아래와 같이 표기 가능 

     1회의 :  80명

     2회의 :  60명 ( 2회의와 안겹치는건 0회의, 0회의는 없음 )

     3회의 :  max(80명, 0명) + 70명 = 150명  ( 나중에 3회의를 선택하는것은 1,3회의를 선택 했다는 의미가 됨 )

     4회의 :  max(60명, 80명) + 100명 = 180명 ( dp[4]를 선택하는것은 1,4회의를 선택 했다는 의미 )
 

'''




def solution():

    num = int(input())


    conference=[[0,0,0]]

    for _ in range(num):

        s, e, people = map(int, input().split())

        conference.append([s,e,people])
        
    if num == 1 :

        dp = [0, conference[1][2] ]
        

    elif num >= 2 :
    
        dp = [0, conference[1][2] , conference[2][2] ]

        for idx in range(3, num+1):

            value = max( dp[idx-2] , dp[idx-3] ) + conference[idx][2]

            dp.append(value)
        
    print(max(dp))

solution()
