'''

 Backjoon _ exampels #

  "Baek 16953 - A -> B"   by Jinwoo Lee


 # Algorithm 

  0. A -> B 를 가능한 연산 = [ * 2 , 1붙이기 ]을 사용하여 변환할떄의 연산사용의 최소값 구하기 

  1. B의 일의자리 수가 1이면 1을 제거한다.

  2. 1이 성립하지 않을경우 B를 짝수/홀수로 경우를 나눈다.

     if B % 2 == 0 :  B //= 2
     else : print(-1) 


 # Attention for Implementation

  - 홀수일 때를 고려하지 않으면 B //= 2 에서 소숫점의 몫에 대한 오차가 발생한다.



'''

a, b = list(map(int,input().split()))
cnt = 0 

while True:
    if b == a : 
        print(cnt+1)
        break

    elif b<a:
        print(-1)
        break

    chk = list(str(b))

    if chk[-1] == '1' : b = int("".join(chk[:-1]))
       

    else:

        if b % 2 == 0 : b //= 2
        else: 
            print(-1)
            break
        
    cnt +=1


