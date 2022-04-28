

'''

 Backjoon _ exampels 7569

  "Tomato"   by Jinwoo Lee

  < 알고리즘 >

  1. 2차원 평면 최단 거리 문제를 3차원에 적용 

     dx = [1, -1, 0, 0, 0 ,0]   이동 방향이 6방향 
     dy = [0, 0, 1, -1, 0, 0]
     dz = [0, 0, 0, 0, 1, -1]



  2.  최단거리 문제와 동일하게, 최초 방문한 토마토가 몇일만에 만난지 value update 후 queue에 해당 토마토의 좌표값  추가 


  3. visited를 활용할 필요는 없음, all_tomato_ripe 함수를 통해 

     a) queue 진행 전에 검사 -> 모든 토마토가 이미 익어있는 경우 판별

     b) queue 이후 검사 -> 혹시라도 익지 못하는 토마토가 있는 경우 판별




  * 최초 시도 시간 초과 (TEL)  => 해결 
  
    queue = stack()   =>  queue = deque() 
    queue.pop(0)      => queue.popleft()   


    => Reason 정리 

    1. 일반적으로, pop() 연산은 O(1) 시간이 걸리지만, 
    
       pop(0)의 경우 :  O(1) + O(N-1) =  O(N) 
       
       why ?  idx 0 위치의 data 삭제 후,   남아 있는 n-1 개의 data를 빈자리를 메꾸기위해 땡겨줘야 함으로 O(N-1) 의 시간이 추가로 걸리게 된다 
       
       
    2. deque()의 popleft() 연산의 경우 O(1)이다 

      => doubled linked list로 구성되있으며, deque의 크기가 얼마나 크던지 간에 삭제 연산만 일어나기 떄문에 o(1)로 고정된 constant time이다.



 

'''

from collections import deque

def make_field():

    width, height, num_box = list(map(int, input().split()))

    field = [ [ list(map(int, input().split()))  for _ in range(height) ] for _ in range(num_box)]


    return field, width, height, num_box


def search_tomato(field, width, height, num_box):

    candidate = []

    for _z in range(num_box):

        for _y in range(height):

            for _x in range(width):


                if field[_z][_y][_x] == 1 : 

                    candidate.append([_x, _y, _z])

    return candidate


def all_tomato_ripe(field, width, height, num_box):

    for _z in range(num_box):

        for _y in range(height):

            for _x in range(width):
                
                if field[_z][_y][_x] == 0 :
                    return False


    return True


def check_empty_space(field, width, height, num_box):

    cnt = 0

    for _z in range(num_box):

        for _y in range(height):

            for _x in range(width):
                
                if field[_z][_y][_x] == -1 :
                    
                    cnt +=1

    return cnt




def max_value(result, width, height, num_box):
    

    max_value = 0

    for _z in range(num_box):

        for _y in range(height):

            for _x in range(width):

                if result[_z][_y][_x] > max_value : max_value = result[_z][_y][_x] 



    return max_value -1


def bfs(field, candidate, width, height, num_box):
    
    if all_tomato_ripe(field, width, height, num_box) : return 0

    else:
        
        queue = deque()

        queue.extend(candidate)
        
        # 2D - up , down, left, right  
        dx = [0, 0, -1, 1, 0, 0]
        dy = [1, -1, 0, 0, 0, 0]

        # 3D  - up /down 
        dz = [0,0 ,0, 0,  1 , -1 ]


        while queue :
            
           _x, _y, _z = queue.popleft()
           
           for idx in range(6):

               n_x = _x + dx[idx]
               n_y = _y + dy[idx]
               n_z = _z + dz[idx]


               if n_x < 0 or n_y < 0 or  n_z < 0 or n_x >= width or n_y >= height or n_z >= num_box: 
                   continue

               if field[n_z][n_y][n_x] == -1 : 
                   continue

               if field[n_z][n_y][n_x] == 0 :
                   
                  field[n_z][n_y][n_x] = field[_z][_y][_x] + 1

                  queue.append([n_x ,n_y, n_z])
                  
    if not all_tomato_ripe(field, width, height, num_box) : return -1

    else:

        result = max_value(field, width, height, num_box)

        return result

    


info_field, width, height, num_box = make_field()

info_candidate = search_tomato(info_field, width, height, num_box)

result = bfs(info_field, info_candidate, width, height, num_box )

print(result)