'''

 Backjoon _ exampels #

  " Baek - 1946 "

 by Jinwoo Lee ( 2021/06/14 )


 # Attention for Implementation

  - 실행속도 : sys.stdin.readline > raw_input > input()   / readline, readlines 구별

    -> 시간초과 오류뜨면 sys 사용

    -> readlines 하면 계속입력받기 떄문에 line 


  - 신입사원 뽑기 방식이 서류,면접 점수 중 하나라도 다른 지원자보다 높아야 뽑는다

    -> 서류로 오름차순 정렬하여 면접 점수끼리만 비교를 하면

    -> 최초 min_value(서류 심사1등)의 면접 등수보다 높은 애들만 뽑음 (이걸 문제에서 이해하는게 핵심)

    => 처음에 틀린 이유 : 서류순으로 정렬해놓고 면접에서 또 일일히 비교를 하려고 시도 -> 기존 서류 점수로 정렬한 내용을 무시해버림 

'''


import sys

tc = int(sys.stdin.readline())

result = []
for _ in range(tc):

    num_user = int(sys.stdin.readline())

    # sys 사용하여 입력받을땐 list형태로 만들어줘야 오류가 발생하지 않는다
    user_list = sorted([list(map(int,sys.stdin.readline().split())) for _ in range(num_user)], key = lambda x :x[0]) 

    cnt = 1
    min_value = user_list[0][1]

    
    for value in user_list:

        if value[1] < min_value :

            min_value = value[1]
            cnt+=1

    result.append(cnt)

for value in result:
    print(value)

