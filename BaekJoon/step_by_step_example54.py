'''

 Backjoon _ exampels #

  "Baek 1182 - 부분수열의 합(BF)"   by Jinwoo Lee


 # Algorithm 

  0. score를 만족하는 부분수열의 개수를 구하라 

  1. itertools의 combination을 사용하여 모든 조합을 구하고 score에 맞는 조합이 있는지 체크 


'''

from itertools import combinations

num, score = list(map(int,input().split()))


nums = list(map(int,input().split()))


candidate = [list(combinations(nums, idx)) for idx in range(1,num+1)]

cnt = 0

for cluster in candidate:

    for value in cluster:

        if sum(value) == score : cnt+=1

print(cnt)