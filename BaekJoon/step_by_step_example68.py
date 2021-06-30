'''

 Backjoon _ exampels #

  "Baek 11655 - ROT13(문자열)"   by Jinwoo Lee


 # Algorithm 

  0. 13글자씩 밀어서 암호화, 대상이 알파벳일떄만 적용한다 .

  1. is_alpha를 통한 알파벳 체크, 아스키코드를 이용한 13글자씩 밀기 

  2. +13 할떄 범위체크 필요 

  

 # Attention for Implementation



'''


string = list(input())


result = []

for value in string:

    if value.isalpha() :

        # 대문자
        if ord(value) >=65 and ord(value) <= 90:

            if ord(value)+13 > 90 : result.append(chr(ord(value)+13 -26))


            else: result.append(chr(ord(value)+13))

        #소문자
        elif ord(value) >=97 and ord(value) <=122:

            if ord(value)+13 > 122 : result.append(chr(ord(value)+13-26))

            else: result.append(chr(ord(value)+13))

        

        ord(value)+13

    else:
        result.append(value)

print(''.join(result))