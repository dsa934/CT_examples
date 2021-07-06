'''

 Backjoon _ exampels #

  "Baek 11501 - 주식(Greedy)"   by Jinwoo Lee


 # Algorithm 

  0. 주식이 최대 이익이 되도록 하는 프로그램 작성 

  1. day별 주가가 주어지면 이를 뒤에서부터 하나씩 뺴서 계산하는 것이 핵심 알고리즘 

  2. if days =[ 2 1 1 5 2 3 4 ] , 뒤에서 부터 비교 

     cur_max = 4 :   total += (4-3) + (4-2) 

     cur_max = 5 :  total += (5-1) +(5-1) + (5-2)    => total : 14
     


 # Attention for Implementation

  1. 주식과 같은 시계열 데이터이면서 시간에 흐름이 중요한 경우 "뒤에서" 부터 뺴는 방법을 먼저 생각해보자.


'''

num_test = int(input())

result = []

while num_test != 0 :

    day = int(input())

    days = list(map(int,input().split()))

    total = 0

    max_val = 0

    for idx  in range(len(days)-1,-1,-1):

        if max_val < days[idx] : max_val = days[idx]

        elif max_val > days[idx] : total += max_val - days[idx]

        
    result.append(total)
    num_test -=1

for value in result:

    print(value)





