
'''

 Backjoon _ exampels 4396

  "���� ã��"   by Jinwoo Lee

  < algorithm & attention >

  1. Ư�� ��ǥ(x,y)�� Ŭ�� ���� ��, �ش� ��ǥ ���� 8���⿡�� ������ ������ ã�� ��� ( find_bomb )

  2. Ư�� ��ǥ(x,y)�� Ŭ�� ���� ��, ������ ���, ���� ��� ���ڸ� ǥ�� 
  
     => index_bomb_pos �Լ��� ���� ���� ��ġ�� Ȯ��, Ŭ���� ��ǥ�� ������ ��� �ش� �Լ��� ã�� ��ġ�� *�� �ο�


  * ��� ��

  =>  ���� ���ӿ����� ���ڸ� ã���� ������ ���������,  2�� ������ ���� ��ǥ�� ���� ������� �����ϱ� ������ 

      ���� ��ǥ(x) �̸鼭, ������ ���(*) �ʿ� ���ڸ� �Ѹ���, �ٽ� ������ ���� �Ǳ� ������ ���� ǥ�ð� ���ļ� �������� ������ ��� ȥ��

      => �ش� ��ǥ�� ������ ���, �ƴѰ�츦 ������ ������ ���ļ� �������� �ʴ´�.


  
 

'''




def find_bomb(bomb_field, s_x, s_y, num):
    
    # move left right up down 11 13 17 19
    drow = [0, 0, -1, 1, -1, -1, 1, 1]
    dcol = [-1, 1, 0, 0, -1, 1, 1, -1]


    cnt = 0 

    for idx in range(8):

        n_row = s_x + drow[idx]
        n_col = s_y + dcol[idx]

        if n_row < 0 or n_col < 0 or n_row >= num or n_col >= num : continue

        if bomb_field[n_row][n_col] == '*' : cnt+=1

    return cnt


def index_bomb_pos(bomb_field, num):

    candidate = [] 

    for row_idx in range(num):

        for col_idx in range(num):

            if bomb_field[row_idx][col_idx] == '*':

                candidate.append([row_idx, col_idx])


    return candidate



def solution():
    
    num = int(input())

    bomb_field = [input() for _ in range(num)]

    use_field = [input() for _ in range(num) ]

    
    answer = [['.' for _ in range(num)] for _ in range(num) ]

    for row_idx in range(num):

        for col_idx in range(num):

            if use_field[row_idx][col_idx] == 'x' : 
                

                if bomb_field[row_idx][col_idx] != '*':

                    answer[row_idx][col_idx] = str(find_bomb(bomb_field, row_idx, col_idx, num))

                else:

                    candidate = index_bomb_pos(bomb_field, num)

                    for value in candidate:

                        answer[value[0]][value[1]] = '*'



    for idx in range(num):
        print(''.join(answer[idx]))

solution()