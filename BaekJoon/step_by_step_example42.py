'''

 Backjoon _ exampels #

  "Baek 1759 - 암호만들기(문자열)"   by Jinwoo Lee


 # Algorithm 

  0. 모음이 최소 1개, 자음이 최소 2개가 들어가는 암호문을 만들어야 한다. 또한, 암호는 사전식 순서로 정렬이 되있을 것이다.

  1. itertools library를 통해 알파벳을 조합하여 사전순으로 정렬하고, 

  2. a,e,i,o,u가 최소 1개 포함되었는지 체크, 모음이 아닌것이 2개이상인지 체크 

  

 # Attention for Implementation

  - 모음이 2종류가 아니라 같은게 2개 있는 경우도 고려해야함 ex) aa

    => 자음의 수를 전체길이 - 모음개수로 처리했기 떄문


'''
from itertools import combinations

l, c = list(map(int,input().split()))

alpha = list(input().split())

password = list(combinations(sorted(alpha), l))

vowels = ['a','e','i','o','u']

result = []

for value in password:

    temp = ''.join(value)
    vowel_cnt = 0
    vowel_flag = False

    for vowel in vowels:

        if vowel in temp:

            vowel_cnt += temp.count(vowel)
            vowel_flag = True
    if vowel_flag and l - vowel_cnt >= 2: result.append(temp)

      

for value in result:
    print(value)
