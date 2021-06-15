'''

 Backjoon _ exampels #

  "Baek 1715 - 카드 정렬하기 "

 by Jinwoo Lee ( 2021/06/xx )


 # Attention for Implementation

  - 문제는 간단, 시간초과 해결문제 

    => list 구축, remove 함수 모두 O(N)임 

  - 우선순위 큐를 사용 

    => 최소,최대값을 계속해서 호출할떄 자주 사용하는 자료구조 

    => O(logN) base= 2 

    

'''
import sys 
import heapq as hq

num_card = int(sys.stdin.readline())

cards = [] 
total =0 

for _ in range(num_card):

    hq.heappush(cards, int(sys.stdin.readline()))


while len(cards)>1:

    first = hq.heappop(cards)
    second = hq.heappop(cards)

    total += first +second
    hq.heappush(cards, first+second)

print(total)
