
'''

 Backjoon _ exampels 19621

  "ȸ�ǽ� ����2"   by Jinwoo Lee

  < algorithm >

  1. �������� k-th ȸ�Ǵ� k+1, k-1 ȸ�Ƕ� �ð��� ��ģ�ٴ� �κп��� DP �������� �� �� ����

     k���� ��������, k-2, k-3 ȸ�� �ο����� ���Ͽ� �� ū���� ä���ϸ� �ȴ�


     ��ȭ�� :  dp[idx] = max(dp[idx-2] , dp[idx-3] ) + conference[idx][2]


     bottom_up & memoization�� �ǰ��Ͽ� Ǯ�� �Ʒ��� ���� ǥ�� ���� 

     1ȸ�� :  80��

     2ȸ�� :  60�� ( 2ȸ�ǿ� �Ȱ�ġ�°� 0ȸ��, 0ȸ�Ǵ� ���� )

     3ȸ�� :  max(80��, 0��) + 70�� = 150��  ( ���߿� 3ȸ�Ǹ� �����ϴ°��� 1,3ȸ�Ǹ� ���� �ߴٴ� �ǹ̰� �� )

     4ȸ�� :  max(60��, 80��) + 100�� = 180�� ( dp[4]�� �����ϴ°��� 1,4ȸ�Ǹ� ���� �ߴٴ� �ǹ� )
 

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
