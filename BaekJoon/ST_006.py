

'''

 Backjoon _ exampels 4096

  "팰린드로미터"   by Jinwoo Lee

  < algorithm >

  1. 0 이면 입력 종료 

    => 입력으로 0000이 주어질 수도 있기 때문에 , int(''.join(num)) = 0 이면서, 길이가 1인지 체크 필요 ( 이 조건 불이행시 50% 에서 틀림 판정)


  2. 문자열 + 숫자

    1) 문자열 -> 숫자 변환 

       string = '00001234'  

       int( ''.join(string) )                    



    2) 숫자 -> 문자열

       num = 1234

       list( str(num) )    # 숫자를 문자열 화(str) 후 list로 선언해야 int object not iterable 오류 발생하지 않음 


    3) 문자열 + 숫자 펠린드롬 문제에서는  길이, 펠린드롬 여부를 체크해주면 된다


      * 길이 : 최초 길이 저장 후 ,  문자열을 숫자로 변환하는 과정에서 앞에 000이 사라짐으로  최초 길이 차이만큼 0을 더해준다 

      * raw 와 reverse가 같으면 펠린드롬         
      

'''




def chk_palindrome(num):

    cnt = 0

    length = len(num)
    
    while True :

        if ''.join(num) == ''.join(num[::-1]) and len(list(''.join(num))) == length: 
            
            break

        else:
            cnt +=1
            
            str2int = list(str(int(''.join(num)) + 1 ))

            differ = length - len(str2int)
            
            # algorithm - 3
            num = list(('0'*differ) + ''.join(str2int))        

    return cnt

    
   

def solution():

    while True:

        num = list(input())

        if len(num) == 1 and int(''.join(num)) == 0 :
            break

        else:

            print( chk_palindrome(num) )

    

solution()