
'''

 Backjoon _ exampels 9657

  "�� ���� 3"   by Jinwoo Lee

  < algorithm >
 
  1. �ش� ������ �������� ���� �������� �÷��̾ �¸��ϴ� ���� 

     * ���� 1, 3, 4 �� ���� �� �� �ִ�



  2. N�� ���Ͽ� N-1, N-3, N-4 �� ����� ���� �ִ�.


     * 1 <= N <= 4 �� ���, init value�� ���� ���� ����

     * N >= 5�� ���, prev_value = [ N-1, N-3, N-4 ] �� ����ص� ���� ������ 0�� ���� �ʴ´�

       ��,  prev_value �߿� �ѹ��̶� 'CY'�� ������ (������̸�) ���� ���� 'SK'�� ���� ���� ������ �¸��Ѵ�




  * �Ϻ��ϰ� �����Ѵ� => �̱� �� �ִ� ������ �ִٸ� ������ �� ���� ���´� ( ������ ���� ���´� )

'''

def solution():

    num = int(input())

    dp = [0, 'SK', 'CY', 'SK', 'SK']

    if num > 4:

        for idx in range(5, num+1):

            if 'CY' in [ dp[idx-1], dp[idx-3], dp[idx-4] ] :

                dp.append('SK')

            else:
                dp.append('CY')
    return dp[num]


print( solution() )