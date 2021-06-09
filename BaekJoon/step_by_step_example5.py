'''

 Backjoon _ exampels #

  "Baek - 2108 통계학"

 by Jinwoo Lee ( 2021/06/09 )



 # Attention for Implementation

  - 최빈수 : collections library의 Counter 사용

  - Counter가 적용된 결과값에 most_common() 함수를 사용하면 최빈수 순으로 정렬된다

  - (중요) Counter에 사용되는 list를 미리 한번 정렬하면 정렬된 순서대로 최빈수를 카운트 하기 떄문에 코드 처리가 용이함

  - import sys , sys.stdin.readline() 을 통해 입력에 받는 시간을 줄였음 -> 백준 시간초과 오류 


'''
import sys
from collections import Counter

def _counter(input_list):

    # 처음 정렬 시키는것이 매우 중요함 
    input_list = sorted(input_list)
  
    cnt_list = Counter(input_list).most_common()

    # 중복 case

    if len(cnt_list) > 1:

        if cnt_list[0][1] == cnt_list[1][1]:

            answer = cnt_list[1][0]

        else:
            answer = cnt_list[0][0]
    else:
        answer = cnt_list[0][0]

    return answer

test = int(input())

input_list = [int(sys.stdin.readline()) for _ in range(test)]


# avg
print(round(sum(input_list)/len(input_list)))

# middle
sorted_list = sorted(input_list)
print(sorted_list[int(len(sorted_list)/2)])

# counter
print(_counter(input_list))

# range
print(int(max(sorted_list) - min(sorted_list)))

