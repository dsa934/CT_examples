'''

 Backjoon _ exampels #

  "Baek 2960 - 에라토스테네스의 체"(구현)   by Jinwoo Lee

'''

N, K = list(map(int,input().split()))

nums = [value for value in range(2,N+1)]


save = []

while nums:

    min_val = min(nums)

    stack = [] 

    for value in nums:

        if value % min_val != 0 : stack.append(value)

        else : save.append(value)

    nums = stack


print(save[K-1])
