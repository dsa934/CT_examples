

'''

 Backjoon _ exampels 22864

  ""   by Jinwoo Lee

  < algorithm >
 

'''

def solution():
    
    a,b,c,m = list(map(int, input().split()))


    time, piro, work  = 0 , 0 , 0

    while True:
            
        if time == 24 : 
            print(work)
            break

        else :

            if piro + a <= m :

                piro += a
                work += b
                    
            else:

                piro -= c

                if piro < 0 : piro =0



            time +=1 


solution()