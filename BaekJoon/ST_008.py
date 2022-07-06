
'''

 Backjoon _ exampels 4659

  "비밀번호 발음하기"   by Jinwoo Lee

  < algorithm >

  1. 주어진 조건 3개를 나누어서 구현하면 된다

    a) 모음(a,e,i,o,u) 하나를 반드시 포함

    b) 모음이 3개 or 자음이 3개 연속 금지

    c) 같은 글자 연속적으로 두번 오면 안되지만 ee , oo 허용


  2. 조건 구현은 a -> c -> b 순서로 한다.


   => eee의 경우 ee연속을 허용하지만, 모음이 3개 연속이기 때문에 not acceptable 해야 한다.

      ee일 경우 cnt를 줄여주는 방식으로 코딩했음으로  조건의 순서를 바꿔서 배치해야 문제에 알맞게 돌아간다



 

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