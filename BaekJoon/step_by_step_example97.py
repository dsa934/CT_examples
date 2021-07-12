'''

 Backjoon _ exampels #

  "Baek 11508 - 2+1 세일 "(Greedy)   by Jinwoo Lee


 # Attention for Implementation

'''
import sys
input = sys.stdin.readline

num_item =int(input())

items = sorted([int(input()) for _ in range(num_item)],reverse=True)


stack = []

total = 0


while items:

    value = items.pop(0)
    stack.append(value)

    if len(stack) == 3 : 

        stack.pop()

        total += sum(stack)

        stack = []


    if len(items) == 0 and len(stack) != 3 :

        total +=sum(stack)



print(total)

