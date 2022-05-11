
'''

 Backjoon _ exampels 11053

  "LIS (Longest Increasing Subsequence)"   by Jinwoo Lee

  < algorithm >

  1. cur_idx ����,  0 ~ cur_idx -1 ���� ���� ���Ͽ� �ڱ� �ڽź��� ���� ���

    dp[cur_idx] = max ( dp[cur_idx], dp[ cur_idx -1] + 1 )


    * dp[cur_idx-1 ] +1 
    
    => dp[cur_idx-1] :=  cur_idx ���� �ϳ� ������ ������ ������, ���� �� �ִ� �ִ� ������ ����

       +1            :=  numbers[cur_idx-1] �� numbers[cur_idx]���� �۱� ������, numbers[cur_idx-1]�� �ش��ϴ� ���� numbers[cur_idx]�� �κм����� ���� ������ +1 



 * dp�� Ǯ��� O(N^2) �� ���⵵ �� ���� ������, �̺�Ž�� (Binary Search)�� ���� O(nlogn)�� ������� �߰��� �����ؾ� �� 

'''

def solution():

    num = int(input())

    numbers = list(map(int, input().split()))

    dp = [1 for _ in range(num)]
    
    for idx in range(num):

        for cmp_idx in range(idx):

            if numbers[idx] > numbers[cmp_idx]:

                dp[idx] = max( dp[idx], dp[cmp_idx]+1)

    return max(dp)





print( solution() )
