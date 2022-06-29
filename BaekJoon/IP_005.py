

'''

 Backjoon _ exampels 1308

  " D-day"   by Jinwoo Lee

  < algorithm >

  1. 1000년의 기준 (윤년을 포함해서 계산 해야 함)


   1) 기본적으로 365 * 1000 = 365,000

   2) 1000년 동안 윤년이 평균적으로 몇번 있는가 ? (0을 포함 해야 함 )

     => 4로 나누어 떨어짐 : 1000/4 = 250 +1  = 251 

     => 100 으로 나누어 떨어짐 : 1000/100 = 10 + 1 = 11

     => 400 으로 나누어 떨어짐 : 0, 400, 800  = 2 +1 = 3

     => 251 - 11 + 3 = 243
  
    ∴ 365,000 + 243 = 365,243 


 

'''





def chk_yoon(year):

    if year % 400 == 0 : return True

    elif year % 100 != 0 and year % 4 == 0 : return True

    else : return False

def solution():
    
    start = list(map(int, input().split()))
    end =  list(map(int, input().split()))


    s_day, e_day = 0, 0 

    # add year
    for value in range(1, start[0]):

        if chk_yoon(value): s_day +=366
        else : s_day += 365

    for value in range(1, end[0]):

        if chk_yoon(value): e_day +=366
        else: e_day += 365



    mon2day = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31 }

    # add month
    for value in range(1,start[1]):

        if chk_yoon(start[0]) and value == 2: s_day += 29

        else : s_day += mon2day[value]

    
    for value in range(1,end[1]):

        if chk_yoon(end[0]) and value == 2: e_day += 29

        else : e_day += mon2day[value]


    # add day 
    s_day += start[2]
    e_day += end[2]

    answer = e_day - s_day

    
    if answer >= 365243 : print('gg')
    else:

        print(f'D-{answer}')

        

solution()