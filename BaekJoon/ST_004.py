
'''

 Backjoon _ exampels 2714

  "���ڸ� ���� ��ȯ��"   by Jinwoo Lee

  < algorithm >

  * search ��� = ������ ���

   1) bfs�� �̿��Ͽ�, �̵� ������ right, down, left, up ������ ��ġ�Ѵ�

   2) right, up�� ���ÿ� �����ϴ� �Ϳ� ���� ���� ó�� �ʿ� 

      �� �� �� ��
      x  �� �� ��
      �� �� �� ��

      ���� ���� field ����, ������ �� ���·� ���Ҵٸ� x�� ���������� right, up�� ���ÿ� �����ϱ� ������ 

      ������ ���·� �̵���Ű�� ���ؼ��� up�� �켱�� �ϵ��� �����ϸ� �ȴ�.  -> special case _1 


   3) �̵��� �����ϸ� break�� �ɾ�� ������ ó�� �̵� ���� 


  * ���� ���ڿ�

  1) ���������� row*col ��ŭ msg�� ���� ��� zero_padding�� ����µ� �̿� ���� ����� ��Ȯ�� �������� ���ؼ� zero_padding ���� ���� => ���� ���ص� ������ ������ ���� źź���� 

  2) 0�϶� �������� ó��


  * n���� -> 10����

  int(n����_value, n����)  =>   int(0110101, 2)   # 2���� -> 10���� 
 

'''




from collections import deque


def make_field(row, col, msg):
    
    msg = list(msg)
    
    # zero padding
    if len(msg) != row*col :

        for _ in range(abs( (row*col)-len(msg) ) ):

            msg.append('0')

    field = [] 

    for idx in range(0, row*col, col ):


        field.append(msg[idx:idx+col])

    return field


def decode_bfs(field ,row, col):
    

    queue = deque([[0,0]])

    visited = [ [False for _ in range(col)] for _ in range(row) ]
    visited[0][0] = True
    
    # move order right, down, left, up
    drow = [0, 1, 0, -1]
    dcol = [1, 0, -1, 0]

    answer = [field[0][0]]


    while queue :

        _x, _y = queue.popleft()

        for idx in range(4):

            n_x = _x + drow[idx]
            n_y = _y + dcol[idx]

            if n_x < 0 or n_y < 0 or n_x >= row or n_y >= col : continue

            if not visited[n_x][n_y]:

                # special case 1
                # right move
                if idx == 0 :  

                    temp_x = _x + drow[3]
                    temp_y = _y + dcol[3]

                    if 0 <= temp_x < row and 0<= temp_y < col and not visited[temp_x][temp_y] :

                        n_x = temp_x
                        n_y = temp_y


                queue.append([n_x,n_y])
                visited[n_x][n_y] = True
                answer.append(field[n_x][n_y])
                break


    return answer



def solution():
    

    row, col, msg = input().split()

    field = make_field(int(row), int(col), msg)

    answer_list =  decode_bfs(field , int(row), int(col) )


    decode_dict ={0:' ', 1 :'A',  2 :'B', 3 :'C', 4 :'D', 5 :'E', 6 :'F', 7 :'G', 8 :'H', 9 :'I', 10 :'J', 11 :'K', 12 :'L', 13 :'M', 14 :'N', 15 :'O', 16 :'P', 17 :'Q', 18 :'R' , 
                  19 :'S' ,20 :'T', 21 :'U' ,22 :'V' ,23 :'W', 24 :'X' ,25 :'Y' ,26 :'Z' }


    answer = []
    for idx in range(0, len(answer_list), 5):
        
        # binary -> int
        answer.append( decode_dict[int(''.join(answer_list[idx:idx+5]),2)] )

    print(''.join(answer).strip())



num_test = int(input())

for _ in range(num_test):
    solution()