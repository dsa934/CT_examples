
'''

 Backjoon _ exampels 11034

  "Ļ�ŷ� ������2"   by Jinwoo Lee

  < algorithm >

  1. ���� ���򼱻� �ִٰ� �߿��� ��Ʈ

    A,B,C�� ���Ͽ�,  A < B <  C �� ���·� �����ϸ�


    C-B �� A�� �� �� �ִ� ����

    B-A �� C�� �� �� �ִ� ����


    A,B,C ������ ���̰� 1�̸� ������ ���� ������ ���� �Ұ���


    ��  A,B,C = 4,6,10 

        C-B = 4 ( 7,8,9,10 )  - 1 , 10�� �������̶� -1

        B-A = 2 ( 5,6 ) , 6�� ������������ -1



        ��ȭ�� : max(B-A, C-B) -1 

 

'''





def solution():

    while True :

        try :

            a,b,c, = map(int, input().split())

            print( max(b-a, c-b) -1 )
       
        except:
            break

solution()