'''

 Backjoon _ exampels #

  "Baek - 18870 좌표 압축"

 by Jinwoo Lee ( 2021/06/14 )


 # Attention for Implementation

  - 문제가 이해가 안됬음 => 주어진 좌표의 순서를 오름차순 정렬

  - dict을 사용하여 index로 접근하기 때문에 O(1)의 접근이 가능

  - N의 범위가 1,000,000, 시간제한 2초 이기 때문에 최대한 선형시간에 가깝게 설계해야 할 필요성이 있음 


'''

tc = int(input())

data = list(map(int,input().split()))

# value : idx => -10 : 0, -9 : 1 ...
order_list = {value : idx for idx, value in enumerate(sorted(set(data)))}


for value in data:

    print(order_list[value], end=' ')