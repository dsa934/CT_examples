

'''

 Backjoon _ exampels 2491

  "����"   by Jinwoo Lee

  < algorithm >

  1. LIS�� Ǯ���� ������, ���ӵ� ���� ��� LIS�� �� �ʿ䰡 ����

    => 2�� ������ �̿��ؼ� idx ����, 0~idx�� ���� ���� �ʿ䰡 ���ٴ� ��


  2. ���ӵ� �� ������ , idx ���� idx-1���� ũ�� �񱳸�  �ؼ� dp[idx]�� �����ϸ��

     => dp[idx] = max( dp[idx], dp[idx-1] +1 )


  3. �����ϴ� ������ ���̵� ���������� ��ȣ�� ����� ���� 
 

'''


def solution():
    

    length = int(input())

    numbers = [0] + list(map(int, input().split()))

    dp = [1 for _ in range(length+1)]

    dp_rev = [ 1 for _ in range(length+1) ]

    
    for idx in range(2,length+1):
        
        if numbers[idx] >= numbers[idx-1]:

            dp[idx] = max(dp[idx], dp[idx-1] + 1 )

        if numbers[idx] <= numbers[idx-1]:
                
            dp_rev[idx] = max(dp_rev[idx], dp_rev[idx-1] + 1 )
                  
    
    return max( max(dp_rev) , max(dp) )


print( solution() )


