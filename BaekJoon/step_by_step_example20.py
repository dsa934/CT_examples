'''

 Backjoon _ exampels #

  "Baek 4796 - 캠핑"

 by Jinwoo Lee ( 2021/06/xx )


 # Attention for Implementation



'''

date = []

while True:

    l, p, v = map(int,input().split())
    
    if l == 0 and p ==0 and v ==0:
        break
    
    else:
        date.append([l,p,v])


for idx, day in enumerate(date):

    if day[2] % day[1] < day[0]:
        
        answer = ((day[2] // day[1])*day[0]) + (day[2] % day[1] )

    else:

        answer = (((day[2] // day[1])*day[0]) + day[0] )



    print(f"Case {idx+1}:",answer )
