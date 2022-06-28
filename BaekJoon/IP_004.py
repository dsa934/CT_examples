
'''

 Backjoon _ exampels 1205

  "��� ���ϱ�"   by Jinwoo Lee

  < algorithm >

  1. N == 0 ,  N != 0 

     N == 0 �̸� ������ 1��


  2. N == P �ε� score�� ��������(���� ������) ���� �¼��� ������ ������ ��ŷ�� �� �ڸ����� ���� ������ -1 ���


  3. N != P �� ���,  

    �¼��� ������ N+1 �� �ʱⰪ ����( ���� ��ŷ�� ���ٰ� ����)

    ���� score ������ ���鼭 �¼� �������� ���� ������ �ִٸ� �� index+1 �� ���� ��

    index�� 0���� ���������� index+1 �ؾ���




    * ��� ���ҋ� �����ڰ� �ִٰ� �ؼ� �ʹ� ��ư� dict ������ �Ἥ ���� ���� , ����ȭ �ϱ� 

    * ���� üũ .0 <= N <= P 

'''


def solution():

    n, score, p = map(int, input().split())

    if n == 0: answer = 1

    else:

        score_board = list(map(int, input().split()))

        if n == p and score_board[-1] >= score : answer = -1
            
        else:

            answer = n +1

            for i in range(n):

                if score_board[i] <= score :

                    # idx �� 0���� �����̴� +1 ����� ���� ����� ����,  score���� ������ ã���� ���ڸ��� ���Ե� �ڸ���
                    answer = i +1 
                    break
        
    print(answer)
solution()