


'''

 Backjoon _ exampels 8394

  "�Ǽ�"   by Jinwoo Lee

  < algorithm >

  1. ��� �� �� �Ǽ� Ƚ���� �᳻������ �Ǻ���ġ ������ ����

  2. ��¿��� ���� �ſ� Ŀ�� �� �ֱ� ������ 1�� �ڸ��� ǥ���϶�� �䱸 

    => recursion ������� dp�� Ǫ�°��� recursion depth �ʰ��� �߻���ų Ȯ���� �������� ���� 

    => �ڷ����� ���� Ŭ���� dp array�� �������� ��� �޸� �ʰ� ������ �߻��ϴ� �� ��

    => �޸� �ʰ� ������ ���� ������ ���ڸ������� ����� �������� �����Ұ� 
 

'''



def solution():
    
    num = int(input())

    dp =  [1 for _ in range(num+1)]

    dp[1] = 1
    
    if num > 1 :

        for idx in range(2, num+1):

            dp[idx] = (dp[idx-1] + dp[idx-2])% 10


    return dp[num]

print( solution() )
