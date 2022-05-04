
'''

 Backjoon _ exampels 1003

  "�Ǻ���ġ �Լ�"   by Jinwoo Lee

  < algorithm >

  1. bottom up & memoization�� Ȱ���� �Ǻ���ġ ���� ����

  2. N := n��° �Ǻ���ġ �� ( N�� ����� �Ǻ���ġ �� ��� �ǹ̷� ȥ�� ���� ���� )

  3. N�� �����ϱ� ���� 1�� 0�� ��� ���Դ��� �� ���� �����̸�,

     0,1 ������ f(n) = f(n-2) + f(n-1)�� �����ϸ� N�� ° ���� ���� 0,1�� ���� ��� ���Ǿ������� ���� '����'�� �� �� ���� 
  


'''




def fib_naive(n):

    zero = [0 for _ in range(41)]
    one = [0 for _ in range(41)]
    
    zero[0], one[0] = 1,0
    zero[1], one[1] = 0,1
    
    if n >= 2 :


        for idx in range(2, n+1):

            zero[idx] = zero[idx-2] + zero[idx-1] 
            one[idx] =  one[idx-2] + one[idx-1] 


    print(zero[n], one[n])

num_test = int(input())

for _ in range(num_test):
    
    fib_naive(int(input()))