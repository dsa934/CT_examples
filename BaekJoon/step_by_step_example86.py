'''

 Backjoon _ exampels #

  "Baek 7567 - 그릇 "(문자열)   by Jinwoo Lee


'''

dish = input()

total = 0


if dish :
    total = 10

    for idx in range(len(dish)-1):

        if dish[idx] != dish[idx+1] : total+=10
        else: total+=5

    print(total)

else: print(total)