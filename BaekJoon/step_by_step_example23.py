'''

 Backjoon _ exampels #

  "Baek 1439 - 뒤집기"

 by Jinwoo Lee ( 2021/06/17 )


 # Attention for Implementation

  - 0,1 중에 중복되는 수를 1개만 남기고 지운다  ex) 00011000  -> 010 
 
  - 이 후 0과 1의 개수를 카운팅하여 적은 수만큼 뒤집어주면 해결 -> 스택 활용



'''

words = input()

stack = [words[0]]

for idx in range(1,len(words)):

    if words[idx] != stack[-1]:

        stack.append(words[idx])

print(min(stack.count('0'), stack.count('1')))



