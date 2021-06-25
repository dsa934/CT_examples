'''

 Backjoon _ exampels #

  "Baek 15903 - 카드합체놀이 (Greedy) "   by Jinwoo Lee


 # Algorithm 

  0. 카드합체 후 남은 카드들이 최소가 되도록 프로그래밍 

  1. x번 y번 카드 고르고, 그 합을 계산해서 x,y에 덮어쓴다 ( x ! = y  : 값은 같아도되는데 순서는 같으면안됨 1번과 1번 x)

  2. 횟수 m만큼  작은값 2개를 골라서 더하고 덮어씌움 



'''
import heapq as hq


n, m = list(map(int,input().split()))

nums = list(map(int,input().split()))


hq.heapify(nums)

pick = []

while m >0:

    m -= 1

    val1 = hq.heappop(nums)
    val2 = hq.heappop(nums)

    hq.heappush(nums, val1+val2)
    
    hq.heappush(nums, val1+val2)

    
    
print(sum(nums))




