
'''

 Backjoon _ exampels 7576

  "tomato - 2D"   by Jinwoo Lee


'''

from collections import deque

def input_data():

    height, width,  = list(map(int , input().split()))

    field = [list(map(int, input().split())) for _ in range(width)]


    return field, width, height



def all_tomato_riped(field, width, height):
    
    for raw in range(width):

        for col in range(height):

            if field[raw][col] == 0:

                return False
            
    return True


def bfs(field, candidate, width, height):

    if all_tomato_riped(field, width, height): return 0

    
    queue = deque()

    queue.extend(candidate)
    
    #     up, down, left, right
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    
    while queue:
        

        _x, _y = queue.popleft()


        for idx in range(4):

            n_x = _x + dx[idx]
            n_y = _y + dy[idx]
            
            
            if n_x < 0 or n_y < 0 or n_x >= width or n_y >= height:
                continue

            if field[n_x][n_y] == -1 :
                continue


            if field[n_x][n_y] == 0:

                field[n_x][n_y] = field[_x][_y] + 1

                queue.append([n_x, n_y])
                
                
    if not all_tomato_riped(field, width, height) : return -1


    max_value = 0

    for raw in range(width):

        for col in range(height):

            if field[raw][col] > max_value :

                max_value = field[raw][col]

    return max_value -1







def select_candidate(field, width, height):

    
    candidate = [] 

    for raw in range(width):

        for col in range(height):

            if field[raw][col] == 1 :

                candidate.append([raw, col])
                
              
    return candidate


info_field, width, height = input_data()

candidates = select_candidate(info_field, width, height)



print( bfs(info_field, candidates, width, height) )






