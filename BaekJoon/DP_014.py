
'''

 Backjoon _ exampels 11722

  "���� ū �����ϴ� ���� "   by Jinwoo Lee


  < algorithm >

  1. LIS ������ �˰��� ���� but number list�� ����� ���� 

   * �����ϴ� ������ �ݴ��� �ؼ�, info[idx] < info[cmp_idx]�� �ϰ� �Ǹ�,

     idx ����, �ִ� ���̰� ����Ǵ� ���� �ƴ϶� ���� �� ���� ���� ���� ���� value�� dp[idx]�� ����ǰ� ��


   * ������ ����� number list ��ü�� ����� �ϸ�, �� idx ����, �����ϴ� ������ ���̸� ������ �� ���� 


 

'''


def solution():

    num = int(input())

    field = list(map(int, input().split()))

    dp = [ 1 for _ in range(num) ]

    rev_field=field[::-1]

    for idx in range(num):

        for cmp_idx in range(idx):

            if rev_field[idx] > rev_field[cmp_idx]:

                dp[idx] = max(dp[idx], dp[cmp_idx] +1)

    return max(dp)

print( solution() )


