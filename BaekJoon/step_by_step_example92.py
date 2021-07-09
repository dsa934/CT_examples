'''

 Backjoon _ exampels #

  "Baek 9009 - 피보나치" (Greedy + Math)  by Jinwoo Lee


 # Algorithm 

  0. 주어진 입력에 대하여 최소의 피보나치 조합으로 표현하기 

  1. 주어진 입력 이하일떄 까지(while) 피보나치 식을 통해 DP의 형태로 list 각 위치에 피보나치 수를 저장 ( 재귀사용x)

  2. list_value + total <= input() 인 list_value를 찾아 오름차순 정렬 -> 출력 


 # Attention for Implementation

  1. 1만이 넘어가는 수가 피보나치 조합으로 나타내면 생각보다 오래걸리지 않는다.
  
  

'''

def fibo(number):
    
    stack = [0,1]

    while stack[-1] <= number:

        
        stack.append(stack[-1] + stack[-2])

    return stack
            


num_test = int(input())

for _ in range(num_test):

    num = int(input())
    total = 0 
    stack = sorted(fibo(num),reverse=True)

    result = []

    for value in stack:

        if value + total <= num: 
            total += value
            result.append(value)

    sort_result = sorted(result)[1:]
    for idx,value in enumerate(sort_result):
        print(value, end=' ')

        if idx == len(sort_result)-1 : print()




