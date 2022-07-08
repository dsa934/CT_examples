
'''

 Backjoon _ exampels 4396

  "지뢰 찾기"   by Jinwoo Lee

  < algorithm & attention >

  1. 특정 좌표(x,y)를 클릭 했을 때, 해당 좌표 기준 8방향에서 지뢰의 개수를 찾아 출력 ( find_bomb )

  2. 특정 좌표(x,y)를 클릭 했을 떄, 지뢰인 경우, 맵의 모든 지뢰를 표시 
  
     => index_bomb_pos 함수를 통해 지뢰 위치를 확보, 클릭한 좌표가 지뢰일 경우 해당 함수로 찾은 위치에 *을 부여


  * 헷깔린 점

  =>  실제 게임에서는 지뢰를 찾으면 게임이 종료되지만,  2중 포문을 통해 좌표에 따라 순서대로 진행하기 떄문에 

      사용된 좌표(x) 이면서, 지뢰일 경우(*) 맵에 지뢰를 뿌리고, 다시 포문이 진행 되기 떄문에 지뢰 표시가 겹쳐서 지워지지 않을까 잠시 혼동

      => 해당 좌표가 지뢰일 경우, 아닌경우를 나눴기 떄문에 겹쳐서 지워지지 않는다.


  
 

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