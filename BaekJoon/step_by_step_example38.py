'''

 Backjoon _ exampels #

  "Baek 1543 - 문서 검색"   by Jinwoo Lee


 # Algorithm 

  0. 주어진 문서이름에 대하여 검색하려는 단어가 겹치지 않게 몇번 중복되는지 체크하는 함수 

  1. list.find("문자열") 함수를 사용하면 해당 문자열이 시작하는 index를 알 수 있음 

  2. 1번에서 알게된 idx를 가지고, idx:idx+len(검색문자열) 만큼 ""로 대체

  3. 1,2를 문서이름 끝까지 반복 


 # Attention for Implementation

  - 문자열에 replace 함수 사용시 return 값을 받아줘야함 return_value = list.replace(...)

  - 주어진 문서 이름에서 검색하려는 단어가 몇번 중복되는지를 구하는 것이기 때문에 

    aaabbb / ab 의 경우 첫번쨰 ab를 지우고 ""로 대체하면 ab가 붙어서 또 지워지기 떄문에 " " 공백을 집어넣어 주어진 문서의 길이를 유지해야 함



'''


book = input()
str = input()
cnt = 0


while True:

    idx = book.find(str)

    if idx == -1 : break
    
    else:
        book = book.replace(book[idx:idx+len(str)], " "*len(str), 1)
        cnt +=1

print(cnt)



