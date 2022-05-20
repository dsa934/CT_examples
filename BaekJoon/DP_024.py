
'''

 Backjoon _ exampels 14916

  "�Ž��� �� "   by Jinwoo Lee

  < algorithm >

  1. �Ž������� ������ ����, user�� 1��

    => �ݾ׿� ���� �Ž������� ���� dp array ���� ( ���� ����� ������ ���� )

    =>     0     1     2     3     4     5     6     7     8
          max   max    1    max    2     1     


          idx > 5 , dp[idx] = min ( dp[idx-2], dp[idx-5] ) + 1 


  2. idx-5�� ����ϱ� ������, init value�� 1~ 5������ �������� �� 

     => dp [ max_value for _ in range( num + 5 )]   // num+5 �� ���� 

     => �ʱ� ��Ұ����� ũ�� ��Ƴ����� min ���� �񱳰� ���� �� 


'''



def solution():
    
    num = int(input())

    max_value = 100000 +1

    dp = [max_value for _ in range(num+5) ]

    dp[2] = 1
    dp[4] = 2
    dp[5] = 1

    for idx in range(6, num+1):
        
        dp[idx] = min( dp[idx-2], dp[idx-5]) + 1

    return  dp[num] if dp[num]!= max_value else -1


print( solution() )