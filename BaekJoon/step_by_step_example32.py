'''

 Backjoon _ exampels #

  "Baek - 2444"   by Jinwoo Lee


 # Attention for Implementation

  - 별찍기 표현할때 빈칸 + "*" 조합으로 나타내는 경우가 많은데 


     *
    ***
   *****        => 이와 같은 모양은 " " + "*" 조합이지 
  *******                           " " + "*" + " " 까지 고려할 필요는 없음 



'''

num = int(input())

for idx in range(0, num):

    print(" "*(num-idx-1) + "*"* (2*idx+1) )

for idx in range(num-2, -1,-1):

    print(" "*(num-idx-1) + "*"* (2*idx+1) )

