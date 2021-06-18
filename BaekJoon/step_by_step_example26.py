'''

 Backjoon _ exampels #

  "Baek 1449 - 수리공 항승 "

 by Jinwoo Lee ( 2021/06/xx )


 # Attention for Implementation

  * algorithm 

  1. 물이 새는 곳을 내림 차순 정렬, pivot = place_list[0] -0.5 로 시작 

  2. pivot + len_tape 보다 작은 place_list 요소들을 모두 소거

  3. 2번 과정 이후 place_list의 남아있는 첫번쨰 요소가 pivot이 됨 

  

'''


place, tape = list(map(int,input().split()))

place_list = list(map(int,input().split()))
place_list.sort()

# 여기를 처음에 0으로 시작해서 틀렸었음, 굳이 0이아니라 좌우 0.5만 있으면 된다.
pivot = place_list[0]-0.5

answer =0 

while place_list:

    if pivot + tape > place_list[0]:

        place_list.pop(0)

        if not place_list: answer+=1

    else:
        answer +=1

        pivot = place_list[0]

print(answer)





