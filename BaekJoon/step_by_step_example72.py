'''

 Backjoon _ exampels #

  "Baek 10820 - 문자열분석 (문자열)"   by Jinwoo Lee


 # Algorithm 

  0. 입력의 끝이 정해져 있지 않는다 -> while ~ try ~ except 

  1. 출력의 형태가 a, b, c, d와 같이 list가 아닌 경우 -> 2중포문 + print(end =" ") + 마지막원소일 경우 print(num) 처리 

  
 # Attention for Implementation

  - 추후 Core algorithm 복습시에 입출력 형태에 대해 체크하기 

'''

result = []

while True:

    try :
        string = list(input())

        num_lower = 0
        num_upper = 0
        num_number = 0
        num_empty = 0

        for value in string :

            
            if value.isalpha() and value.isupper() : num_upper+=1

            elif value.isalpha() and value.islower() : num_lower+=1

            elif value.isdigit() : num_number+=1

            else: num_empty +=1


        result.append([num_lower, num_upper, num_number, num_empty])

    except : 
        break

for value in result:

    for idx,nums in enumerate(value):

        if idx == len(value)-1 : print(nums)
        else : print(nums,end=" ")



