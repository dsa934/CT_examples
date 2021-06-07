'''

 Backjoon _ exampels #

  "Baek :1316 - 그룹 단어 체커"

 by Jinwoo Lee ( 2021/06/xx )


 # Attention for Implementation

  - c++ 습관처럼 일일히 조건에 맞는 개수를 카운트하려고 하지말기

  - python style 이용 ( in, slicing )


'''

tc = int(input())
answer =0

for _ in range(tc):

    g_word = input()

    for idx in range(len(g_word)):

        if idx != len(g_word)-1:


            if g_word[idx] == g_word[idx+1]:
                pass

            elif g_word[idx] in g_word[idx+1:]:
                break
        else:
            answer+=1

print(answer)


