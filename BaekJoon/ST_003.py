
'''

 Backjoon _ exampels 1769

  "3의 배수 "   by Jinwoo Lee

  < algorithm >
 
  기본 문자열 문제 

'''




def transfer(string):
    

    cnt = 0
    
    answer = None

    while True:

        if len(string)== 1 : 
            
            answer = int(string)
            break


        string = list(string)

        tmp_total = 0

        for value in string:

            tmp_total += int(value)

        string = str(tmp_total)
        cnt +=1


    result = 'YES' if answer%3 == 0 else 'NO'

    return cnt, result


def solution():

    cnt, offset =transfer(input())

    print(cnt)
    print(offset)

solution()