
'''

 Backjoon _ exampels 1417

  "��ȸ�ǿ� ����"   by Jinwoo Lee

  < algorithm >

  1. �Է��� ù������ �ټؿ� �ش��ϴ� ��ȣ 1�� ������ , �̸� ������ ������ �ĺ��� ������������ ����

  2. �������� ���� �� , sub_candidate[0]�� �׻� ū���� ����������, 

     �� ���� ��ȣ1���� �ش��ϴ� dasom ���� ���ؼ� dasom�� ���� Ŭ������ �ش� ������ �ݺ� 
 

'''


def solution():

    num = int(input())

    candidate = [ int(input()) for _ in range(num)]

    if num == 1 : print(0)


    else:


        answer = 0 

        sub_candidate = sorted(candidate[1:], reverse= True)

        dasom = candidate[0]

 

        while sub_candidate[0] >= dasom :

            dasom +=1

            sub_candidate[0] -=1

            answer +=1

 
            sub_candidate = sorted(sub_candidate, reverse = True)


        print(answer)



solution()