'''

 Backjoon _ exampels #

  "Baek 11497 - 통나뮤 건너뛰기(Greedy) "   by Jinwoo Lee


 # Algorithm 

  0. 인접 통나무의 높이차가 최소가 되도록 하는 프로그래밍 

  1. 입력받은 trees에서 가장 큰값을 중심에 두고, 큰값들을 좌우로 배치하기 

    => [2,4,5,7,9]  -> [ 9]  -> [ 5, 9, 7]  -> [ 2, 5, 9, 7, 4] 


  2. 1에서 얻은 list의 각요소별 차이를 계산하여 가장 큰값을 result에 추가

    => 1번에서 얻은 배열은 각 인접 통나무의 높이차가 최소가 됨을 보장함 (이문제에선)



 # Attention for Implementation

  - 첫시도에 시간초과 판정을 받았는데     hq._heapify_max(trees[idx]) 부분을 

    while문 안에 집어넣어서 그런 실수가 발생했음 
 



'''

import heapq as hq
import sys

tc = int(sys.stdin.readline())

nums = []
trees = []

for _ in range(tc):

    nums.append(int(sys.stdin.readline()))
    trees.append(list(map(int,sys.stdin.readline().split())))

result = []


for idx in range(tc):

    tmp = [] 
    flag = True

    hq._heapify_max(trees[idx])

    # 1번에 의한 배치 
    while True:
        if len(trees[idx]) == 0 : break


        val = hq._heappop_max(trees[idx])

        if not tmp : tmp.append(val)

        else:

            if flag : 
                tmp.insert(0,val)
                flag = False

            else :
                tmp.append(val)
                flag = True


    max_value = 0

    for idx in range(len(tmp)-1):

        if max_value < abs(tmp[idx] - tmp[idx+1]) : max_value = abs(tmp[idx] - tmp[idx+1])



    result.append(max_value)

for value in result:
    print(value)
    



