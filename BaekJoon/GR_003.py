
'''

 Backjoon _ exampels 14437

  "욱제는 효도쟁이야"   by Jinwoo Lee

  < algorithm >

  1. 무조건 원형으로 빙빙 돌아야지만 이동이 가능하기 떄문에 각 마을을 순서대로 방문했을 떄 최소비용을 묻는 문제임으로,

    '시작 지점'을 어디로 셋팅 하느냐에 따라 비용이 결정된다.


  2. 최초시도 )

     입력받은 이동비용 리스트를 복사하여 concate 한다. [1,2,3,4]  =>  [1,2,3,4,1,2,3,4]

     => 별다른 조치 없이, for문안에서 0~마을수 를 시작점으로 셋팅, [idx:idx+num-1]의 값을 비교해주면 됨

     => 이 경우 TLE 가 발셍


     해결 풀이 )

     전체 이동 경로를 더한 후, 가장 큰 값을 뺴는것이 일일히 비교하는 최초시도 보다 빠르게 진행 가능 

     
 

'''



def solution():

    num = int(input())

    cost = list(map(int, input().split()))

    cost.extend(cost)
    
    min_value = int(1e10)

    interval = num-1

    for idx in range(ㅜ):
        
        if min_value > sum(cost[idx:idx+interval]) :

            min_value = sum(cost[idx:idx+interval])

    print(min_value)
