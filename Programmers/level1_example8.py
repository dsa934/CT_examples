'''

 Programmers _ exampels 8

  "이상한문자 만들기"

 by Jinwoo Lee ( 2021/05/27 )


 # Problem
 
  - 문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 각 단어는 하나 이상의 공백문자로 구분되어 있습니다. 
  - 각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.


 # 대문자 & 소문자 관련 function 

  - lower() : 문자열 소문자 변환 
  - upper() : 문자열 대문자 변환
  - capitalize() : 문자열 맨 첫글자 대문자 변환 문자열
  - title() : 내 알파벳 외 문자(숫자, 특문, 띄어쓰기 등) 로 구분된 알파벳의 첫글자를 모두 대문자
  
  * Example

   "triple - check algorithm"        => upper()                    TRIPLE-CHECK ALGORITHM
                                     => title()                    Triple-Check Algorithm
                                     => capitalize()               Triple-check algorithm

 # Attention for implementation

  - for word in s.split(" ") : 을 통해 공백으로 구분된 문자열 속 단어들 열거 가능

     => "life is too ... "  => "life", " ", "is", " ", "too"  

     => s.split(" ") : 공백을 기준으로 분류하여, 
     
     => for word in s.split(" ") :  문자열 속 단어, 공백을 차례대로 return하는 것이 포인트 

    
'''

def solution(s):
    
    result = []
    
    for word in s.split(" "):
        
        for idx, chr_value in enumerate(word) :
            
            if idx % 2 == 0:
                
                result.append( chr_value.upper())
                
            else:
                result.append(chr_value.lower())
                
        result.append(" ")
        
    # 마지막에 result.append("")에 의해 공백이 한번 더생기기 떄문에 [:-1]을 통해 마지막요소만제거
    return "".join(result[:-1])

            
            
