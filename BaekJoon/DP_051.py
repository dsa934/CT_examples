
'''

 Backjoon _ exampels 17202

  "�ڵ��� ��ȣ ����"   by Jinwoo Lee

  < algorithm >

  1. dp style�� ������ Ǯ���� ������

     => ��ȭ��ȣ�� ���� �Ѱ��� �ƴϱ� ���� ( ���� ����� ã�� �ʿ伺 ���� )
 

'''



def solution():

    number_1 = list(input())
    number_2 = list(input())


    candidate = [] 

    for idx in range(len(number_1)):


        candidate.extend(number_1[idx] + number_2[idx])

    while len(candidate) != 2 :

        ans = [] 
        
        for idx in range(len(candidate)-1):

             ans.extend( str((int(candidate[idx]) + int(candidate[idx+1]) ) % 10 ) )



        candidate = ans


    print("".join(candidate))


solution()