
'''

 Backjoon _ exampels 1837

  "��ȣ ����"   by Jinwoo Lee

  < algorithm >

  1. �Ҽ� �Ǻ� ��, �����佺�׳׽��� ü�� ����ϴ°��� TLE ���� ����

   => �׷��� �� ������ ��� K ���� ���� �Ҽ��� ���ϰ�, �ش� �Ҽ��� ������ �������� ��� BAD�� ����ϸ� �Ǳ� ������ ������ �� �� �Ĳ��ϰ� �д°��� �䱸 
 

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
