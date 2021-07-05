'''

 Backjoon _ exampels #

  "(Implementation)"   by Jinwoo Lee


 # Attention for Implementation

  1. KING/stone이 문자열이기 떄문에 king[1] = 't' 와 같이 수정이 불가능함, REPLACE를 사용해야함 

     => king/stone list화 하면 되는데 범위판별에 그렇게 사용하지 않았기 떄문에 replace를 활용


  2. 범위 체크할떄 다시한번 신경쓰기 

     => 최초에 문제를 틀린 이유가 stone, king 위치가 중복일 경우 - 킹과 같은 방향으로 움직인 stone이 체스판을 벗어나지 않을 경우에 대한 처리가 되있지 않았음


'''

def is_check(king, stone, value):

    row, col = value[0], value[1]

    row_king, col_king = king[0], king[1]

    row_stone, col_stone = stone[0], stone[1]


    # king 범위 확인 
    if ord(row_king) + row < 65 or ord(row_king) + row > 72 or int(col_king) + col < 1 or int(col_king) + col > 8 : return 0


    else:
        
        # stone 과 중복인지 확인
        if ord(row_king) + row == ord(row_stone) and int(col_king) + col == int(col_stone) : 

            if ord(row_stone) + row < 65 or ord(row_stone) + row > 72 or int(col_stone) +col < 1 or int(col_stone) + col > 8 : return 1

            else: return 2



        else : return 3



move = {'R' : [1,0] , 'L' : [-1,0] , 'B' : [0,-1] , 'T' : [0,1] , 
       'RT' : [1,1] , 'LT' : [-1,1] , 'RB' : [1,-1] , 'LB' : [-1,-1] }


king, stone, num = list(input().split())

oper = [input() for _ in range(int(num))]


for value in oper:

    flag = is_check(king, stone, move[value])


    # case 0 : king - out of area
    if flag == 0 or flag == 1: continue

    # case 1 : king - stone duplicate
    elif flag == 2 : 

        king = king.replace(king[0], chr(ord(king[0])+move[value][0]))
        king = king.replace(king[1], str(int(king[1])+move[value][1]))

        stone = stone.replace(stone[0], chr(ord(stone[0])+move[value][0]))
        stone = stone.replace(stone[1], str(int(stone[1])+move[value][1]))



    # case 2 : only king move
    elif flag == 3:

        king = king.replace(king[0], chr(ord(king[0])+move[value][0]))
        king = king.replace(king[1], str(int(king[1])+move[value][1]))


print(king)
print(stone)