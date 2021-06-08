'''

 Backjoon _ exampels #

  "Baek - 2798 블랙잭"

 by Jinwoo Lee ( 2021/06/08 )


 # Attention for Implementation

  - itertools의 combination을 이용하면 코드가 좀더 간 결해질수 있음


'''

from itertools import combinations

n, m = map(int,input().split())

card_list = list(map(int,input().split()))
com_list = list(combinations(card_list,3))
max_value = 0

for value in com_list:

    if sum(value) <= m and sum(value) > max_value:

        max_value = sum(value)

print(max_value)
        



