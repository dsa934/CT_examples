

'''

 Backjoon _ exampels 14655

  "������ �������̾� !!"   by Jinwoo Lee

  < algorithm >

  1. ���ӵ� 3���� ������ �����µ�,  ������ ������ Ƚ���� ������ ����

    => ������ ������ ������ �� �ִٸ� 

       a) first �� ��Ұ� ��� ����� �ɶ����� ��� ������

       b) second�� ��Ұ� ��� ������ �ɋ����� ��� ������

       �� ��������� ������ ������ �ٴ� ������ �����ߴٸ� , '3���� ���ӵ� ������ �����´�' �� ���ð� ��������


  * map function

   => ���� map ��  list(map(int , input().split() )) �� ���·� ����ߴµ� 

     int ->  lambda x : abs(int(x))  �� ä�������ν�  

     int : cast ������

     abs() : ���밪 ���ϱ� 

     �� �Լ��� ���ÿ� ���� ���� -> �ڵ尡 �� �� ���� ���� 

 

'''



def solution():
    
    num = int(input())

    first = sum( list(map(lambda x : abs(int(x)), input().split())) ) 

    second = sum( list(map(lambda x : abs(int(x)), input().split())) ) 

    print(first + second)

solution()