'''

 Backjoon _ exampels #

  "Baek 7785 - 회사에 있는 사람(문자열)"   by Jinwoo Lee


 # Algorithm 

  0. dictionary 타입을 이용하여 손쉽게 처리 


'''

num_person = int(input())

entry_log = {}

for _ in range(num_person):

    name, status = input().split()

    entry_log[name] = status



result = [value[0] for value in entry_log.items() if value[1] == 'enter' ]

for value in sorted(result, reverse=True):
    print(value)


