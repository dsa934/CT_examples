
'''

 Backjoon _ exampels 15624

  "�Ǻ���ġ �� 7"   by Jinwoo Lee

  < algorithm >

  1. dp ������ �������ϸ� bottom_up & memoization���� ���� 

 

'''


def solution():

    num = int(input())

    dp = [0, 1]


    if num > 1: 

        for idx in range(2, num+1):

            value = (dp[idx-1] + dp[idx-2])% 1000000007

            dp.append(value)

    return dp[num]

print(solution())