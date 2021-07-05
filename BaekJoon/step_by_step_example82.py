'''

 Backjoon _ exampels #

  "(Greedy)"   by Jinwoo Lee


 # Algorithm 

  0. 

  1. 

  2.

  3.


 # Attention for Implementation

 1. 자리수가 다르면 무조건 0이다 




'''

min_value, max_value = input().split()

len_min = len(min_value)
len_max = len(max_value)

if len_min != len_max :  print(0)

else :

    cnt =0 

    for idx in range(len_max):

        if min_value[idx] != max_value[idx] : break

        else:

            if min_value[idx] == '8': cnt+=1
            
    print(cnt)