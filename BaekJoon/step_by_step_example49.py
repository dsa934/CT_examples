'''

 Backjoon _ exampels #

  "Baek 1764 - 듣보잡(문자열) "   by Jinwoo Lee


 # Algorithm 

  0. 2개의 리스트에 대해서 서로 공통속성인 요소를 찾자

  1. 처음엔 for문으로 했으나 hear,see이 500,000 까지이기 떄문에 이 경우 시간초과 

  2. 집합을 활용  (집합 s1,s2에 대해)

     교집합 : s1 & s2
     차집합 : s1 - s2
     합집합 : s1 | s2

  
'''


hear, see = list(map(int,input().split()))

hear_list = [input() for _ in range(hear)]

see_list = [input() for _ in range(see)]


result = set(see_list) & set(hear_list)

print(len(result))
for value in sorted(result):
    print(value)