'''

 Backjoon _ exampels #

  "Baek - 회의실 배정"

 by Jinwoo Lee ( 2021/06/010 )

 # Attention for Implementation

  - 회의의 개수가 최대가 되려면 ? 

     => 끝나는 시간으로 정렬 후 시작시간으로 다시 정렬을 하면 greedy 하게 풀이할 수 있음 


  - (중요) Python sort에 대한 정리 

    - data = [ [2,4] , [1,2], [4,3], [4,4] ] 로 이루어진 데이터에 대하여 정렬을 할 떄

      일반적 용법(i번쨰 idx 기준 정렬) : sorted(data, key = lambda x :x[i] )  

      
      * sorted(data, key = lambda x: ( x[i], x[j] ) )  

        - 이 경우 i번쨰 idx 기준으로 정렬된 list값을 유지한 상태로 j번쨰 idx 기준을 가지고 list를 한번 더 정렬함 

          => [ [1,2] , [4,3], [2,4] , [4,4] ]  즉, 동시에 정렬하는 개념 


        - i번 기준 정렬 이후 다시 j번 기준 정렬 하는 경우와 다름 이때는 마지막에 한 정렬 기준으로 list가 정렬이 됨 



'''

test = int(input())

# lambda x : ( ... ) or lambda x : [ ... ]  => (), [] 형태는 데이터 type에 맞춤, 보통 tuple이 메모리면에서 덜 소비됨
time = sorted( [tuple(map(int,input().split())) for _ in range(test)], key = lambda x :(x[1], x[0]))

answer = 0

for idx in range(len(time)) :

    if idx == 0:

        chk = time[idx]
        answer +=1

    elif chk[1] <= time[idx][0] :

        answer +=1

        chk = time[idx]

print(answer)


