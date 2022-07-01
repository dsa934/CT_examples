
'''

 Backjoon _ exampels 20546

  "기적의 매매법"   by Jinwoo Lee

  < algorithm >

  1. BNP & Timing 매매 기법의 승률 구하기 

    1) BNP : 해당 날짜의 주식을 살 수 있다면 무조건 사서 마지막 날 되팔기 


    2)  연속으로 3일 오르거나, 내리거나를 기준으로 매매/매입을 진행

       => 이 문제에서 말하는 연속 3일은 

          현재일을 기준으로 idx-1, idx-2, idx-3일때 주가가 상승했는가를 의미 함
          
          a)  3일 연속 상승하면, 다음날 무조건 하락

          b)  3일 연속 하락하면, 다음날 무조건 상승 이지만 아래 예제를 보면

          ...  98 15 6 4 1 1 1 ... 와 같이 4번 하락하는 경우가 주어짐 


       ∴ 문제를 푸는 작성자는 2주치의 주식 가격을 미리 알고 있지만, 문제 속 가상의 인물 준현, 성민의 입장에서는 미래의 주식 가격을 알 수 없기 떄문에,

          a), b) 와 같은 '가정'을 하는 것임으로 

          프로그래밍 설계 시에는 현재의 날짜(idx)를 기준으로 

          [idx, idx-1], [idx-1, idx-2], [idx-2,idx-3] 조건을 비교하여 모두 크거나, 모두 작을 경우에 a,b에 맞는 매매법을 하도록 설계하면 된다.







         

'''

def BNP(money, stock):
    

    cnt = 0 

    cur_money = money

    last_price = stock[-1]

    for value in stock:

        if cur_money >= value :

            cnt += cur_money // value

            cur_money %= value


    return cur_money + (cnt*last_price)




def Timing(money, stock):
    
    cur_money, cnt = money, 0
    
    last_price = stock[-1]
    

    for idx in range(3,len(stock)):
        
        # up 
        if stock[idx] > stock[idx-1] and stock[idx-1] > stock[idx-2] and stock[idx-2] > stock[idx-3] :

            cur_money += cnt * stock[idx]

            cnt = 0

        # down
        elif stock[idx] < stock[idx-1] and stock[idx-1] < stock[idx-2] and stock[idx-2] < stock[idx-3] :
            

            cnt += cur_money // stock[idx]

            cur_money %= stock[idx]

  
    return cur_money + last_price*cnt



def solution():
    
    money = int(input())

    stock = list(map(int, input().split()))
   

    BNP_val = BNP(money,stock)
    Timing_val = Timing(money,stock)
    
    if BNP_val == Timing_val : answer = 'SAMESAME'

    elif BNP_val > Timing_val : answer = 'BNP'
    else : answer='TIMING'


    return answer



print (  solution() )