'''

 Backjoon _ exampels 1667

  "숨박꼭질"   by Jinwoo Lee


  문제 설명 : Start -> End 까지의 최단 경로를 구하는 문제로 이동 방향은 dx = [ -1, +1, x2 ] 로 제한 

  1. 최단 경로 문제라서 bfs 알고리즘 활용

  2. 핵심 아이디어 

     * [좌표값, 해당 좌표일떄의 cost] 값으로 queue를 활용

     * visited를 기존의 [] 형태가 아닌 set()을 사용해야 중복이 사라짐 

       => 이미 방문한 값이라면 그 값을 계산하기 위한 최적값이 따로 존재함 

          왜냐 ?  이미 방문한 값이라면 해당 값에 도달하기 위한 최적값은 이미 달성 되있다고 생각할 수 있음 


     * 이 문제에서 범위 ( 0<= pos <= 100000 )을 제한하지 않으면 시간 초과가 걸림 

       1.  pos >= 0       ,    음수 일 경우 *2 떄문에 계산할 필요 없는 더미값이 늘어 날 수 있음 

       2.  pos <= 100000  ,   

          만약 100000에 도달해야 하는 값에 대해서 생각해보면

          a) 50001 x2 -1 -1 

          b) 50001 -1 x2 

          a) 보다 b)의 계산 결과가 더 빠름 




'''

def bfs(start, end):
    
    queue = []
    visited = set()

    max_value = 100000

    cost = 0

    dx = [ -1, 1 , 2 ]

    queue.append([start,cost])

    visited.add(start)
    

    while queue:

        _pos, _cost = queue.pop(0)

        if _pos == end :

            return _cost

        
        for idx in range(3):



            if idx == 2 : 

                n_pos = _pos * dx[idx]


            else:

                n_pos = _pos + dx[idx]



            if n_pos not in visited and n_pos <= max_value and n_pos >= 0 :

                visited.add(n_pos)

                n_cost = _cost + 1

                queue.append([n_pos, n_cost])
        



start, end = list(map(int, input().split()))

print( bfs(start, end) )