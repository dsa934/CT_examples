'''

 Backjoon _ exampels #

  "11650 - 좌표 정렬하기 "

 by Jinwoo Lee ( 2021/06/07 )



'''


test_case = int(input())

str_list = [] 

for _ in range(test_case):

    str_list.append(list(map(int,input().split())))


sorted_list = sorted(str_list)

for value1, value2 in sorted_list:

    print(value1, value2)


