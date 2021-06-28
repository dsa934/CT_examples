'''

 Backjoon _ exampels #

  "Baek 1212 - 8진수 2진수(문자열)"   by Jinwoo Lee


 # Attention for Implementation

   - bin(), oct(), hex() 사용시 2,8,16진수 표현 가능 

     bin() -> 0b ...
     oct() -> 0o ...
     hex() -> 0x ...

   - format 함수를 통해 접두어 생략가능 



'''
# 8진수 -> 10진수 변환 
num= int(input(),8)

# 10진수 -> 2진수 변환
print(format(num, 'b'))

