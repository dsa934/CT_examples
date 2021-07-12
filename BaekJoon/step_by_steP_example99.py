'''

 Backjoon _ exampels #

  "Baek 3986 - 좋은 단어 "(문자열)   by Jinwoo Lee


 # Algorithm 

  0. while문에서 stack[-1]과 value (= string.pop())값과 비교 

    -> 같으면 stack을 비우고, 다르면 stack에 value 추가 

    -> 최후에 stack이 비어 있으면 좋은단어, 아니면 해당없음 




 # Attention for Implementation

  1. ABBABB의 경우도 좋은단어에 속함 -> 0번 가정을 다듬어야 함 (기존엔 palindrome을 따로 계산)

  2. palindrom을 따로 계산했더니 시간초과 -> Algorithm 0만 구현해도 모든 케이스 커버 가능  -> 시간초과 => stack이 아닌 deque로 구현해서 해결 



 # 그렇다면 deque와 stack의 시간복잡도 차이는 ? 





'''
import sys
from collections import deque 

cnt = 0 

num_words = int(sys.stdin.readline())

for _ in range(num_words):

    string = list(sys.stdin.readline().rstrip())
    flag = False

    # puzzle game
    stack = deque()

    while string:

        value = string.pop()

        if not stack : stack.append(value)

        else:

            if stack[-1] == value : stack.pop()

            else : stack.append(value)

    if not stack : flag = True
    else : flag = False

    if flag : cnt +=1

print(cnt)
