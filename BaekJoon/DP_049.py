
'''

 Backjoon _ exampels 14607

  "���� (Large)"   by Jinwoo Lee

  < algorithm >

  1. ��ȭ�� : dp[idx] = dp[idx-1] + idx-1

  2. 1 <= N <= 1e9 

    => N�� ������ ũ�� ������ 1�� ��ȭ���� dp array�� �ۼ��ϸ� memory �ʰ� �߻�

    => ���� ��, ���� idx�� ������ ������ ���� answer �ϳ��� �ʿ� 

    => dp array ��� dp scalar �� �ϳ��θ� ó���ϸ� ���


  * �迭�� �������� dp.clear() �õ� �Ѱ��� �޸� �ʰ� ��� TLE ���� �� 

    => ���� �ϳ��� �ϴ� ���� ���� 

'''


def solution():

    num = int(input())

    answer = 0 

    if num > 1:
        
        for idx in range(2, num+1):

            answer += (idx-1)

    return answer

print(solution())