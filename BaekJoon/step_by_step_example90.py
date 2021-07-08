'''

 Backjoon _ exampels #

  "Baek 17609 - 회문 "(Greedy)   by Jinwoo Lee


 # Algorithm 

  0. 시간초과(substring), 메모리초과(itertools - combinations) 문제로 인해 다른 방법을 고안

  1. 문자열의 끝과 처음부분을 비교해 나가는 방식으로 처리 



 # Attention for Implementation



'''

def pseudo(start, end,string):

    while start < end:

        if string[start] == string[end] :

            start +=1
            end -=1


        else: 

            return False

    return True


def pelindrome(start, end, string ):

    while start < end :

        if string[start] == string[end]:

            start +=1
            end -=1

        else:

            if pseudo(start+1, end, string) or pseudo(start, end-1, string) : 

                return 1

            else:
                return 2

    return 0



num_test = int(input())

result = []


for _ in range(num_test):

    string = input()

    result.append(pelindrome(0, len(string)-1, string))

for value in result:
    print(value)

'''
import sys
from itertools import combinations

num_test = int(sys.stdin.readline())

for _ in range(num_test):

    string = sys.stdin.readline().rstrip()

    # palindrome
    if string == string[::-1] : 
        print(0)
        continue

    else:
        combination = list(combinations(list(string), len(string)-1))
        flag = False

        for value in combination:

            if ''.join(value) == ''.join(value[::-1]) : 
                print(1)
                flag = True
                break


        if not flag : print(2)
        
========================= < 메모리 초과>


import sys 

num_test = int(sys.stdin.readline())

result = []

for _ in range(num_test):

    string = sys.stdin.readline().rstrip()

    # palindrome
    if string == string[::-1] :
        result.append(0)
        continue

    else:
        flag = False

        for idx in range(len(string)):

            sub_string = string[:idx] + string[idx+1:]

            if sub_string == sub_string[::-1] :
                result.append(1)
                flag = True
                break

        if not flag : result.append(2)

for value in result:
    print(value)
======================== <시간 초과>

'''
