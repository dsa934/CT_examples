'''

 Backjoon _ exampels #

  "Baek - 1789 "

 by Jinwoo Lee ( 2021/06/xx )


 # Attention for Implementation

  - 서로 다른 N개의 자연수의 합이 S

    -> 만약 s= 80 이면

       [ 1,2,3,4,5,6,7,8,9,10, 11, 12 ] # 78 

       합이 80은 아니지만, 80에 근접한 78을 구했기 떄문에 12대신 14를 넣으면 80이됨 

       따라서 if result >s then chk-1을 해도 답이 됨



'''

import sys 

s = int(sys.stdin.readline())

chk = 0
result = 0

while True:


    result += chk

    if result > s:

        print(chk-1)
        break

    elif result == s:
        print(chk)
        break

    chk+=1


        




