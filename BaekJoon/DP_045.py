
'''

 Backjoon _ exampels 2193

  "��ģ��"   by Jinwoo Lee

  < algorithm >

  1. 01 Ÿ�� ������ �ٸ��� ���� ( �Ǻ���ġ ����)
 

'''

def solution():

    num = int(input())

    dp = [0,1]

    if num > 1 : 

        for idx in range(2, num+1):

            value = dp[idx-1] +dp[idx-2]

            dp.append(value)

    return dp[num]


print(solution())