
'''

 Backjoon _ exampels 2714

  "문자를 받은 승환이"   by Jinwoo Lee

  < algorithm >

  * search 방법 = 달팽이 모양

   1) bfs를 이용하여, 이동 방향을 right, down, left, up 순으로 배치한다

   2) right, up을 동시에 만족하는 것에 대한 예외 처리 필요 

      ㅁ ㅁ ㅁ ㅁ
      x  ㅁ ㅁ ㅁ
      ㅁ ㅁ ㅁ ㅁ

      위와 같은 field 에서, 달팽이 관 형태로 돌았다면 x에 도착했을때 right, up이 동시에 가능하기 때문에 

      달팽이 형태로 이동시키기 위해서는 up을 우선시 하도록 셋팅하면 된다.  -> special case _1 


   3) 이동에 성공하면 break를 걸어야 달팽이 처럼 이동 가능 


  * 공백 문자열

  1) 문제에서는 row*col 만큼 msg가 없을 경우 zero_padding을 해줬는데 이에 대한 언급을 명확히 이해하지 못해서 zero_padding 따로 구현 => 굳이 안해도 되지만 있으면 좀더 탄탄해짐 

  2) 0일때 공백으로 처리


  * n진수 -> 10진수

  int(n진수_value, n진수)  =>   int(0110101, 2)   # 2진수 -> 10진수 
 

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