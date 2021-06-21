'''

 Backjoon _ exampels #

  "Baek 11050 - 이항계수"   by Jinwoo Lee


 # Algorithm 

  - binomial coefficient 
 
    => n! / r!(n-r)!


'''

n, k = list(map(int,input().split()))

total =1
divide = 1

for value in range(n,k,-1):

    total*= value

for value in range(1, (n-k)+1):

    divide *= value

print(int(total/divide))