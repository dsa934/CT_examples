
'''

 Backjoon _ exampels 1463

  "1�� �����"   by Jinwoo Lee

  < algorithm >

  1. ���� ������ ��� ����� Ȱ�� 

     dp[idx] = dp[idx-1] + 1   => ���ڰ� 1���� �߱� ������ �ּ��� -1 ������ Ȱ������� Ƚ�� 1 ����


  2.  Greedy method ���� �Ұ� 

     * /3 , /2 , -1 �߿� � ����� �ּ����� �� �� ����

       => greedy�� ����Ƿ���, �ּҺ���� ���ϴ¸�ŭ /3�� ������ �ذ� ����Ǿ�� �ϴµ� �ش� ������ �׷��� ���� 

          �̿� ���� ���÷� '10 -> 9 -> 3 -> 1 ' �־���


  3.  dfs/bfs ���� �Ұ���

     * ���������κ��� ����������  /3 , /2 , -1 �� 3���� ����� ����Ͽ� ���� ���� �����ϴ� (�ִܰ�� ����) ��� ������ �� ������,

       /3 , /2 , -1 �� ���� ���� ������ '�Ұ���'�� ��찡 ���� 


  4.  /3, /2, -1 ��� ���� �ּ����� �𸣱� ������ ��� ���ؼ� �ּҰ��� �����ؾ� �Ѵ�.



'''

def make_one():

    num = int(input())

    dp_table = [0] * (num +1)
    

    for idx in range(2, num+1):

        dp_table[idx] = dp_table[idx-1] +1


        if idx % 2 == 0 :

            dp_table[idx] = min (dp_table[idx], dp_table[idx//2]+1 )

        if idx % 3 == 0:

            dp_table[idx] = min (dp_table[idx], dp_table[idx//3]+1 ) 

    return dp_table[num]

print (make_one())