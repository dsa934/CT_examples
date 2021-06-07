'''

 Backjoon _ exampels #

  "Baek :2941 - 크로아티아 알파벳 "

 by Jinwoo Lee ( 2021/06/07 )


 # Attention for Implementation

  - 문자열 치환을 통한 문자열 길이 구하기 

  - 'dz=', 'z='의 경우 후자가 전자에 포함됨으로 정렬을 통해 'dz='를 우선적으로 처리하게 해주어야 더 정확함



'''

croatia_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

sort_cro =[ value[1] for value in sorted([(len(value), value) for value in croatia_list], reverse=True, key = lambda x : x[0])]

str_input = input()

for alpha in sort_cro:

    str_input = str_input.replace(alpha, '*')

print(len(str_input))



