
'''

 Backjoon _ exampels 11504

  "���� �� ������� �κ� ����"   by Jinwoo Lee


  < algorithm >

  1. 11503 LIS ������ ����� �ι� �̿��ϸ� �ȴ�.


   * idx�� �������� 0 ~ idx-1 ������ ���� ���� dp �˰����� �����Ѵ�

     dp[idx] = max ( dp[idx], dp[cmp_idx]+1 ) 


  2. ������� �κ� ������ ���� ���� S_t�� �������� , S_t-1 < S_t  and  S_t > S_t+1 �̱� ������ 

    ���� ���� numbers[idx]�� ���ؼ� 
    
    a)  numbers[0] ~ numbers[idx-1]  

    b)  numbers[idx+1] ~ numbers[-1]

    
    a), b) �ΰ��� ������ ���ؼ� ���� dp �˰����� �����ؾ� �ϸ�, 

    b)�� ��� a)���� ���Ǵ� dp �˰����� ������ ��� �迭�� '������'�� �Ѵ� (������ �ٸ��� ������)


  3. ��� �� 

    max_value =  max  ( dp_increase[idx] + dp_decrease[::-1][idx] ) - 1  

    dp_increase ( a case ) , dp_decrease( b case) �� ��� ���� ��, 

    
    increase �� decresae�� idx�� �����ֱ� ���Ͽ� dp_decrease�� �ٽ� �����´�.

    
    �������� ���� �ؾ� ������ ��������� -1�� ���ش� 





  * ���������� ������� ���� ���� ���α��� �Ǵ��϶�� �ߴµ�, �ش� �κп� ���� ó���� ��� pass ������ ���� �� ����

    => LIS �迭 ������ �� Ǯ��鼭 ���� �� �����ϱ� 

 

'''


def solution():

    num = int(input())

    field = list(map(int, input().split()))

    dp_increase = [1 for _ in range(num)]
    dp_decrease = [1 for _ in range(num)]


    rev_field = field[::-1]
    
    for idx in range(num):

        for cmp_idx in range(0,idx):

            if field[cmp_idx] < field[idx] :

                dp_increase[idx] = max(dp_increase[idx] , dp_increase[cmp_idx]+1 ) 


            if rev_field[cmp_idx] < rev_field[idx] :

                dp_decrease[idx] = max(dp_decrease[idx], dp_decrease[cmp_idx]+1) 

    max_value = 0

    dp_decrease = dp_decrease[::-1]

    for idx in range(num):

        if dp_decrease[idx] + dp_increase[idx] > max_value:

            max_value = dp_decrease[idx] + dp_increase[idx] -1


    return max_value




print( solution() )