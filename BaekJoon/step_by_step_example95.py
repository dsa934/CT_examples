'''

 Backjoon _ exampels #

  "Baek 1758 - 알바생 강호 "(Greedy)   by Jinwoo Lee

'''

num_person = int(input())

total = 0

tips = [int(input()) for _ in range(num_person)]

for idx, value in enumerate(sorted(tips,reverse=True)):

    if value - idx >= 0 : total += value - idx

print(total)