'''

 Programmers _ exampels 3

  " 2016 years"

 by Jinwoo Lee ( 2021/05/24 )


 # Problem

    2016년 1월 1일은 금요일입니다. 2016년 a월 b일은 무슨 요일일까요? 두 수 a ,b를 입력받아 2016년 a월 b일이 무슨 요일인지 리턴하는 함수, solution을 완성하세요.
    요일의 이름은 일요일부터 토요일까지 각각 SUN,MON,TUE,WED,THU,FRI,SAT 입니다. 
    예를 들어 a=5, b=24라면 5월 24일은 화요일이므로 문자열 "TUE"를 반환하세요.


 # Condition

    2016년은 윤년입니다.
    2016년 a월 b일은 실제로 있는 날입니다. (13월 26일이나 2월 45일같은 날짜는 주어지지 않습니다)
'''

def solution(a, b):
    
    # set init params
    answer_list = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    additional_cnt = int((a-1)/2)
    passed_date = (a-1)*31 + b
    
    # calculate passed date
    passed_date -= additional_cnt

    if a>=3 :
        passed_date -= 1

        if a>=9 and a % 2 != 0:

            passed_date +=1

    
    result = answer_list[(passed_date % 7)-1]
    print(result)
    return result

solution(9,5)
solution(10,5)
solution(11,5)
solution(12,5)



'''
 # map & lambda 활용하는 코드도 있으니 참고하여 공부

def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
'''