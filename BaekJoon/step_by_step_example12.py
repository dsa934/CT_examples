'''

 Backjoon _ exampels #

  "10989 - 수 정렬하기 3"

 by Jinwoo Lee ( 2021/06/xx )


 # Attention for Implementation

  - 제한시간 3초 , 메모리 제한 8MB

  - input()을 sys library 의 stdin으로 받는것 

  - 미리 list의 크기를 정해놓고 시작하는것이 포인트 



'''
import sys

N = int(sys.stdin.readline())

result = [0 for _ in range(10001)]

for i in range(N):
    num = int(sys.stdin.readline())
    result[num] += 1
    
for i in range(len(result)):
    for j in range(result[i]):
        print(i)