'''

 Backjoon _ exampels #

  "Baek 2563 - 색종이"(Implementation)   by Jinwoo Lee


 # Algorithm 

 1. 전체 종이칸에서 색종이로 덮어지는 영역의 수를 구하는 방식으로 코딩 

  
 # Attention for Implementation

 1. 일일히 겹치는 구간을 계산하면 중복으로 겹치는 구간에 대해서 2번 이상 뺴주게 되는 문제가 발생한다



'''
num_test = int(input())

areas = [[0 for x in range(101)] for y in range(101)]

for _ in range(num_test):

    x, y = map(int,input().split())

    
    for row in range(x, x+10):

        for col in range(y, y+10):

            areas[row][col] = 1

total = 0

for row in areas:

    total += row.count(1)

print(total)


