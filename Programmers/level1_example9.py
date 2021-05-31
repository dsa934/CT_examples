'''

 Programmers _ exampels 9

  "시저 암호"

 by Jinwoo Lee ( 2021/05/28 )


 # Problem

  - 어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다. 
  - 예를 들어 "AB"는 1만큼 밀면 "BC"가 되고, 3만큼 밀면 "DE"가 됩니다. "z"는 1만큼 밀면 "a"가 됩니다. 
  - 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.


 # Attention for implementation

  - ord : 문자 -> 문자의 유니코드 값 return  ( chr <-> ord)

  - 공백을 포함한 문자열 s에 대하여 for문 사용시 a, " ", B, " ", Z 순으로 str_value에 입력됨을 기억 

'''

def solution(s, n):

    # ASCII : a ~ z : 97 ~ 122 / A ~ Z : 65 ~90
    
    # set init params
    result = []
    
    for str_value in s:
        
        # empty space
        if ord(str_value) == 32 :
            
            result.append(str_value)
            
        elif str_value.islower() and ord(str_value)+n>122:
            
            result.append(chr(ord(str_value)+n -26))
            
        elif str_value.isupper() and ord(str_value)+n > 90:
            
            result.append(chr(ord(str_value)+n-26))
            
        else:
            result.append(chr(ord(str_value)+n))
            
    return ''.join(result)

solution("a B z", 4)