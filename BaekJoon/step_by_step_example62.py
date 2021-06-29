'''

 Backjoon _ exampels #

  "Baek 2212 - 센서 (Greedy)"   by Jinwoo Lee


 # Algorithm 

  0. 최대 k개의 집중국을 세우는데, n개의 센서가 적어도 하나의 집중국과 통신이 가능하면서 각 집중국의 수신영역거리합이 최소가 되도록 설계

  1. N개의 센서들을을 K개의 구간으로 나누는 문제가 된다 

     => 센서 위치 내림차순 정렬시 1,3,6,6,7,9 이며,

        센서 위치 차이를 구하면  2, 3, 0, 1, 2 이다.

        k개의 구역을 나눠야 함으로 k-1개 만큼의 구분선이 필요한데, 수신영역거리가 최소가 되어야 한다고 했음으로, 센서 거리차가 가장 큰값을 k-1만큼 지운다 


  2. 센서 위치를 오름차순 정렬 후 각 센서 위치간의 차이를 계산

  3. 센서 위치차이 배열에서 max_value를 k-1만큼 지운다 

  4. 센서 개수 (N) < 집중국개수(K) 일 경우 각 센서마다 설치하면 되니 수신영역거리 합은 0




'''
import heapq as hq 

num_sensor = int(input())

num_k = int(input())

pos = sorted(list(map(int,input().split())))


if num_k > num_sensor : print(0)

else:

    differ_pos = sorted([ abs(pos[idx] - pos[idx+1]) for idx in range(num_sensor-1) ], reverse=True)

    hq._heapify_max(differ_pos)

    while num_k-1 > 0:

        hq._heappop_max(differ_pos)

        num_k -=1

    print(sum(differ_pos))









