'''

 Backjoon _ exampels #

  "1181 - 단어정렬"

 by Jinwoo Lee ( 2021/06/07 )


 # Problem

  - 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

   1. 길이가 짧은 것부터
   2. 길이가 같으면 사전 순으로


 # Attention for Implementation

  - 사전 정렬은 <, > 로 가능

  - 첫 코드 작성시 시간초과 -> 시간제한 2초, n <= 20000 

    => 지수시간 미만으로 코드를 구현해야 함 


  - 문자열 정렬에서 sorted(data(문자열 길이, 문자열))와 같이 내장함수를 사용할 경우

    첫번쨰 인자인 문자열 길이로 정렬 후 두번쨰 인자인 문자열을 사전순으로 정렬한다. 

    즉, sort 되는 데이터가 갖는 속성에 대하여 모두 정렬해주는것을 기억하기 


'''

test_case = int(input())

str_list = [] 

for _ in range(test_case):

    str_list.append(input())


result = []

str_list = set(str_list)


for value in str_list:

    result.append([len(value), value])


sorted_result = sorted(result)

for idx, value in sorted_result:

    print(value)    



