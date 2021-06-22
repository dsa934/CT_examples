'''

 Backjoon _ exampels #

  "Baek 11000 - 강의실 배정(Greedy) "   by Jinwoo Lee


 # Algorithm 

  0. 모든 수강신청을 소화하기 위한 최소한의 강의실 수 

  1. 강의가 동시에 진행될수가 있기 떄문에 stack을 활용

  2. stack에 강의가 들어갈떄만 cnt+= 1

  3. stack에 강의를 넣는 조건은 강의 i,j에 대하여  s_j가 T_i보다 큰 경우 stack에 들어간다.

  4. stack에 들어있는 강의들은 끝나는시간을 기준으로 내림차순 정렬한다 

  5. stack에 들어있는 강의 k와 들으려는 강의 t에 대하여 T_k <= S_t 일 경우 강의 k를 stack에서 제거 


 # Attention for Implementation

  - 시간초과 발생 -> 우선순위 큐와 sys.stdin.readline()을 사용해보자 

  - 끝나는시간만 stack에 넣자 => min_heap에서 꺼낼떄 끝나는시간 기준으로 생각해야함 

    => 시작시간은 이미 stack에 넣는 행위를 할때 고려가 되었음 


'''
import sys 
import heapq as hq

num = int(sys.stdin.readline())

lecture = [list(map(int,sys.stdin.readline().split())) for _ in range(num)]

stack = [] 
cnt = 0


hq.heapify(lecture)
hq.heapify(stack)

while lecture :

    lec = hq.heappop(lecture)
    if not stack : 

        # 첫강의 endtime을 넣어줌
        hq.heappush(stack, lec[1])
        cnt+=1

    else:
        # 다음 강의의 시작시간이 듣고있는 강의의 끝시간보다 크거나 같을떄

        tmp = hq.heappop(stack)

        if tmp <= lec[0]: 
                       
            hq.heappush(stack, lec[1])
            
        else:
            hq.heappush(stack,tmp)
            hq.heappush(stack, lec[1])
            
            cnt+=1

    

print(cnt)



