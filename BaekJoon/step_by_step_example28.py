'''

 Backjoon _ exampels #

  "Baek 2446 - 별찍기"   by Jinwoo Lee


 # Algorithm 

  0. 자리수 말고, 빈칸 + "*" 조합으로 출력하면 해결


'''

n = int(input())

for value in range(n):

    print(" "*value + "*" * (2*(n-value)-1))

for value in range(n-2,-1,-1):

    print(" "*value + "*" * (2*(n-value)-1))

