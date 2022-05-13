
'''

 Backjoon _ exampels 1912

  "������"   by Jinwoo Lee

  < algorithm >
 
  1.  dp[idx] = max( dp[idx-1] + info[idx] , info[idx] ) 

  2. '���ӵ� ��' ������  idx, idx-1�� �̿�


  * dp_table�� �ڱ� �ڽ��� ���� �ʱ�ȭ�ϰ�, ������(idx-1)�� ���Ͽ� dp_table �����ϱ�



  * dp ������ ī�װ�ȭ�� ��͵��� ������.. ? (2022/5/14)



'''

def solution():

    num = int(input())

    info = list(map(int, input().split()))


    dp = [value for value in info]


    for idx in range(1,num):

        dp[idx] = max( dp[idx-1] +info[idx] , info[idx])


    return max(dp)

print(solution())


