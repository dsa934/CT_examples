

'''

 Backjoon _ exampels 7569

  "Tomato"   by Jinwoo Lee

  < �˰��� >

  1. 2���� ��� �ִ� �Ÿ� ������ 3������ ���� 

     dx = [1, -1, 0, 0, 0 ,0]   �̵� ������ 6���� 
     dy = [0, 0, 1, -1, 0, 0]
     dz = [0, 0, 0, 0, 1, -1]



  2.  �ִܰŸ� ������ �����ϰ�, ���� �湮�� �丶�䰡 ���ϸ��� ������ value update �� queue�� �ش� �丶���� ��ǥ��  �߰� 


  3. visited�� Ȱ���� �ʿ�� ����, all_tomato_ripe �Լ��� ���� 

     a) queue ���� ���� �˻� -> ��� �丶�䰡 �̹� �;��ִ� ��� �Ǻ�

     b) queue ���� �˻� -> Ȥ�ö� ���� ���ϴ� �丶�䰡 �ִ� ��� �Ǻ�




  * ���� �õ� �ð� �ʰ� (TEL)  => �ذ� 
  
    queue = stack()   =>  queue = deque() 
    queue.pop(0)      => queue.popleft()   


    => Reason ���� 

    1. �Ϲ�������, pop() ������ O(1) �ð��� �ɸ�����, 
    
       pop(0)�� ��� :  O(1) + O(N-1) =  O(N) 
       
       why ?  idx 0 ��ġ�� data ���� ��,   ���� �ִ� n-1 ���� data�� ���ڸ��� �޲ٱ����� ������� ������ O(N-1) �� �ð��� �߰��� �ɸ��� �ȴ� 
       
       
    2. deque()�� popleft() ������ ��� O(1)�̴� 

      => doubled linked list�� ������������, deque�� ũ�Ⱑ �󸶳� ũ���� ���� ���� ���길 �Ͼ�� ������ o(1)�� ������ constant time�̴�.



 

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