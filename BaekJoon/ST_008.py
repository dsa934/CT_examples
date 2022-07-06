
'''

 Backjoon _ exampels 4659

  "��й�ȣ �����ϱ�"   by Jinwoo Lee

  < algorithm >

  1. �־��� ���� 3���� ����� �����ϸ� �ȴ�

    a) ����(a,e,i,o,u) �ϳ��� �ݵ�� ����

    b) ������ 3�� or ������ 3�� ���� ����

    c) ���� ���� ���������� �ι� ���� �ȵ����� ee , oo ���


  2. ���� ������ a -> c -> b ������ �Ѵ�.


   => eee�� ��� ee������ ���������, ������ 3�� �����̱� ������ not acceptable �ؾ� �Ѵ�.

      ee�� ��� cnt�� �ٿ��ִ� ������� �ڵ���������  ������ ������ �ٲ㼭 ��ġ�ؾ� ������ �˸°� ���ư���



 

'''




def condition_1(string, vowel):
    
    
    for value in vowel:

        if value in string:

            return True

    return False

def condition_2(string, vowel):

    v_cnt, nv_cnt = 0, 0

    for idx in range(len(string)):

        if string[idx] in vowel:

            v_cnt +=1
            nv_cnt =0

        else:
            nv_cnt +=1
            v_cnt = 0

        if v_cnt == 2 and string[idx] == string[idx-1] :

            if string[idx] == 'e' or string[idx] == 'o': 

                v_cnt -= 1
                
            else:
                return False

        if nv_cnt == 2 and string[idx] == string[idx-1] : return False


    return True

def condition_3(string, vowel):

    v_cnt, nv_cnt = 0, 0

    for idx in range(len(string)):

        if string[idx] in vowel:

            v_cnt +=1
            nv_cnt =0

        else:
            nv_cnt +=1
            v_cnt = 0

        if v_cnt == 3 or nv_cnt == 3 : 
            return False


    return True

def chk(string):
    
    vowel = ['a', 'e', 'i', 'o', 'u']


    flag_1 = condition_1(string, vowel)
    
    flag_2 = condition_2(string, vowel)

    flag_3 = condition_3(string, vowel)

    
    if False in [flag_1, flag_2, flag_3]: return False

    else: return True



def solution():
    
    while True:

        string = input()

        if string == 'end': break

        else:

            if chk(string) : print(f'<{string}> is acceptable.')
            else: print(f'<{string}> is not acceptable.')






solution()