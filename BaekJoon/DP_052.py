
'''

 Backjoon _ exampels 9711

  "�Ǻ���ġ"   by Jinwoo Lee

  < algorithm >

  1. python ����� TLE, pypy3 ����� pass

    => python Ǯ�� �߿���, P�� ������ 10000 ���������� �̸� 10000 ���� ���� �������� ����� ���ϸ� Pass ���� �� ����

      �׷��� ȿ���������� �ǹ� 


  2. �Ʒ� �ڵ尡 ���� ���� 

    * ���� �ӵ��� ����   pypy 3 > pyhon 3

       pypy3(�����Ϸ�) > python3 (���������� ���)


    * pypy3�� �޸𸮸鿡�� ����

      => object code ����, linking ����( object code ����) ������ �޸� ȿ���� ���������� ��Ŀ� ���� ������


    * ���� ���⵵�� O(1)

      => dp array�� ����� ��� ���� ���⵵�� O(n) ������,

         bottom_Up & memoization ����� ����� ���, ���������� ���ؾ��ϴ� ���� t�� ���� ���ϱ� ����  t-1 ���� ������ �Ǳ� ������ �������⵵ O(1) ���� ����


    �� ���������, ����ӵ��� ������ �޸� ȿ���� ������ pypy3 �� ����ϸ鼭, �������⵵�� O(1)�� �ٿ� �޸𸮿��� ��� ���ظ� ������� zero_sum �ϰ��� �� �ڵ� 

 

'''


def solution():

    p, q = map(int ,input().split())


    prev_1, prev_2 = 1,1

    if p > 2 :

        for _ in range(3, p+1):

            prev_2, prev_1 = (prev_1 + prev_2 ), prev_2

    return prev_2 % q



num = int(input())

for idx in range(1,num+1):


    ans = solution()


    print(f'Case #{idx}: {ans}')



