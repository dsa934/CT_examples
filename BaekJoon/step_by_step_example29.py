'''

 Backjoon _ exampels #

  "Baek 2747 - 피보나치의 수 "   by Jinwoo Lee


 # Algorithm 

  0. DP를 이용하여 fibo구현 


'''

n = int(input())

fibo = [0]*46
fibo[0] = 1
fibo[1] = 1

for value in range(3,n+1):

    fibo[value-1] = fibo[value-2] +fibo[value-3]

print(fibo[n-1])