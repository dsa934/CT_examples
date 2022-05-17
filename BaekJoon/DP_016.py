
'''

 Backjoon _ exampels 2565

  "������"   by Jinwoo Lee

  < algorithm >

  1. A ���� ���� �� , LIS ����

    * A����, �������� ������ �ϰ�, ������� ��Ҹ� ã�� ���,

      info[idx] ����, info[0:idx-1] ���� info[idx] ���� ���� ���� ���� DP�� ���������� ������Ʈ ��

      DP[idx] = max(dp[idx] , dp[cmp_idx] + 1) 

      DP�� ã�� ������, ������ update -> �������� �ʴ� ��� �������� ���� ���� �� ���� 

     

  

 

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