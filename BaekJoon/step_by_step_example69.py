'''

 Backjoon _ exampels #

  "Baek 4446 - ROT13 ( Silver ver.) (문자열)"   by Jinwoo Lee


 # Algorithm 

  0. 정해진 자음, 모음 집합에서 각각 +10, +3 위치에 있는 문자로 치환 

  1. 대소문자는 유지, 기존 ROT13과 같음 (알파벳만 변환)

  

 # Attention for Implementation

  1. 최초시도 틀린 이유 -> 입력이 여러줄일 수 있다.

  => 백준에서 별다른 종료 조건없이 입력이 여러줄일 수 있다라고 표기하는 경우에는 

      while ~ try ~ except문을 사용하되,  아래와 같이 사용한다 

      while True:

      try :   ... print(result)          => 즉, 각 입력에 대한 출력을 한번에 하는 것이 아닌, 입력by입력 순으로 처리하면 정답판정을 받는다.

      except : break  


'''

def rot13(value):

    if value in vowel:

        tmp_idx = vowel.index(value)

        if tmp_idx+3 > len(vowel)-1 : return vowel[tmp_idx+3 -len(vowel)]

        else : return vowel[tmp_idx+3]


    elif value in consonant:

        tmp_idx = consonant.index(value)

        if tmp_idx+10 > len(consonant)-1 : return consonant[tmp_idx+10 -len(consonant)]

        else : return consonant[tmp_idx+10]


    else: return value



vowel = ['a','i','y','e','o','u']

consonant = ['b', 'k', 'x', 'z', 'n', 'h', 'd', 'c', 'w', 'g', 'p', 'v', 'j', 'q', 't', 's', 'r', 'l', 'm', 'f']


while True:

    try : 

        string = list(input())

        result = []

        
        for value in string:

            if value.isalpha() and value.isupper(): 

                value = value.lower()

                value = rot13(value)

                value = value.upper()

                result.append(value)
        
            elif value.isalpha() and value.islower: 
        
                value = rot13(value)

                result.append(value)


            else: result.append(value)


        print(''.join(result))

    except : break



