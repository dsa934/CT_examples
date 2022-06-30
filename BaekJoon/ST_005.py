

'''

 Backjoon _ exampels 21966

  "중략"   by Jinwoo Lee

  < algorithm >


  1. 문자열 slicing
  
    1) 뒤에서 n번쨰 : -n 

    2) 앞에서 n번쨰 :  n     =>  strng[n:-n] 과 같이 표기



  2. 조건에 의해 자른 문자열이 한 문자임을 판단하는 방법

    1) sub_string에 '.'이 포함되는가

    2) '.'의 위치가 문단의 제일 마지막인가


    * index('찾고자하는 표기') 사용 시, 문자열 안에 찾고자하는 표기가 없을 경우 에러가 발생 

      => '.'이 있는지부터 체크


    3) 주어진 조건들에 추가적으로, 중간 sub_string에 ','이 없는 경우 한문장에 속하기 떄문에 ...로 축약 가능


  * 이전에 온라인 코테 대회에서 실패한 코딩

 

'''




def solution():
    
    n = int(input())

    string = list(input())

    if n > 25 :
    
        sub_string = string[11:-11]
        

        if '.' in sub_string:
            
            if sub_string.index('.') == len(sub_string)-1:

                string[11:-11]='...'

            else:

                string[9:-10]='......'

        else :
            string[11:-11] ='...'

    print(''.join(string))

solution()