'''

 Backjoon _ exampels #

  "Baek 2847 - 게임을 만든 동준이 "   by Jinwoo Lee


 # Algorithm 

  0. 레벨별 클리어 점수가 잘못되었음 (높은것이 낮은점수) 이를 해결하기 위해 낮은 스테이지의 클리어 점수 감소 

  1. 점수를 내리는 방법밖에 없음으로 뒤에서부터 비교하며 진행하기 


 # Attention for Implementation



'''


nums = int(input())

level = [int(input()) for _ in range(nums)]

total = 0 

for idx in range(nums-1, 0, -1):
    
    while True:

        if level[idx] > level[idx-1] : break

        elif level[idx] <= level[idx-1] :

            level[idx-1] -=1

            total+=1

print(total)




