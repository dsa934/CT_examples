'''

 Backjoon _ exampels #

  "Baek 1059 - 좋은 구간 (BF)"   by Jinwoo Lee


 # Algorithm 

  0. 집합 S와 정수 N이 주어졌을떄 S에 속하지 않으면서 N을 갖는 구간의 개수를 구하라 

  1. 집합 S에서 N에 가장 가까운 min,max값을 각각 구하여 전체 범위를 구함 min <= n <= max 

      1-1. N으로 시작하는 구간 :  N ~ max

      1-2. N으로 끝나는 구간 : min ~ N

      1-3.  N이 중간에 속해 있는 구간 :  (N-min) * (max-N)


  2. N이 집합 s의 최소값보다 작을 수가 있다는 점을 고려하기 

     집합s보다 N이 큰 경우는 문제에서 제한조건에 위배되기 떄문에 고려하지 않아도 된다.


 # Attention for Implementation

  1. max, min 값이 비어있는 경우도 고려해야함

  2.(반례) 제한 조건에서 N <= max(S) 이지만,  위에서 구한 min <= n <= max가   n<= min <= max 일수도 있음 

    =>  2 
        3  7        => [1,2]  => answer : 1 
        2 

       
'''

nums = int(input())

s_list = sorted(list(map(int,input().split())))

N = int(input())
total = 0 

if N in s_list : print(total)

else:
    # 반례 2 
    if N < min(s_list) : min_value = 1 

    else:
    
        # 작은값들중 n에 가장 근접한 값을 구하기 위해 마지막에 Max
        min_value = [ value for value in s_list if value < N]

        if min_value : 
            min_value = max(min_value) +1

        else: min_value = 0

    max_value = [ value for value in sorted(s_list,reverse=True) if value > N]

    if max_value :
        max_value = min(max_value) -1

    else: max_value =0 


    if min_value != 0 and max_value != 0 : 

        # case 1
        total += max_value - N

        # case 2
        total += N - min_value

        # case 3
        total += (max_value -N) * (N - min_value)

    elif min_value == 0: total += max_value - N

    elif max_value == 0 : total += N - min_value 


    print(total)
