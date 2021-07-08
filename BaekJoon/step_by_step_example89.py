'''

 Backjoon _ exampels #

  "Baek 9237 - 이장님의 초대 "(Greedy)   by Jinwoo Lee


 # Algorithm 

  0. 나무가 자라는데 걸리는 시간 list를 내림차순 정렬 ( 오래걸릴수록 빨리 심어야함)

  1. 나무 심기 (+1), 나무가 완전히 자란 후 ( +1) 

  2. 나무가 자라는데 걸리는시간 + 몇번쨰에 심었는지 + 나무심기 + 나무완전자라기  

     => days[idx] + idx + 1 + 1 의 값이 가장큰 경우를 찾아 출력 

  

'''

num_tree = int(input())

days = sorted(list(map(int,input().split())),reverse=True)

max_value = 0

for idx in range(len(days)):

    if days[idx] +1 +1 + idx >= max_value : max_value = days[idx]+1 +1 + idx


print(max_value)