
'''

 Backjoon _ exampels 1331

  "나이트 투어"   by Jinwoo Lee

  < algorithm >
 
   1. 나이트의 경로를 모두 candidate 에 저장 후 bfs를 통해 올바른 이동 경로인지 체크

   2. start = deque(candidate[0]) , target = candidate[1:]

     * 네이버 코테 문제에서 bfs를 활용하여 경로를 저장하고, 해당 경로를 한개씩 뺴올려고 시도한적이 있었는데, 

       path = [ [5,3], [4,3] ... ] 이라면 [5,3], [4,3] 하나씩 뺴서 bfs 처리를 하려고 했는데 한번에 모든 경로가 pop 되었었다. ( 당시에는 시간 부족으로 이유를 찾지 못했다)

       deque 선언시 보통 deque ( [ ] ) 형태를 취하는데 , 이미 list 형태인 path 데이터를 deque ( [ [path] ]) 와 같이 초기값 설정을 해서 차원의 문제가 생겼던 것이다.

       [] 을 두번 취함으로써 2차원 배열이 선언되고, 배열의 한 위치에 모든 경로를 집어넣은 형태로 코딩이 되어버렸던 것이다.

       다음부턴 주의하자.

       물론, 이 문제에서는 queue에 시작좌표 한개만 넣기 떄문에 위 내용과는 별개지만, 이 문제를 풀다가 네이버 문제를 왜 해맸는지

       알게 되어서 기록한다


   3. bfs

     * 보통의 bfs문제에서는 start point에 대해 방문 처리를 하지만, 이 문제는 다시 되돌아와야 하기 때문에 방문처리를 하지 않는다

       => 이로 인해 마지막 좌표에서 시작점으로 되돌아오는것 까지 확인을 할 수 있다.


     * target = candidate[1:] 

       target.append(candidate[0])  

       => 다시 되돌아 오는것도 확인해야 하기 때문에 target에 시작 좌표를 추가해 주어야 한다


     * 보통 while queue의 형태로 queue가 빌떄까지만 bfs를 돌리지만, 이 경우 target이 다떨어질 경우로 해야 한다

       => 주어진 path는 36개지만, 마지막 위치에서 처음위치로 돌아 올 수 있는지를 확인해야 하고, 
        
          코딩 설계 상 마지막 좌표에서도 조건이 맞으면 queue에 또 집어넣기 떄문에 비교할 target이 없기 떄문이다


      

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