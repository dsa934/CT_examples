
'''

 Backjoon _ exampels 17175

  "�Ǻ���ġ�� ���ܿ�~"   by Jinwoo Lee

  < algorithm >

  *  ��°��� Ŀ�� �� int(1e9)+7�� ���� �������� ����ϴ� ������ ?

   => 
 

'''





def solution():

    num = int(input())

    dp = [1,1]

    mode = int(1e9) +7

    if num > 1: 

        for idx in range(2, num+1):

            value = (dp[idx-1] + dp[idx-2] + 1)%mode

            dp.append(value)

    print( dp[num] )

solution()
