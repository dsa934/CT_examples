'''

 Backjoon _ exampels #

  "Baek 1202 - 보석 도둑 "

 by Jinwoo Lee ( 2021/06/18 )


 # Attention for Implementation

  * Algorithm

   1. 보석, 가방 모두 내림차순 정렬하여 가장 적은무게의 보석과 가장 작은 가방부터 비교하는것이 포인트

   2. bags = [2,3,4,5] 일떄 

      2-1. jewel = [ [1,50], [2,40], [3,30] , [4,90] ] 라면 2(50), 3(40), 4(90), 5(30) => 210

           
           * 가장 작은 가방인 2번 가방에 들어갈 수있는 보석은 [1,50], [2,40] 인데 [1,50]이 선택 되었음으로 [2,40]은 다시 jew_list에서 넣어줘야 하는데

             다른 풀이 코드들은 이부분이 없는데 어떻게 가능한건지 이해가 안됬음 



           => 가방안에 들어 갈 수있는 보석 list : temp 

              case bags = 2 : temp = [ [1,50] ,[2,40] ] , [1,50] pick 

              case bags = 3 : temp = [ [2,40] , [3,30] ] , [2,40] pick

              => 즉, 가방 2에서 비교한 temp값을 다시 돌려줄 필요 없이, 새로운 가방에 대하여 temp에 추가할 보석이 있는지 없는지만 체크한 후

                 len(temp) == 0이 될때까지 보석의 값어치를 더하면 풀리는 문제 




'''

import sys, heapq

num_jew, num_bag = list(map(int,sys.stdin.readline().split()))

jew_list = sorted([list(map(int,sys.stdin.readline().split())) for _ in range(num_jew)], key= lambda x : x[0])
bag_list = sorted([list(map(int,sys.stdin.readline().split())) for _ in range(num_bag)])


total = 0 
tmp = []

for bag in bag_list:
   
    # 가방에 들어가는 보석 뽑기
    while jew_list and bag[0] >=jew_list[0][0]:

        weight, value = heapq.heappop(jew_list)

        # 우선순위큐는 기본적으로 min_heap 구조
        # -value를 취하고 heapop을 하면 결과적으로 max_heap 구조로 활용가능 
        heapq.heappush(tmp, -value)


    if tmp: total += heapq.heappop(tmp)

    elif not jew_list : break


print(abs(total))
