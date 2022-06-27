
'''

 Backjoon _ exampels 1340

  "연도 진행바"   by Jinwoo Lee

  < algorithm >

  * 문자열로 들어오는 날짜를 분리하는 과정에서 hour 다음에 minute가 아닌 second로 계산해서 오류가 났던 문제

    => 복잡할수록 기록하고 코딩하기 

 

'''





def chk_yoon(year):

    

    if year % 400 == 0 : return True

 

    elif year % 4 == 0 and year % 100 !=0 : return True

 

    else : return False

 

 

def string_separate(string):

 

    string = string.replace(',', '')

 

    candidate = string.split(' ')

 

    month, day, year, time = candidate[0], candidate[1], candidate[2], candidate[3]

 

    time = time.split(':')

 

    hour, minute = time[0], time[1]

 

 

    return month, int(day), int(year), int(hour), int(minute)

 

def solution():

 

    month, day, year, hour, minute = string_separate(input())

 

    mon2num = {'January':1, 'February':2, 'March':3, 'April':4, 'May':5, 'June':6, 'July':7, 'August':8, 'September':9, 'October':10, 'November':11, 'December':12} 

 

    num2day = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

    

    yoon_offset = chk_yoon(year)

    

    whole_time = 0

 

    if yoon_offset: 

        whole_time = 366 * 24 * 60 * 60 

        num2day[2]=29

 

    else: whole_time = 365 * 24 * 60 * 60 

    

    answer = 0

    

    for n_month in range(1, mon2num[month]):

        

        answer += num2day[n_month]

    

    answer += day-1

    

    # today calculated hour, minute

    

    

    answer *= 24 * 60 * 60 

    

    answer += (hour*60*60) + (minute*60)

    

    print( answer/whole_time*100)

 

    

solution()