
'''

 Backjoon _ exampels 25214

  "ũ�� �Ľ�Ÿ"   by Jinwoo Lee

  < algorithm >
 
  1. ���� ���� 

    < ���� >  A : ��迭, a_i : i��°�� �߰��� ������

    => a_i�� A�� �߰��� ��,  A[0 : i] (�ڱ� �ڽ� ���� ������ i����)  ������ �ִ� �����Ϳ� ���Ͽ� ���� ū �� ���

    dp[idx] = max( dp[idx-1], numbers[idx] - min_value)

    dp array�� �����ϴ� �� ó��, �迭���� ���� ���� ���� ���� ( �߰��ҋ����� �ѹ��� �� �ϱ� ������ O(1) ���⵵ )


  * ���� �õ��� min(numbers[:idx]) �� ����ߴµ� N ���߿� ã�ƾ� ������ O(N) 

    �߰� �Ǵ� �����Ͱ� n�������� �� �ð����⵵�� O(N^2) �� �Ǿ� TLE


    => �߰��Ҷ����� ���� ���� min_value�� �����ϸ� �ش� �۾��� �ð����⵵ O(1)

       �� �ð� ���⵵�� O(N * 1 ) = O(N)  => TLE �ذ� 



'''



def solution():
    

    num = int(input())

    numbers = list(map(int, input().split()))

    dp = [0 for _ in range(num)]

    min_value = numbers[0]
    
    for idx in range(1,num):

        if min_value > numbers[idx]:

            min_value = numbers[idx]

        dp[idx] = max( dp[idx-1] , numbers[idx] - min_value )


    return dp


print(* solution() )
