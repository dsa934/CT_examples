
'''

 Backjoon _ exampels 11034

  "캥거루 세마리2"   by Jinwoo Lee

  < algorithm >

  1. 같은 수평선상에 있다가 중요한 힌트

    A,B,C에 대하여,  A < B <  C 의 형태로 존재하며


    C-B 는 A가 들어갈 수 있는 공간

    B-A 는 C가 들어갈 수 있는 공간


    A,B,C 각각의 차이가 1이면 공간이 없기 떄문에 진입 불가능


    ∴  A,B,C = 4,6,10 

        C-B = 4 ( 7,8,9,10 )  - 1 , 10은 미포함이라 -1

        B-A = 2 ( 5,6 ) , 6은 미포함임으로 -1



        점화식 : max(B-A, C-B) -1 

 

'''





def solution():

    while True :

        try :

            a,b,c, = map(int, input().split())

            print( max(b-a, c-b) -1 )
       
        except:
            break

solution()