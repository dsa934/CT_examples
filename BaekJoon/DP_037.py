
'''

 Backjoon _ exampels 10826

  "�Ǻ���ġ�� �� 4"   by Jinwoo Lee

  < algorithm >

  1. �⺻ �Ǻ���ġ ����, bottom up ��� ���� 
 

'''


def solution():

    num = int(input())

    dp = [0 for _ in range(num+1)]

    if num >=1 :

        dp[1] = 1

        for idx in range(2, num+1):

            dp[idx] = dp[idx-1] + dp[idx-2]


    return dp[num]

print( solution() )