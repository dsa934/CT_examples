

'''

 Backjoon _ exampels 14720

  "���� ����"   by Jinwoo Lee

  < algorithm >

  * 0->1->2 �� ��ȯ�Ǵ� ������ ����, 3���� ���� ������ �����̶�� ���̵� �̿�
 

'''

def solution():

    num = int(input())

    candidate = list(map(int ,input().split()))

    cnt, answer = 0, 0


    for idx in range(num):

        if candidate[idx] == cnt%3:

            cnt+=1

            answer +=1

    print(answer)

solution()