
'''

 Backjoon _ exampels 15312

  "이름 궁합"   by Jinwoo Lee

  < algorithm >

  1. 이걸 DP로 어떻게 풀지 ?  
 

'''



def solution():

    name_1 = list(input())

    name_2 = list(input())

    alpha = {'A':3 , 'B':2, 'C':1 , 'D':2, 'E':3 , 'F':3, 'G':2 , 'H':3, 'I':3 , 'J':2, 'K':2 , 'L':1, 'M':2 , 'N':2, 'O':1 , 'P':2, 'Q':2 , 'R':2, 'S':1 , 'T':2, 'U':1 , 'V':1, 'W':1 , 'X':2, 'Y':2 , 'Z':1}

    candidate = [] 

    for idx in range(len(name_1)):

        candidate.extend ( str(alpha[name_1[idx]]) + str(alpha[name_2[idx]]))


    while len(candidate) != 2 :

        ans = [] 

        for idx in range(len(candidate)-1):

            ans.extend( str((int(candidate[idx]) + int(candidate[idx+1]))%10) )


        candidate = ans 


    print("".join(ans))

    


solution()