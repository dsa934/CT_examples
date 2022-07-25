
'''

 Backjoon _ exampels 1837

  "암호 제작"   by Jinwoo Lee

  < algorithm >

  1. 소수 판별 시, 에라토스테네스의 체를 사용하는것이 TLE 방지 가능

   => 그러나 이 문제의 경우 K 보다 작은 소수를 구하고, 해당 소수로 나누어 떨어지는 경우 BAD를 출력하면 되기 떄문에 문제를 좀 더 꼼꼼하게 읽는것이 요구 
 

'''


def eratos(number,k):

    eratos_table = [False, False ] + [ True for _ in range(2, k)]

    prime = [] 

    for idx in range(2, k):

        if eratos_table[idx] :

            prime.append(idx)

            for cmp_idx in range(idx+idx, k, idx):

                eratos_table[cmp_idx] = False
                
    for value in prime:

        if number % value == 0 :
            
            return False, min(number//value, value)

    return True, None
    

def solution():
    
    number, k = map(int, input().split())

    flag, alpha = eratos(number, k)

    if flag : print("GOOD")

    else:

        print('BAD', alpha )


solution()
