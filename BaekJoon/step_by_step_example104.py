'''

 Backjoon _ exampels #

  "Baek 1003 - 피보나치 함수"(DP)   by Jinwoo Lee


 # Algorithm 

  0. 피보나치 수(num)에 대하여 0,1의 호출 개수를 각각 나열하면 0,1의 개수 또한 피보나치 수열의 성질을 갖는것을 알 수 있다.

 # Attention for Implementation


'''


num_test = int(input())

zero = [1,0,1]
one = [0,1,1]

tmp = [0 for _ in range(40)]

zero.extend(tmp)
one.extend(tmp)

for _ in range(num_test):

    num = int(input())

    if num > 2 : 

        for idx in range(3,num+1):

            zero[idx] = zero[idx-2] + zero[idx-1]
            one[idx] = one[idx-2] + one[idx-1]

    print( zero[num], one[num])


        
