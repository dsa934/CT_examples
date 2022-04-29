
'''

 Backjoon _ exampels 9205

  "���� ���ø鼭 �ɾ�� "   by Jinwoo Lee


  < �˰��� >

  1. �ִ� �Ÿ� BFS �˰����� ���� ���� 

     * ������ ���� ���� �������� '��� ������ �����ؼ�' �̵�

     * ������ ������ �ִ� ��ΰ� �ƴ�, '������ ��������' ��  �ٽ�


  2. �����¿� �̵��� +- 50 �� ������ �����ϴ� ���� �ƴ϶� 

    '�߰� �������� ������'�� �Ÿ����ǿ� ���� (���� 20�� , 1000 ����) queue�� ���� �� �ִ��� �������� ���Ͽ� BFS ���� 



'''


from collections import deque

def input_data():

    num_store = int(input())

    start_x, start_y = list(map(int, input().split()))

    store = [list(map(int ,input().split())) for _ in range(num_store)]

    destination_x, destination_y = list(map(int , input().split()))



    return start_x, start_y, destination_x, destination_y, store 




def dfs(start_x, start_y, destination_x, destination_y, store):

    queue = deque()

    visited = []


    visited.append([start_x, start_y])

    queue.append([start_x, start_y])


    while queue:

        _x , _y = queue.popleft()


        if abs(_x - destination_x) + abs(_y - destination_y) <= 1000:

            return "happy"

        for idx in range(len(store)):

            n_x , n_y = store[idx]

            if [n_x, n_y] not in visited:
                
                if abs(n_x - _x) + abs(n_y - _y) <= 1000:

                    queue.append([n_x, n_y])
                    visited.append([n_x, n_y])

    return "sad"






num_test = int(input())

for _ in range(num_test):

    s_x, s_y, d_x, d_y, store = input_data()


    print(dfs(s_x, s_y, d_x, d_y, store))
