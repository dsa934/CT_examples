'''

 Backjoon _ exampels #

  "Baek 1057 - 토너먼트 (BF)"   by Jinwoo Lee


 # Algorithm 

  0. 지민, 한수, 총인원수가 주어질 때 지민 한수가 붙게 되는 라운드를 출력하는 프로그램 작성 

  1. 지민, 한수가 각각 짝수, 홀수일 경우에 

     => 홀수 : (a // 2) +1 , 짝수 : (a//2) 의 형태로 등수가 올라가게 된다. 


  2.  abs(지민-한수) == 1 &  min(지민,한수) == 홀수 & max(지민,한수) == 짝수 조건이 성립할 경우 해당 라운드에서 지민과 한수가 맞붙게 된다.


  3. flag를 설정하여 만나지 못하는 경우 -1을 출력한다. ( 전체인원수는 고려할 필요가 없다.)


'''

nums, jimin, hansu = list(map(int,input().split()))

result = 1

min_value = min(jimin, hansu)
max_value = max(jimin, hansu)

flag =False

while True:


    if abs(min_value - max_value) == 1 and min_value %2 != 0 and max_value %2 == 0:
        print(result)
        flag =True
        break

    else:

        result +=1

        if min_value %2 == 0: min_value //=2
        elif min_value %2 != 0 : 
            min_value = (min_value//2) +1

            

        if max_value %2 == 0 : max_value //=2
        elif max_value %2 != 0 : 
            max_value = (max_value //2) +1



if not flag : print(-1)


