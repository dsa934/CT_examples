
'''

 Backjoon _ exampels 2670

  "���Ӻκ��ִ��"   by Jinwoo Lee

  < algorithm >
 
  1. ���� + dp ������ ���� idx, idx-1�� ���ϸ� �ذ��� �ȴ�


   => ���� idx ����, �Ʒ��� ���� ���� ���� 

      dp[idx] = max( dp[idx], dp[idx-1] * dp[idx] )   # ���簪, Ȥ�� �������� ���簪�� ���� �� �߿� ū��

      dp[idx-1]�� �̹�, ���� �������� ������ ���� ���� ��� max( dp[idx-1] , dp[idx-2] * dp[idx-1]) �� ������ ������ ������

      ���� idx-1 �� ���ؼ��� ������ ���� �Ǿ��ִٰ� �� �� �ִ� ( ������ �ƴ϶�� idx-1���� ���� ��ȭ�� ���� ���� )

      ��, idx ���ؿ��� idx-1 ������ �񱳸� �ص� �Ǵ� �� 



  2. 1�� ������ �޹�ħ �ϱ� ����, �ʱ�ȭ�� ����� �ؾ� �Ѵ�

   => �ڸ���/ ���� ���� : dp = [ 1 for _ in range( �������� �־����� ���� )]

   => �հ� ���� �� ���� : dp = [ value for value in range(�������� �־����� ���� )]
  



'''


def solution():

    num = int(input())

    numbers = [] 

    for _ in range(num):

        numbers.append(float(input()))
        
    dp = [0] + [value for value in numbers ]
    

    for idx in range(2, num+1):

        dp[idx] = max( dp[idx], dp[idx-1] * dp[idx])
            

    return f'{max(dp):.3f}'

print( solution() )