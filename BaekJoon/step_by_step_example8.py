'''

 Backjoon _ exampels #

  "Baek -1541 잃어버린 괄호"

 by Jinwoo Lee ( 2021/06/xx )


 # Attention for Implementation

  - eval() 함수는 012 같은 형태를 갖는 수를 처리하는데 제약이 있다.

  - 제일 처음에 -가 오는 경우도 고려했으나 문제에 가장 처음과 마지막이 숫자로 되어 있다고 명시 되있음 (뻘짓 주의)





'''


data = input().split('-')
total = 0


for value in data[0].split('+'):

    total += int(value)

for value in data[1:]:

    for sep_value in value.split('+'):

        total -= int(sep_value)

print(total)