
'''

 Backjoon _ exampels 1331

  "����Ʈ ����"   by Jinwoo Lee

  < algorithm >
 
   1. ����Ʈ�� ��θ� ��� candidate �� ���� �� bfs�� ���� �ùٸ� �̵� ������� üũ

   2. start = deque(candidate[0]) , target = candidate[1:]

     * ���̹� ���� �������� bfs�� Ȱ���Ͽ� ��θ� �����ϰ�, �ش� ��θ� �Ѱ��� ���÷��� �õ������� �־��µ�, 

       path = [ [5,3], [4,3] ... ] �̶�� [5,3], [4,3] �ϳ��� ���� bfs ó���� �Ϸ��� �ߴµ� �ѹ��� ��� ��ΰ� pop �Ǿ�����. ( ��ÿ��� �ð� �������� ������ ã�� ���ߴ�)

       deque ����� ���� deque ( [ ] ) ���¸� ���ϴµ� , �̹� list ������ path �����͸� deque ( [ [path] ]) �� ���� �ʱⰪ ������ �ؼ� ������ ������ ����� ���̴�.

       [] �� �ι� �������ν� 2���� �迭�� ����ǰ�, �迭�� �� ��ġ�� ��� ��θ� ������� ���·� �ڵ��� �Ǿ���ȴ� ���̴�.

       �������� ��������.

       ����, �� ���������� queue�� ������ǥ �Ѱ��� �ֱ� ������ �� ������� ��������, �� ������ Ǯ�ٰ� ���̹� ������ �� �ظ̴���

       �˰� �Ǿ ����Ѵ�


   3. bfs

     * ������ bfs���������� start point�� ���� �湮 ó���� ������, �� ������ �ٽ� �ǵ��ƿ;� �ϱ� ������ �湮ó���� ���� �ʴ´�

       => �̷� ���� ������ ��ǥ���� ���������� �ǵ��ƿ��°� ���� Ȯ���� �� �� �ִ�.


     * target = candidate[1:] 

       target.append(candidate[0])  

       => �ٽ� �ǵ��� ���°͵� Ȯ���ؾ� �ϱ� ������ target�� ���� ��ǥ�� �߰��� �־�� �Ѵ�


     * ���� while queue�� ���·� queue�� �􋚱����� bfs�� ��������, �� ��� target�� �ٶ����� ���� �ؾ� �Ѵ�

       => �־��� path�� 36������, ������ ��ġ���� ó����ġ�� ���� �� �� �ִ����� Ȯ���ؾ� �ϰ�, 
        
          �ڵ� ���� �� ������ ��ǥ������ ������ ������ queue�� �� ����ֱ� ������ ���� target�� ���� �����̴�


      

'''




from collections import deque

def bfs(candidate, eng2num, num2eng ):

    queue = deque([candidate[0]])

    target = deque(candidate[1:])

    # algorithm - 3
    target.append(candidate[0])

    row,col = 6,6

    visited = [ [False for _ in range(col+1)] for _ in range(row+1)]


    drow = [2, 2, -2, -2, 1, -1, 1, -1]
    dcol = [1, -1, 1, -1, 2, 2, -2, -2] 

    while target:

        flag = False

        _x, _y = queue.popleft()

        _x, _y  = eng2num[_x], int(_y)

        t_x, t_y = target.popleft()

        t_x, t_y = eng2num[t_x], int(t_y)

        for idx in range(8):

            n_x = _x + drow[idx]
            n_y = _y + dcol[idx]

            if n_x < 0 or n_y < 0 or n_x > row or n_y > col : continue 

            if not visited[n_x][n_y] :
            
                # algorithm - 3
                if t_x == n_x and t_y == n_y:
                    
                    queue.append([num2eng[n_x], n_y])
                    visited[n_x][n_y] = True

                    flag = True

                else:
                    continue


        if not flag : 
            return False

    return True



def solution():
    
  
    eng2num = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6}

    num2eng = {1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F'}


    candidate = [ input() for _ in range(36)] 
    

    if bfs(candidate, eng2num, num2eng) : print('Valid')
    else : print('Invalid')

    

solution()