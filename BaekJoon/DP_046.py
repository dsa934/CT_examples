

'''

 Backjoon _ exampels 24416

  "�˰��� ����- �Ǻ���ġ �� 1 "   by Jinwoo Lee

  < algorithm >

  *  5 <= n < = 40 �ϋ� �Ʒ��� �ڵ尡 ���� ������,

   n �� ������ �� Ŀ���� �Ʒ��� �ڵ�� TLE�� ������ ��  ( ref, �˰��� ���� - �Ǻ���ġ �� 2 )

   => �̸� �ذ��ϱ� ���� ����� �ʿ� ��� (2022.5.30)


 

'''




num =int(input())

dp = [1,2]

if num > 1:

    for idx in range(2, num+1):
            
        value = (dp[idx-1] + dp[idx-2]) % 1000000007

        dp.append(value)

print( dp[num-2], num-2 )

