

'''

 Backjoon _ exampels 10709

  "기상 캐스터"   by Jinwoo Lee

  
 

'''





def solution():

    row, col = map(int, input().split())

    field = [ list(input()) for _ in range(row)]


    for row_idx in range(row):

        cnt ,offset = 1, False

        for col_idx in range(col):
            
            if field[row_idx][col_idx] == 'c':

                field[row_idx][col_idx] = 0
                cnt = 1

                offset = True
                
            elif field[row_idx][col_idx] == '.' and offset:

                field[row_idx][col_idx] = cnt
                cnt+=1


    for row_idx in range(row):

        for col_idx in range(col):

            if field[row_idx][col_idx] == '.':
                field[row_idx][col_idx] = -1

    for idx in range(row):

        print(*field[idx])

solution()
