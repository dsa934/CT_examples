'''

 Backjoon _ exampels #

  "Baek 15904 - UCPC는 무엇의 약자일까? (Greedy)"   by Jinwoo Lee


 # Algorithm 

  0. 주어진 문자열을 축약해서 UCPC로 남길 수 있다면 UCPC의 약자이다. ( University CPC  ... ) 

  1. 주어진 문자열에서 대문자인 것만 따로 뽑기 (아스키코드 사용 )

  2. 덱을 사용하여 save, stack list를 만들어서  두 배열에서 요소하나씩 뺴서 같으면 둘다 pop 아니면 다시 집어넣음( stack은 앞으로, save는 뒤로 )

  3. stack이 비었으면 I love~ / else : i hate~


 # Attention for Implementation

  1. if stack 과 같은 형태로 사용할떄 ( if stack is empty ...)

    => stack = [] 선언시, stack에 요소가 있으면 True , 없으면 False임 


  2. in 을 사용하면 UPCC 반례가 생김 

    => 순서에 영향이 있음 

'''

from collections import deque 

string = list(input())

save = [char for char in string if ord(char) >=65 and ord(char)<= 90]


deq_save = deque(save)

deq_stack = deque(['U','C','P','C'])


cnt = 0
len_save = len(save)

while True:
    
    if cnt == len_save : 

        if not deq_stack :
            print("I love UCPC")
            break
        else:
            print("I hate UCPC")
            break

    if deq_stack : 

        stack = deq_stack.popleft()
        value = deq_save.popleft()

    
        if stack != value:
            deq_stack.appendleft(stack)
            deq_save.append(value)

    if not deq_stack : 
        print("I love UCPC")
        break

    cnt+=1


        

        