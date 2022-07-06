
'''

 Backjoon _ exampels 14437

  "������ ȿ�����̾�"   by Jinwoo Lee

  < algorithm >

  1. ������ �������� ���� ���ƾ����� �̵��� �����ϱ� ������ �� ������ ������� �湮���� �� �ּҺ���� ���� ����������,

    '���� ����'�� ���� ���� �ϴ��Ŀ� ���� ����� �����ȴ�.


  2. ���ʽõ� )

     �Է¹��� �̵���� ����Ʈ�� �����Ͽ� concate �Ѵ�. [1,2,3,4]  =>  [1,2,3,4,1,2,3,4]

     => ���ٸ� ��ġ ����, for���ȿ��� 0~������ �� ���������� ����, [idx:idx+num-1]�� ���� �����ָ� ��

     => �� ��� TLE �� �߼�


     �ذ� Ǯ�� )

     ��ü �̵� ��θ� ���� ��, ���� ū ���� ���°��� ������ ���ϴ� ���ʽõ� ���� ������ ���� ���� 

     
 

'''



def solution():

    num = int(input())

    cost = list(map(int, input().split()))

    cost.extend(cost)
    
    min_value = int(1e10)

    interval = num-1

    for idx in range(��):
        
        if min_value > sum(cost[idx:idx+interval]) :

            min_value = sum(cost[idx:idx+interval])

    print(min_value)
