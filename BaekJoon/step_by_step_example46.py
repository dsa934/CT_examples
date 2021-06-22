'''

 Backjoon _ exampels #

  "Baek 2812 - making bigger number(Greedy) "   by Jinwoo Lee


 # Algorithm 

  0. k개의 숫자를 지웠을떄 구할 수 있는 가장 큰 수 출력하기  1231234 -> 3234

  1. str형태로 입력받아 자리수 분리하여 str_list에 추가 

  2. stack을 구성, 비어있다면 str_list의 요소를 넣고, 그렇지 않다면 stack 요소와 str_list[0]을 대소비교 

  3. 살아남은 알파벳만 stack에 들어가게 된다.

  4. 지워지는 알파벳의 개수 == k이면, while 종료 나머지를 다 stack에 넣음 


 # Attention for Implementation

   - 마지막에 stack [ : (num-k) ] 인 이유 

     => 99999와 같이 중복된수가 들어올 경우 while문에서 따로 제거가 되지않기 때문에 길이만 따져서 출력



'''

num , k = list(map(int,input().split()))

str_list = list(input())

stack = [] 

cnt = 0
for number in str_list:

    while stack and stack[-1] < number:
        
        if cnt == k : 
            break

        stack.pop()
        cnt +=1
        

    stack.append(number)

print(''.join(stack[:(num-k)]))


