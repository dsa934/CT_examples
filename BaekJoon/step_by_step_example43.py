'''

 Backjoon _ exampels #

  "Baek 1476 - 날짜 계산"   by Jinwoo Lee


 # Algorithm 

  0. E/S/M -> 지구의 연도로 몇년 ? 

  1. 1/1/1/ => 1, 1년지날때 3개다 +1 

  2. 그냥 while문으로 돌려서 풀면됨 


 # Attention for Implementation



'''

e, s, m = list(map(int, input().split()))


set_e, set_s, set_m = 1,1,1
cnt = 1

while True:

    if set_e == e and set_s == s and set_m ==m:
        print (cnt)
        break

    else:
        set_e+=1
        set_m+=1
        set_s+=1
        cnt +=1
        if set_e > 15 : set_e %= 15 

        if set_s > 28 : set_s %= 28

        if set_m > 19 : set_m %= 19

