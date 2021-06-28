'''

 Backjoon _ exampels #

  "Baek 5430 - AC(문자열)"   by Jinwoo Lee


 # Algorithm 

  0. 주어진 규칙에 의한 새로운 언어 AC를 만들어보자 (규칙과, 배열을 받아서 R : reverse, D: drop 연산 시행 )


  1. R,D의 count를 세면 안됨 -> RDRD라는 반례가 생김 

     1-1. 지워지는 부분은 어쩄든 제일 끝부분 or 제일 첫번째 부분이다.

     1-2. D를 만났을때 r_flag 상태를 체크해서 앞,뒤 카운트를 세서 array[앞:뒤] 형태로 출력


  2. 출력에 주의 [2,1] 과 [2, 1]은 다르다

     2-1. append를 이용하면 [2, 1] 문제에서 요구하지 않는 원소간 공백이 생기기 떄문에 입력을 문자열의 형태로 받아야함 

     2.2. input().rtstrip()[1:-1].split(",") : (순서대로) 입력 + 우측공백제거 + [] 제거 + ',' 기준 분리 


  3. 마지막 출력부분 

    3-1. r_flag =True일 경우 , reverse를 통한 정렬이 아니라 구한 값 array[front:] or array[front:-1*back]에다가 [::-1]을 취하여 뒤집어 줌


  4. 시간초과 판정 

    4-1. 입력을 import sys 이용

    4-2. oper 연산 다룰떄 덱을 사용 

       => Deque ( doubly - ended - queue), pop / popleft 연산을 통해 O(1) 가능 

       => 보통의 D_list : prev,next 로 연결되있기 떄문에 index 접근이 불가능하여 O(n), 링크가2개라 메모리가 2배 

       => collection 의 deque는 [i]접근 연산자를 사용하여 인덱스처럼 접근하는데 이러면 O(1) or O(N) ? 

          -> 파이썬의 deque는 데이터를 하나씩 연결한것이 아닌, 데이터를 묶은 block 단위로 연결한 이중연결리스트 

          -> 따라서 deque의 index접근은 양끝에서 O(1), 데이터 중간에서는 O(N) 이번 문제 한정으로 양끝만 다루기 때문에 O(1)
  



 # Attention for Implementation

  1. reverse를 reverse 한다고 다시 뒤집히지 않는다. 
  
    => tmp = [1,2,3,4]  -> sorted(tmp, reverse=True) : [4,3,2,1] -> sorted(tmp,reverse=True)  : [4,3,2,1] 그대로   


  2. deque 사용시 \n이 포함됨으로 -1 해줌 

  3. front +back <= num_len  -> 같을떄도 고려해야함 



'''
import sys
from collections import deque


def cal(oper, num_len, array):

    front, back = 0,0
    oper = deque(oper[:-1])
    r_flag = False

    while oper:

        operation = oper.popleft()
      
        if operation == 'R':

            if not r_flag : r_flag = True

            elif r_flag : r_flag = False

       
        if operation =='D' :

            if r_flag : back +=1
            elif not r_flag : front +=1


    if front + back <= num_len : 

        if not r_flag and back == 0 :  return array[front:], True

        elif r_flag and back == 0 : return array[front:][::-1], True

        elif not r_flag and back != 0 : return array[front:-1*back], True

        elif r_flag and back !=0 : return array[front:-1*back][::-1], True

        
    else: return [], False



num_test = int(sys.stdin.readline())
result = []

for _ in range(num_test):

    oper = sys.stdin.readline()
    num_len = int(sys.stdin.readline())
    array = sys.stdin.readline().rstrip()[1:-1].split(",")


    array, flag = cal(oper, num_len, array)

    if flag : result.append('[' + ",".join(array) +"]")

    else: result.append("error")


for value in result:
    print(value)