
'''

 Backjoon _ exampels 14470

  "���ڷ�����"   by Jinwoo Lee

  < algorithm >

  1. �⺻���� simulation ���� 
 

'''



def solution():
    
    raw_temp = int(input())

    purpose_temp = int(input())

    freeze_up = int(input())

    melt = int(input())

    raw_up = int(input())


    cnt = 0 

    if raw_temp > 0 : flag = True

    else : flag = False


    while raw_temp != purpose_temp:

        if raw_temp < 0 :

            cnt += freeze_up

            raw_temp +=1

        elif raw_temp == 0 and not flag :

            flag = True

            cnt += melt



        elif raw_temp >= 0 and flag  :
            
            cnt += raw_up

            raw_temp +=1 
            
    print(cnt)



solution()