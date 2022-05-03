
'''

 Backjoon _ exampels 1012

  "유기농 배추"   by Jinwoo Lee

 < algorithm >

 1. dfs 알고리즘을 적용할 수 있는 pos(x,y)가 있다면 result +=1

 2. 1.에서 찾은 pos에 대하여 dfs 적용 후, 방문한 pos에 값을 모두 0으로 변환 

   => 2중 포문을 통해 pos를 찾음으로, 중복을 제외하기 위해 0으로 변환 

'''


def input_data():

    col, raw, num_vage = list(map(int, input().split()))


    field = [ [ 0 for _ in range(col)] for _ in range(raw)]


    for _ in range(num_vage):

        col_idx, raw_idx = list(map(int, input().split()))

        field[raw_idx][col_idx] = 1

        
    return field, raw, col 



def dfs(field, x, y, width, height):


    stack, visited = [] , []
    
    #   up, down, left, right
    dx = [-1, 1, 0 , 0]
    dy = [0, 0, -1, 1]

    stack.append([x,y])

    visited.append([x,y])


    

    while stack :

        _x , _y = stack.pop()


        for idx in range(4):

            n_x = _x + dx[idx]
            n_y = _y + dy[idx]


            if n_x < 0 or  n_y <0 or n_x >= width or n_y >= height :
                continue

            if field[n_x][n_y] == 0 :
                continue

            if field[n_x][n_y] == 1 and [n_x, n_y] not in visited:

                visited.append( [n_x,n_y])

                stack.append ( [n_x,n_y] )

     
    for value in visited:

        v_x, v_y = value

        field[v_x][v_y] = 0





def find_pos(field, width, height):


    result = 0

    for raw_idx in range(width):

        for col_idx in range(height):

            
            if field[raw_idx][col_idx] == 1 :
                
                result +=1
                dfs(field, raw_idx, col_idx,  width, height)


    return result 

num_test = int(input())

for _ in range(num_test):

    info_field, raw, col = input_data()
    
    print( find_pos(info_field, raw,col ) )
